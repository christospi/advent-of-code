import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day03.txt')


def item_score(item):
  if item.islower():
    return ord(item) - ord('a') + 1
  else:
    return ord(item) - ord('A') + 27


def part_one():
  psum = 0
  with open(INPUT_FILE) as file:
    for line in file:
      s1 = line[:len(line)//2]
      s2 = line[len(line)//2:]
      common = list(set(s1) & set(s2))
      for c in common:
        psum += item_score(c)
  print(psum)


def part_two():
  psum = 0
  with open(INPUT_FILE) as file:
    for l1, l2, l3 in zip(file, file, file):
      common = list(set(l1.strip()) & set(l2.strip()) & set(l3.strip()))
      for c in common:
        psum += item_score(c)
  print(psum)


if __name__ == '__main__':
  part_one()
  part_two()
