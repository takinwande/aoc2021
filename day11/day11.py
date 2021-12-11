#!/bin/env python3

class Octopus(object):
  def __init__(self, energy):
    super(Octopus, self).__init__()
    self.energy = energy
    self.flashes = 0

  def increaseEnergy(self):
    self.energy += 1
    if self.energy == 10:
      self.flashes += 1

  def reset(self):
    if self.energy >= 10:
      self.energy = 0


def debug(octopuses):
  for row in octopuses:
    energies = [str(octopus.energy) for octopus in row]
    print(''.join(energies))

def getInput():
  with open("day11.txt") as infile:
    return list(map(lambda line: line.strip(), infile.readlines()))

def performStep(octopuses):
  def increaseNeighborsEnergies(currentRow, currentCol):
    for row in range(currentRow - 1, currentRow + 1 + 1):
      for column in range(currentCol - 1, currentCol + 1 + 1):
        if row < 0 or row >= len(octopuses) or column < 0 or column >= len(octopuses[row]):
          continue
        octopus = octopuses[row][column]
        octopus.increaseEnergy()
        if octopus.energy == 10:
          increaseNeighborsEnergies(row, column)

  for rowIndex in range(len(octopuses)):
    for colIndex in range(len(octopuses[rowIndex])):
      octopus = octopuses[rowIndex][colIndex]
      octopus.increaseEnergy()
      if octopus.energy == 10:
        increaseNeighborsEnergies(rowIndex, colIndex)

  for row in octopuses:
    for octopus in row:
      octopus.reset()

def part1(octopuses, printDebug = False):
  flashes = 0
  if printDebug:
    print("Before any steps:")
    debug(octopuses)

  for step in range(100):
    performStep(octopuses)
    if printDebug:
      print("\nAfter step {}".format(step + 1))
      debug(octopuses)

  for row in octopuses:
    flashes += sum([octopus.flashes for octopus in row])

  print(f'Part 1: {flashes}')

def part2(octopuses):
  def synchronized():
    for row in octopuses:
      for octopus in row:
        if octopus.energy != 0:
          return False
    return True

  count = 0
  while not synchronized():
    performStep(octopuses)
    count += 1

  print(f'Part 2: {count}')

def main():
  values = getInput()
  part1([[Octopus(int(energy)) for energy in row] for row in values])
  part2([[Octopus(int(energy)) for energy in row] for row in values])

if __name__ == '__main__':
  main()
