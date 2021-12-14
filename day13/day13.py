# #!/bin/env python3

def getInput():
  with open("day13.txt") as infile:
    return list(map(lambda line: line.strip(), infile.readlines()))

def getParameters(values):
  maxX = 0
  maxY = 0
  dots = list()
  for index, value in enumerate(values):
    if value == '':
      continue
    if value.startswith("fold"):
      break
    (x, y) = list(map(lambda xOrY: int(xOrY), value.split(',')))
    dots.append((x, y))
    if x > maxX:
      maxX = x
    if y > maxY:
      maxY = y
  instructions = values[index:]
  return (dots, maxX, maxY, instructions)

def createGrid(dots, maxX, maxY):
  grid = [['.'] * (maxX + 1) for _ in range(maxY + 1)]
  for (x, y) in dots:
    grid[y][x] = '#'
  return grid

def printGrid(grid):
  for row in grid:
    print(''.join(row))
  print('\n')

def performFold(grid, instruction):
  indexOfEqual = instruction.index('=')
  axis = instruction[indexOfEqual - 1]
  value = int(instruction[indexOfEqual + 1:])

  if axis == 'y': # fold up, drop everything below value, and copy into length - index - 1
    length = len(grid)
    for index in range(value + 1, length):
      # copy from index into length - index - 1
      copyTo = length - index - 1
      for columnIndex in range(0, len(grid[index])):
        if grid[index][columnIndex] == '#':
          grid[copyTo][columnIndex] = '#'
    return grid[0: value]
  elif axis == 'x': # fold left, drop everything to the right of value
    newGrid = list()
    for rowIndex, row in enumerate(grid):
      length = len(row)
      for index in range(value + 1, length):
        copyTo = length - index - 1
        if row[index] == '#':
          row[copyTo] = '#'
      newGrid.append(row[0: value])
    return newGrid

def part1(values):
  (dots, maxX, maxY, foldInstructions) = getParameters(values)
  grid = createGrid(dots, maxX, maxY)
  grid = performFold(grid, foldInstructions[0])
  countOfHash = 0
  for row in grid:
    countOfHash += row.count('#')
  print(f'Part 1: {countOfHash}')

def part2(values):
  (dots, maxX, maxY, foldInstructions) = getParameters(values)
  grid = createGrid(dots, maxX, maxY)
  for instruction in foldInstructions:
    grid = performFold(grid, instruction)
  print("Part 2:")
  printGrid(grid)

def main():
  values = getInput()
  part1(values)
  part2(values)

if __name__ == '__main__':
  main()
