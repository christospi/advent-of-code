import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day01.txt')

def part_one():
  maxi = 0
  curr = 0

  with open(INPUT_FILE) as file:
    for line in file:
      curr = curr + int(line) if line.strip() else 0
      if curr > maxi:
        maxi = curr

  print(maxi)

def part_two():
  curr = 0
  per_elf = []

  with open(INPUT_FILE) as file:
    for line in file:
      if line.strip():
        curr += int(line)
      else:
        per_elf.append(curr)
        curr = 0

  print(sum(sorted(per_elf, reverse=True)[:3]))

if __name__ == '__main__':
  part_one()
  part_two()
