# Day 16: Packet Decoder
from functools import reduce

HEX_TO_BITS_MAPPING = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def parse_file(fd):
    return (fd.readline().rstrip(),)


def encode_packet(message):
    def _calc_result(type_id, values):
        if type_id == "000":
            return sum(values)
        if type_id == "001":
            return reduce(lambda x, y: x * y, values)
        if type_id == "010":
            return min(values)
        if type_id == "011":
            return max(values)
        if type_id == "100":
            assert len(values) == 1
            return values
        if type_id == "101":
            assert len(values) == 2
            return 1 if values[0] > values[1] else 0
        if type_id == "110":
            assert len(values) == 2
            return 1 if values[0] < values[1] else 0
        if type_id == "111":
            assert len(values) == 2
            return 1 if values[0] == values[1] else 0

    def _encode_literal_value_packet(message):
        i = 0
        value = ""
        while message[i] == "1":
            value += message[i + 1 : i + 5]
            i += 5
        value += message[i + 1 : i + 5]
        i += 5
        return i, 0, int(value, 2)

    def _encode_operator_packet_type_1(message):
        preamble_length = 15
        preamble, message = message[:preamble_length], message[preamble_length:]
        subpackets_length = int(preamble, 2)
        subpackets = message[:subpackets_length]
        packet_length = subpackets_length + preamble_length

        version_sum = 0
        values = []
        while subpackets_length > 0:
            subpacket_length, version, value = encode_packet(subpackets)
            values.append(value)
            version_sum += version
            subpackets = subpackets[subpacket_length:]
            subpackets_length -= subpacket_length
        assert subpackets_length == 0

        return packet_length, version_sum, values

    def _encode_operator_packet_type_2(message):
        preamble_length = 11
        preamble, message = message[:preamble_length], message[preamble_length:]
        subpackets_number = int(preamble, 2)
        subpackets = message

        packet_length = preamble_length
        version_sum = 0
        values = []
        for _ in range(subpackets_number):
            subpacket_length, version, value = encode_packet(subpackets)
            values.append(value)
            version_sum += version
            packet_length += subpacket_length
            subpackets = subpackets[subpacket_length:]

        return packet_length, version_sum, values

    preamble_length = 6
    version, type_id, body = message[:3], message[3:6], message[6:]
    version = int(version, 2)

    version_sum = version
    packet_length = preamble_length
    if type_id == "100":
        body_length, version, value = _encode_literal_value_packet(body)
    else:
        length_type_id, body = body[0], body[1:]
        packet_length += 1
        if length_type_id == "0":
            body_length, version, values = _encode_operator_packet_type_1(body)
        else:
            body_length, version, values = _encode_operator_packet_type_2(body)
        value = _calc_result(type_id, values)

    packet_length += body_length
    version_sum += version
    return packet_length, version_sum, value


def sum_versions_in_packets(message):
    message = "".join(map(lambda h: HEX_TO_BITS_MAPPING[h], message))
    return encode_packet(message)[1]


def calculate_results_from_transmission(message):
    message = "".join(map(lambda h: HEX_TO_BITS_MAPPING[h], message))
    return encode_packet(message)[2]


solution_function_01 = sum_versions_in_packets
solution_function_02 = calculate_results_from_transmission
