#!/bin/env python3

class ALU(object):
  def __init__(self,):
    super(ALU, self).__init__()
    self.registers = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }

  def inp(self, char, value):
    self.registers[char] = value

  def add(self, a, b):
    if isinstance(b, str):
      self.registers[a] = self.registers[a] + self.registers[b]
    else:
      self.registers[a] = self.registers[a] + b

  def mul(self, a, b):
    if isinstance(b, str):
      self.registers[a] = self.registers[a] * self.registers[b]
    else:
      self.registers[a] = self.registers[a] * b

  def div(self, a, b):
    if isinstance(b, str):
      self.registers[a] = self.registers[a] // self.registers[b]
    else:
      self.registers[a] = self.registers[a] // b

  def mod(self, a, b):
    if isinstance(b, str):
      self.registers[a] = self.registers[a] % self.registers[b]
    else:
      self.registers[a] = self.registers[a] % b

  def eql(self, a, b):
    if isinstance(b, str):
      self.registers[a] = 1 if self.registers[a] == self.registers[b] else 0
    else:
      self.registers[a] = 1 if self.registers[a] == b else 0


def getInput():
  with open("day24.txt") as infile:
    return list(map(lambda line: line.strip(), infile.readlines()))

def parse(instruction):
  operation = instruction[0:3]
  operands = instruction[4:].split(' ')
  if operands[-1].isdigit() or operands[-1].startswith('-'):
    operands[-1] = int(operands[-1])
  return operation, operands

def runProgram(instructions, num):
  num = list(num)
  inputPointer = 0
  alu = ALU()
  for instruction in instructions:
    operation, operands = parse(instruction)
    if operation == 'inp':
      alu.inp(operands[0], int(num[inputPointer]))
      inputPointer += 1
    elif operation == 'add':
      alu.add(operands[0], operands[1])
    elif operation == 'mul':
      alu.mul(operands[0], operands[1])
    elif operation == 'div':
      alu.div(operands[0], operands[1])
    elif operation == 'mod':
      alu.mod(operands[0], operands[1])
    elif operation == 'eql':
      alu.eql(operands[0], operands[1])
  if alu.registers['z'] == 0:
    return True
  else:
    return False

def part1(instructions):
  for num in fourteenDigitNumber():
    if runProgram(instructions, num):
      print(num)
      break

def fourteenDigitNumber():
  for a in range(9,0,-1):
    for b in range(9,0,-1):
      for c in range(9,0,-1):
        for d in range(9,0,-1):
          for e in range(9,0,-1):
            for f in range(9,0,-1):
              for g in range(9,0,-1):
                for h in range(9,0,-1):
                  for i in range(9,0,-1):
                    for j in range(9,0,-1):
                      for k in range(9,0,-1):
                        for l in range(9,0,-1):
                          for m in range(9,0,-1):
                            for n in range(9,0,-1):
                              yield(f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}')


def part2(values):
  pass

def main():
  instructions = getInput()
  part1(instructions)
  # part2(values)

if __name__ == '__main__':
  main()
