#!/bin/env python3

def getInput():
  with open("day7.txt") as infile:
    return list(map(lambda val: int(val), infile.read().strip().split(',')))

def part1(values):
  fuelCost = dict()
  length = len(values)
  for position in values:
    cost = 0
    for index in range(length):
      cost += abs(values[index] - position)
    fuelCost[position] = cost
  print(f'Part 1: {min(fuelCost.values())}')

def part2(values):
  minimum = 10000000000000 # Some absurdly large minimum
  possiblePositions = range(min(values), max(values) + 1)
  fuelCost = {0: 0}
  for position in range(1, max(values) + 1):
    fuelCost[position] = position + fuelCost[position - 1]

  for position in possiblePositions:
    cost = 0
    for value in values:
      key = abs(value - position)
      cost += fuelCost[key]
    minimum = min(cost, minimum)
  print(f'Part 2: {minimum}')


def main():
  values = getInput()
  part1(values)
  part2(values)


if __name__ == '__main__':
  main()
