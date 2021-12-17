# #!/bin/env python3

import re

def getInput():
  with open("day17.txt") as infile:
    return infile.read().strip()

def performStep(x, y, dx, dy):
  x += dx
  y += dy
  if dx > 0:
    dx -= 1
  elif dx < 0:
    dx += 1
  dy -= 1
  return (x, y, dx, dy)

def isWithinTarget(x, y, atLeastX, atMostX, atLeastY, atMostY):
  return atLeastX <= x and x <= atMostX and atLeastY <= y and y <= atMostY

def outOfBounds(x, y, atMostX, atLeastY):
  return x > atMostX or y < atLeastY

def part1(atLeastX, atMostX, atLeastY, atMostY):
  maxYs = list()

  for initialdx in range(-200, 200):
    for initialdy in range(-200, 200):
      x, y = 0, 0
      dx, dy = initialdx, initialdy
      maxY = y
      while not outOfBounds(x, y, atMostX, atLeastY):
        x, y, dx, dy = performStep(x, y, dx, dy)
        if y > maxY:
          maxY = y
        if isWithinTarget(x, y, atLeastX, atMostX, atLeastY, atMostY):
          maxYs.append(maxY)
  print(f'Part 1: {max(maxYs)}')


def part2(atLeastX, atMostX, atLeastY, atMostY):
  count = 0

  for initialdx in range(-200, 200):
    for initialdy in range(-200, 200):
      x, y = 0, 0
      dx, dy = initialdx, initialdy
      while not isWithinTarget(x, y, atLeastX, atMostX, atLeastY, atMostY) and not outOfBounds(x, y, atMostX, atLeastY):
        x, y, dx, dy = performStep(x, y, dx, dy)
      if isWithinTarget(x, y, atLeastX, atMostX, atLeastY, atMostY):
        count += 1
  print(f'Part 2: {count}')

def main():
  values = getInput()
  (atLeastX, atMostX, atLeastY, atMostY) = re.search(r'x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', values).groups()
  (atLeastX, atMostX, atLeastY, atMostY) = (int(atLeastX), int(atMostX), int(atLeastY), int(atMostY))
  part1(atLeastX, atMostX, atLeastY, atMostY)
  part2(atLeastX, atMostX, atLeastY, atMostY)

if __name__ == '__main__':
  main()
