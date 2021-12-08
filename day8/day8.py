#!/bin/env python3

def getInput():
  with open("day8.txt") as infile:
    lines = list(map(lambda line: line.strip(), infile.readlines()))
  output = list()
  for line in lines:
    output.append(line.split(' | '))
  return output


def part1(values):
  count = 0
  for (_, output) in values:
    for segment in output.split(' '):
      if len(segment) in [2, 3, 4, 7]:
        count += 1
  print(f'Part 1: {count}')

def contains(str1, str2):
  # return true if every character in str1 appears in str2
  for char in str1:
    if char not in str2:
      return False
  return True

def solve(digits):
  # Solve for 3:
  # 3 must have all the digits in 1
  threeList = digits[3]
  for value in threeList:
    if contains(digits[1], value):
      digits[3] = value
      break
  # Remove 3 from 2 and 5
  for key in [2, 5]:
    digits[key].remove(digits[3])

  # Solve for 9:
  # 9 Must have all the digits in 4
  nineList = digits[9]
  for value in nineList:
    if contains(digits[4], value):
      digits[9] = value
      break
  #Remove nine from 0, 6
  for key in [0, 6]:
    digits[key].remove(digits[9])

  # Solve for 5 and 2 by using 9 and 8 (whatever value is in 8 but not in 9 is the difference between 2 and 5)
  letterInTwoButNotFive = [value for value in sorted(digits[8]) if value not in sorted(digits[9])][0]
  twoList = digits[2]
  for value in twoList:
    if letterInTwoButNotFive in value:
      digits[2] = value
      break
  digits[5].remove(digits[2])
  digits[5] = digits[5][0]

  # Solve 0:
  # 0 must have all the digits in 7, since we already know what 9 is
  zeroList = digits[0]
  for value in zeroList:
    if contains(digits[7], value):
      digits[0] = value
      break
  # Remove zero from 6
  digits[6].remove(digits[0])
  digits[6] = digits[6][0]


def part2(values):
  count = 0
  for (input, output) in values:
    digits = { 0: [], 1: '', 2: [], 3: [], 4: '', 5: [], 6: [], 7: '', 8: '', 9: [] }
    for segment in input.split(' '):
      segmentLength = len(segment)
      if segmentLength == 2:
        digits[1] = segment
      elif segmentLength == 4:
        digits[4] = segment
      elif segmentLength == 3:
        digits[7] = segment
      elif segmentLength == 7:
        digits[8] = segment
      elif segmentLength == 5:
        digits[2].append(segment)
        digits[3].append(segment)
        digits[5].append(segment)
      elif segmentLength == 6:
        digits[0].append(segment)
        digits[6].append(segment)
        digits[9].append(segment)
    solve(digits)

    segmentKey = dict()
    for (key, value) in digits.items():
      segmentKey[''.join(sorted(value))] = str(key)

    outputList = list()
    for outputSegment in output.split(' '):
      key = ''.join(sorted(outputSegment))
      outputList.append(segmentKey[key])
    # print("SEGMENT VALUE IS: {}".format(''.join(outputList)))
    count += int(''.join(outputList))
  print(f'Part 2: {count}')


def main():
  values = getInput()
  part1(values)
  part2(values)


if __name__ == '__main__':
  main()
