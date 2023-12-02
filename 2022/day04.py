import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day04.txt')


def overlaps(e1, e2, fully = True):
  if fully:
    return e1[0] >= e2[0] and e1[1] <= e2[1]
  else:
    return e1[0] <= e2[0] <= e1[1] or e1[0] <= e2[1] <= e1[1]


def ktimatologio(fully = True):
  psum = 0
  with open(INPUT_FILE) as file:
    for line in file:
      elf_1, elf_2 = [s.split('-') for s in line.split(',')]
      elf_1 = [int(x) for x in elf_1]
      elf_2 = [int(x) for x in elf_2]
      if overlaps(elf_1, elf_2, fully) or overlaps(elf_2, elf_1, fully):
        psum += 1
  print(psum)


def part_one():
  ktimatologio(fully = True)


def part_two():
  ktimatologio(fully = False)


if __name__ == '__main__':
  part_one()
  part_two()
