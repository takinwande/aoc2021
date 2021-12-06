#!/bin/env python3

GRID_SIZE = 991 # found by a pass on the input and figuring out max Xs and Ys (spoiler: they are the same value) (10 for test.txt)

def getLines():
  with open("day5.txt") as infile:
    lines = list(map(lambda line: line.strip(), infile.readlines()))
  pairs = list()
  for line in lines:
    points = line.split(' -> ')
    (x1, y1) = points[0].split(',')
    (x2, y2) = points[1].split(',')
    pairs.append([(int(x1), int(y1)), (int(x2), int(y2))])
  return pairs

def filterLines(lines, includeDiagonals):
  def isDiagonal(line):
    return abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1])

  filtered = list()
  for line in lines:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1] or (includeDiagonals and isDiagonal(line)):
      filtered.append(line)
  return filtered

def findDiagonals(pointA, pointB):
  (y1, x1) = pointA
  (y2, x2) = pointB
  diagonals = set()
  diagonals.add(pointA)
  diagonals.add(pointB)
  if x1 > x2 and y1 > y2:
    while x1 != x2 and y1 != y2:
      x1 -= 1
      y1 -= 1
      diagonals.add((y1, x1))
  elif x1 > x2 and y1 < y2:
    while x1 != x2 and y1 != y2:
      x1 -= 1
      y1 += 1
      diagonals.add((y1, x1))
  elif x1 < x2 and y1 > y2:
    while x1 != x2 and y1 != y2:
      x1 += 1
      y1 -= 1
      diagonals.add((y1, x1))
  elif x1 < x2 and y1 < y2:
    while x1 != x2 and y1 != y2:
      x1 += 1
      y1 += 1
      diagonals.add((y1, x1))
  return list(diagonals)

def drawLine(pointA, pointB, grid, includeDiagonals):
  def mark(x, y):
    if grid[x][y] == '.':
      grid[x][y] = 1
    else:
      grid[x][y] += 1

  (y1, x1) = pointA
  (y2, x2) = pointB
  if x1 == x2: # horizontal line
    for y in range(min(y1, y2), max(y1, y2) + 1):
      mark(x1, y)
  elif y1 == y2: # vertical line
    for x in range(min(x1, x2), max(x1, x2) + 1):
      mark(x, y1)
  elif includeDiagonals:
    for point in findDiagonals(pointA, pointB):
      (y,x) = point
      mark(x, y)

def solution(lines, includeDiagonals=False):
  grids = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]
  filteredLines = filterLines(lines, includeDiagonals)
  for line in filteredLines:
    drawLine(line[0], line[1], grids, includeDiagonals)
  print(sum([len([some for some in row if some != '.' and some >= 2]) for row in grids]))


def main():
  lines = getLines()
  solution(lines)
  solution(lines, includeDiagonals=True)


if __name__ == '__main__':
  main()
