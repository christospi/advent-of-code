import os
import re

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day08.txt')


def create_forest(pad: bool = True):
  forest = []
  with open(INPUT_FILE) as file:
    for line in file:
      trees = [int(num) for num in re.split('', line)[1:-2]]
      trees = [-1] + trees + [-1] if pad else trees
      if len(forest) == 0 and pad:
        forest.append([-1] * len(trees))

      forest.append(trees)
  forest.append([-1] * len(forest[0])) if pad else None

  return forest


def compare_neighbors(forest, tree, cur, l1, l2):
  all_shorter = True
  for k in range(l1, l2):
    if forest[k][cur] >= tree:
      all_shorter = False

  return all_shorter


def part_one():
  forest = create_forest()
  visible = 0

  for i in range(1, len(forest) - 1):
    for j in range(1, len(forest[i]) - 1):
      tree = forest[i][j]

      # if compare_neighbors(forest, tree, j, 0, i) or \
      #    compare_neighbors(forest, tree, j, i - 1, i) or \
      #    compare_neighbors(forest, tree, i, j, j + 1) or \
      #    compare_neighbors(forest, tree, i, j - 1, j):
      #   visible += 1
      #   continue

      # check up
      all_shorter = True
      for k in range(i):
        other_tree = forest[k][j]
        if other_tree >= tree:
          all_shorter = False
      if all_shorter:
        visible += 1
        continue
      else:
        all_shorter = True
      # check down
      for k in range(i + 1, len(forest)):
        other_tree = forest[k][j]
        if other_tree >= tree:
          all_shorter = False
      if all_shorter:
        visible += 1
        continue
      else:
        all_shorter = True
      # check left
      for k in range(j):
        other_tree = forest[i][k]
        if other_tree >= tree:
          all_shorter = False
      if all_shorter:
        visible += 1
        continue
      else:
        all_shorter = True
      # check right
      for k in range(j + 1, len(forest[i])):
        other_tree = forest[i][k]
        if other_tree >= tree:
          all_shorter = False
      if all_shorter:
        visible += 1
        continue
      else:
        all_shorter = True

  print(visible)


def part_two():
  forest = create_forest(pad=False)
  best_view = 0
  cur_view = []

  for i in range(len(forest)):
    for j in range(len(forest[i])):
      tree = forest[i][j]
      cur_view = [0] * 4

      # check up
      for k in range(i):
        other_tree = forest[k][j]
        cur_view[0] += 1
        if other_tree >= tree:
          break
      # check down
      for k in range(i + 1, len(forest)):
        other_tree = forest[k][j]
        cur_view[1] += 1
        if other_tree >= tree:
          break
      # check left
      for k in range(j):
        other_tree = forest[i][k]
        cur_view[2] += 1
        if other_tree >= tree:
          break
      # check right
      for k in range(j + 1, len(forest[i])):
        other_tree = forest[i][k]
        cur_view[3] += 1
        if other_tree >= tree:
          break
      #multiply the number of trees in each direction
      tree_view = cur_view[0] * cur_view[1] * cur_view[2] * cur_view[3]
      if tree_view > best_view:
        best_view = tree_view

  print(best_view)


if __name__ == '__main__':
  # part_one()
  part_two()
