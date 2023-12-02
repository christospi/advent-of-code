import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day05.txt')

# Initial setup is:
#
# [G]                 [D] [R]
# [W]         [V]     [C] [T] [M]
# [L]         [P] [Z] [Q] [F] [V]
# [J]         [S] [D] [J] [M] [T] [V]
# [B]     [M] [H] [L] [Z] [J] [B] [S]
# [R] [C] [T] [C] [T] [R] [D] [R] [D]
# [T] [W] [Z] [T] [P] [B] [B] [H] [P]
# [D] [S] [R] [D] [G] [F] [S] [L] [Q]
#  1   2   3   4   5   6   7   8   9
def initial_setup() -> list:
  l1 = ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G']
  l2 = ['S', 'w', 'C']
  l3 = ['R', 'Z', 'T', 'M']
  l4 = ['D', 'T', 'C', 'H', 'S', 'P', 'V']
  l5 = ['G', 'P', 'T', 'L', 'D', 'Z']
  l6 = ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D']
  l7 = ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R']
  l8 = ['L', 'H', 'R', 'B', 'T', 'V', 'M']
  l9 = ['Q', 'P', 'D', 'S', 'V']
  return [l1, l2, l3, l4, l5, l6, l7, l8, l9]


def parse_move(line) -> tuple:
  # Also kinda lazy, sorry not sorry
  data = line.split()
  # how_many_to_move, from, to
  return int(data[1]), int(data[3])-1, int(data[5])-1


def crate_mover(model, crates, line):
  count, source, dest = parse_move(line)
  if model == '9000':
    for _ in range(count):
      crates[dest].append(crates[source].pop())
  elif model == '9001':
    where_to_put_that = len(crates[dest])
    for _ in range(count):
      crates[dest].insert(where_to_put_that, crates[source].pop())
  else:
    raise ValueError('Model is still in development...')


def anathesi_se_ergolavo(model):
  crates = initial_setup()

  with open(INPUT_FILE) as file:
    # Ain't nobody got time for parsing this
    for _ in range(10):
      next(file)
    for line in file:
      crate_mover(model, crates, line)

  print(''.join([c.pop() for c in crates]))


def part_one():
  anathesi_se_ergolavo('9000')


def part_two():
  anathesi_se_ergolavo('9001')


if __name__ == '__main__':
  part_one()
  part_two()
