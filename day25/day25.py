#!/bin/env python3

def getInput():
  with open("day25.txt") as infile:
    return list(map(lambda line: list(line.strip()), infile.readlines()))

def printGrid(grid):
  for row in grid:
    print(''.join(row))
  print("\n")

def performMoves(grid, moves):
  for move in moves:
    char, (fromRowIndex, fromCharIndex), (toRowIndex, toCharIndex) = move
    grid[toRowIndex][toCharIndex] = char
    grid[fromRowIndex][fromCharIndex] = '.'

def performStep(grid):
  # Figure out which `>` can move
  eastMoves = list()
  length = len(grid[0])
  for rowIndex, row in enumerate(grid):
    for eastIndex, east in enumerate(row):
      if east == '>' and grid[rowIndex][(eastIndex + 1) % length] == '.':
        eastMoves.append(('>', (rowIndex, eastIndex), (rowIndex, (eastIndex + 1) % length)))
  performMoves(grid, eastMoves)

  # Figure out which `v` can move
  southMoves = list()
  length = len(grid)
  for rowIndex, row in enumerate(grid):
    for southIndex, south in enumerate(row):
      if south == 'v' and grid[(rowIndex + 1) % length][southIndex] == '.':
        southMoves.append(('v', (rowIndex, southIndex), ((rowIndex + 1) % length, southIndex)))
  performMoves(grid, southMoves)
  return len(eastMoves) == 0 and len(southMoves) == 0


def part1(grid):
  # printGrid(grid)
  steps = 1
  while not performStep(grid):
    steps += 1
    # printGrid(grid)
  print(f'Part 1: {steps}')

def main():
  grid = getInput()
  part1(grid[:])

if __name__ == '__main__':
  main()
