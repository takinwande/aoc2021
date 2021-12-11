#!/bin/env python3

def getInput():
  with open("day10.txt") as infile:
    return list(map(lambda line: line.strip(), infile.readlines()))

def validate(chunk):
  stack = list()
  for char in chunk:
    if char in ['(', '[', '{', '<']:
      stack.append(char)
    elif (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (char == '}' and stack[-1] == '{') or (char == '>' and stack[-1] == '<'):
      stack.pop()
    else:
      popped = stack.pop()
      expected = None
      if popped == '(':
        expected = ')'
      elif popped == '[':
        expected = ']'
      elif popped == '{':
        expected = '}'
      elif popped == '<':
        expected = '>'
      return (expected, char)
  return (None, None)

def fix(chunk):
  stack = list()
  for char in chunk:
    if char in ['(', '[', '{', '<']:
      stack.append(char)
    elif (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (char == '}' and stack[-1] == '{') or (char == '>' and stack[-1] == '<'):
      stack.pop()
  completionSequence = list()

  stack.reverse()
  for char in stack:
    if char == '{':
      completionSequence.append('}')
    elif char == '(':
      completionSequence.append(')')
    elif char == '[':
      completionSequence.append(']')
    elif char == '<':
      completionSequence.append('>')
  return completionSequence

def part1(chunks):
  points = {')': 3, ']': 57, '}': 1197, '>': 25137}
  total = 0
  for chunk in chunks:
    (expected, found) = validate(chunk)
    if expected and found:
      print("Expected {}, but found {} instead.".format(expected, found))
      total += points[found]
  print(f'Part 1: {total}')


def part2(chunks):
  points = {')': 1, ']': 2, '}': 3, '>': 4}
  scores = list()
  for chunk in chunks[:]:
    (expected, found) = validate(chunk)
    if expected and found:
      chunks.remove(chunk)

  for incomplete in chunks:
    total = 0
    completion = fix(incomplete)
    for char in completion:
      total *= 5
      total += points[char]
    scores.append(total)

  scores = sorted(scores)
  middle = len(scores) // 2
  print(scores[middle])

def main():
  chunks = getInput()
  part1(chunks)
  part2(chunks)


if __name__ == '__main__':
  main()
