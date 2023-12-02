import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day02.txt')

TO_ELVIS = { 'X': 'A', 'Y': 'B', 'Z': 'C'}

RESULT_SCORE = { 'X': 0, 'Y': 3, 'Z': 6 }
HAND_SCORE = { 'A': 1, 'B': 2, 'C': 3 }
BEST_MOVE = {
  'A': { 'X': 'C', 'Z': 'B' },
  'B': { 'X': 'A', 'Z': 'C' },
  'C': { 'X': 'B', 'Z': 'A' }
}


def brawl_score(elf_hand, santa_hand):
  if elf_hand == santa_hand:
    return 3
  elif elf_hand == 'A':
    return 6 if santa_hand == 'B' else 0
  elif elf_hand == 'B':
    return 6 if santa_hand == 'C' else 0
  elif elf_hand == 'C':
    return 6 if santa_hand == 'A' else 0


def part_one():
  score = 0

  with open(INPUT_FILE) as file:
    for line in file:
      elf_hand, santa_hand = line.split()
      santa_hand = TO_ELVIS[santa_hand]
      score += brawl_score(elf_hand, santa_hand) + HAND_SCORE[santa_hand]

  print(score)


def part_two():
  score = 0

  with open(INPUT_FILE) as file:
    for line in file:
      elf_hand, result = line.split()

      if result == 'Y':
        score += HAND_SCORE[elf_hand] + 3
      else:
        santa_hand = BEST_MOVE[elf_hand][result]
        score += HAND_SCORE[santa_hand] + RESULT_SCORE[result]

  print(score)


if __name__ == '__main__':
  part_one()
  part_two()
