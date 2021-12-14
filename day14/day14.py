# #!/bin/env python3

from collections import Counter, defaultdict

def getInput():
  with open("day14.txt") as infile:
    return list(map(lambda line: line.strip(), infile.readlines()))

def getTemplateAndRules(values):
  template = values[0]
  rules = dict()
  for rule in values[2:]:
    key, mapping = rule.split(' -> ')
    rules[key] = mapping
  return (template, rules)


def naiveReplication(template, rules):
  result = ""
  length = len(template)
  for index in range(length - 1):
    key = template[index: index + 2]
    value = rules[key]
    result += template[index] + value
  result += template[length - 1]
  return result

def part1(values):
  template, rules = getTemplateAndRules(values)
  for _ in range(10):
    template = naiveReplication(template, rules)
  counts = Counter(template)
  orderedCounts = counts.most_common()
  print(f'Part 1: {orderedCounts[0][1] - orderedCounts[-1][1]}')

def efficientReplication(template, rules, iterations):
  counts = dict()
  for key in rules.keys():
    counts[key] = Counter(key)

  for _ in range(iterations):
    tempCounts = dict()
    for (firstCharacter, secondCharacter), insertionCharacter in rules.items():
      combinedCounts = counts[firstCharacter + insertionCharacter] + counts[insertionCharacter + secondCharacter]
      # Don't count insertionCharacter twice
      combinedCounts[insertionCharacter] -= 1
      tempCounts[firstCharacter + secondCharacter] = combinedCounts
    counts = tempCounts
  return counts

def part2(values):
  template, rules = getTemplateAndRules(values)
  counts = efficientReplication(template, rules, 40)
  result = Counter()

  for index in range(len(template) - 1):
    key = template[index: index + 2]
    result += counts[key]

  dedup = Counter(template[1:-1])
  result -= dedup

  orderedCounts = result.most_common()
  print(f'Part 2: {orderedCounts[0][1] - orderedCounts[-1][1]}')

def main():
  values = getInput()
  part1(values)
  part2(values)

if __name__ == '__main__':
  main()
