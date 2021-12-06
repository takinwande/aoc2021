#!/bin/env python3

def getInput():
  with open("day6.txt") as infile:
    return list(map(lambda val: int(val), infile.read().strip().split(',')))

def part1(countOfAges):
  breed(countOfAges, 80)
  print(sum(countOfAges))

def part2(countOfAges):
  breed(countOfAges, 256)
  print(sum(countOfAges))

def breed(countOfAges, numberOfDays):
  for day in range(numberOfDays):
    countOfAgeZero = countOfAges.pop(0)
    countOfAges[6] += countOfAgeZero
    countOfAges.append(countOfAgeZero) # spawns

def initialCountOfAges(initialState):
  countOfAges = list()
  for value in range(9):
    countOfAges.append(initialState.count(value))
  return countOfAges


def main():
  countOfAges = initialCountOfAges(getInput())
  part1(countOfAges[:])
  part2(countOfAges[:])


if __name__ == '__main__':
  main()
