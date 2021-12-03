#!/bin/env python3

def getInput():
    with open("day2.txt") as infile:
        input = list(map(lambda line: line.strip(), infile.readlines()))
    return input

def main():
	instructions = getInput()
	part1(instructions)
	part2(instructions)

def forward(position, value):
	position[1] += value

def down(position, value):
	position[0] += value

def up(position, value):
	position[0] -= value

def forward2(position, value):
	position[1] += value
	position[0] += value * position[2]

def down2(position, value):
	position[2] += value

def up2(position, value):
	position[2] -= value

def part1(instructions):
	position = [0, 0]
	for instruction in instructions:
		command, value = instruction.split()
		if command == 'forward':
			forward(position, int(value))
		elif command == 'down':
			down(position, int(value))
		elif command == 'up':
			up(position, int(value))
	print(position[0] * position[1])


def part2(instructions):
	position = [0, 0, 0]
	for instruction in instructions:
		command, value = instruction.split()
		if command == 'forward':
			forward2(position, int(value))
		elif command == 'down':
			down2(position, int(value))
		elif command == 'up':
			up2(position, int(value))
	print(position[0] * position[1])



if __name__ == '__main__':
	main()