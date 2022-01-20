# Advent of Code 2021

As written in the [Wikipedia](https://en.wikipedia.org/wiki/Advent_of_Code)
> Advent of Code is an annual set of Christmas-themed computer programming challenges that follow an Advent calendar

My solutions to the 2021 edition [Advent of Code 2021](https://adventofcode.com/2021) are written in Python.

## Running code
The code was written using `Python 3.8.10`, however it should be compatible with the default `python3` command.

To run the solution for a given day for a given task run simply:
```sh
python3 run_solution.py --day 09 --task 02
```
The output is the time duration of the calculations.
```sh
day_09_task_02 took 0.00646[s]
```

By default the solution is run 100 times to have a stabilized time duration result. However there is a possibility to set it to your needs:
```sh
python3 run_solution.py --day 09 --task 02 --retry 10
```

You may want to check the calculated result with the expected one. In that case run:
```sh
python3 run_solution.py --day 07 --task 02 --expected-result 100
```

## Overview
From 25 days of tasks, the solutions for day 22th is still missing.

To run all task, the special script has been created:
```sh
./run_all.sh
```
