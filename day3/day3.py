#!/bin/env python3

def getInput():
    with open("day3.txt") as infile:
        input = list(map(lambda line: line.strip(), infile.readlines()))
    return input

def mostAndLeastCommonValues(values):
    countOfZero = 0
    countOfOne = 0
    for value in values:
        if value == '0':
            countOfZero += 1
        elif value == '1':
            countOfOne += 1
    if countOfZero > countOfOne:
        return ('0', '1')
    else:
        return ('1', '0')

def filter(instructions, columnIndex, bit):
    length = len(instructions)
    while length != 1:
        values = list()
        for rowIndex in range(length):
            values.append(instructions[rowIndex][columnIndex])
        filteredValue = mostAndLeastCommonValues(values)[bit]
        filteredList = list()
        for number in instructions:
            if number[columnIndex] == filteredValue:
                filteredList.append(number)
        if len(filteredList) == 1:
            return filteredList[0]
        else:
            return filter(filteredList, columnIndex + 1, bit)

def part1(instructions):
    gammaList = list()
    epsilonList = list()
    for colIndex in range(len(instructions[0])):
        values = list()
        for rowIndex in range(len(instructions)):
            values.append(instructions[rowIndex][colIndex])
        (mostCommonValue, leastCommonValue) = mostAndLeastCommonValues(values)
        gammaList.append(mostCommonValue)
        epsilonList.append(leastCommonValue)
    gamma = (int(''.join(gammaList), 2))
    epsilon = (int(''.join(epsilonList), 2))
    print("Part 1: {}".format(gamma * epsilon))


def part2(instructions):
    ogr = int(''.join(filter(instructions, 0, 0)), 2)
    csr = int(''.join(filter(instructions, 0, 1)), 2)
    print("Part 2: {}".format(ogr * csr))


def main():
    instructions = getInput()
    part1(instructions)
    part2(instructions)



if __name__ == '__main__':
    main()
