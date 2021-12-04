#!/bin/env python3

class BingoBoard(object):
  def __init__(self, boardList):
    super(BingoBoard, self).__init__()
    self.board = list()
    for row in boardList:
      toList = [value for value in row.strip().split(' ') if value != '']
      self.board.append(toList)


  def mark(self, value):
    for rowIndex, row in enumerate(self.board):
      if value in row:
        valueIndex = row.index(value)
        self.board[rowIndex][valueIndex] = '-'

  def isWinner(self):
    # check rows
    for row in self.board:
      if row.count('-') == 5:
        return True
    # check columns
    for colIndex in range(5):
      sumOfDash = 0
      for rowIndex in range(5):
        if self.board[rowIndex][colIndex] == '-':
          sumOfDash += 1
      if sumOfDash == 5:
        return True
    return False

  def sumOfValues(self):
    result = 0
    for row in self.board:
      for value in row:
        if value != '-':
          result += int(value)
    return result

def getInput():
  with open("day4.txt") as infile:
    return infile.read().split('\n')

def createGameBoards():
  inputValues = getInput()
  instructions = inputValues[0].split(',')
  bingoBoards = list()
  index = 2
  while index < len(inputValues[2:]):
    board = list()
    while inputValues[index] != '':
      board.append(inputValues[index])
      index += 1
    index += 1
    bingoBoard = BingoBoard(board)
    bingoBoards.append(bingoBoard)
  return (instructions, bingoBoards)

def part1(values, boards):
  winnerFound = False
  for value in values:
    if winnerFound:
      break
    for board in boards[:]:
      board.mark(value)
    for board in boards[:]:
      if board.isWinner():
        sumOfValues = board.sumOfValues()
        print("Part 1: {} * {} = {}".format(value, sumOfValues, int(value) * sumOfValues))
        winnerFound = True

def part2(values, boards):
  currentValue = None
  for value in values:
    if currentValue:
      break
    for board in boards[:]:
      board.mark(value)
    for board in boards[:]:
      if board.isWinner():
        boards.remove(board)
        if not boards:
          currentValue = value
  sumOfValues = board.sumOfValues()
  print("Part 2: {} * {} = {}".format(currentValue, sumOfValues, int(currentValue) * sumOfValues))


def main():
  values, boards = createGameBoards()
  part1(values, boards)
  part2(values, boards)


if __name__ == '__main__':
  main()
