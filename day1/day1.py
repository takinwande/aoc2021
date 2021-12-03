#!/bin/env python3

def getInput():
    with open("day1.txt") as infile:
        input = list(map(lambda line: int(line.strip()), infile.readlines()))
    return input

def main():
	values = getInput()
	part1(values)
	part2(values)

def part1(values):
	result = 0
	for index in range(len(values) - 1):
		if values[index + 1] > values[index]:
			result += 1
	print(result)

def part2(values):
	# Generate sliding window
	slidingWindows = list()
	for index in range(len(values) - 2):
		slidingWindows.append(values[index] + values[index+1] + values[index + 2])

	result = 0
	for index in range(len(slidingWindows) - 1):
		if slidingWindows[index + 1] > slidingWindows[index]:
			result += 1
	print(result)


if __name__ == '__main__':
	main()
