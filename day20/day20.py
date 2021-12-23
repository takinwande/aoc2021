#!/bin/env python3

def getInput():
  with open("day20.txt") as infile:
    return list(map(lambda line: list(line.strip()), infile.readlines()))

def printImage(image):
  for row in image:
    print(''.join(row))
  print("\n\n\n")

def frame(image, iteration):
  # Add a top/bottom row and left/right columns of dots or hashes depending on iteration
  newImage = list()
  length = len(image) + 2
  rowLength = len(image[0]) + 2
  character = '.' if iteration % 2 == 0 else '#'

  for index in range(length):
    if index in [0, length - 1]:
      newImage.append([character] * rowLength)
    else:
      value = image[index - 1]
      newImage.append([character] + value + [character])
  return newImage

def valueOf(character):
  return '1' if character == '#' else '0'

def enhance(algorithm, image, iteration):
  outputImage = list()
  framedImage = frame(image, iteration)
  borderChar = framedImage[0][0]
  for rowIndex, row in enumerate(framedImage):
    imageRow = list()
    for colIndex, col in enumerate(row):
      values = [
        (rowIndex-1, colIndex-1), (rowIndex-1, colIndex), (rowIndex-1, colIndex+1),
        (rowIndex, colIndex-1), (rowIndex, colIndex), (rowIndex, colIndex+1),
        (rowIndex+1, colIndex-1), (rowIndex+1, colIndex), (rowIndex+1, colIndex+1)
      ]
      stringRepresentation = ""
      for (x, y) in values:
        if x < 0 or y < 0 or x >= len(framedImage) or y >= len(framedImage[0]):
          stringRepresentation += valueOf(borderChar)
        else:
          stringRepresentation += valueOf(framedImage[x][y])
      index = int(stringRepresentation, 2)
      imageRow.append(algorithm[index])
    outputImage.append(imageRow)
  return outputImage

def part1(algorithm, image):
  for iteration in range(2):
    image = enhance(algorithm, image, iteration)
  countOfHash = 0
  for row in image:
    countOfHash += row.count('#')
  print(f'Part 1: {countOfHash}')

def part2(algorithm, image):
  for iteration in range(50):
    image = enhance(algorithm, image, iteration)
  countOfHash = 0
  for row in image:
    countOfHash += row.count('#')
  print(f'Part 2: {countOfHash}')

def main():
  values = getInput()
  part1(values[0], values[2:])
  part2(values[0], values[2:])

if __name__ == '__main__':
  main()
