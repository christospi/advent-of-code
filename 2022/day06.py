import os
from collections import deque

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day06.txt')


def is_anyone_there(signal, freq):
  return len(set(signal)) == freq


def analyze_signal(freq):
  with open(INPUT_FILE) as file:
    for line in file:
      signal = deque(list(line[:freq]))
      if is_anyone_there(signal, freq):
        print(freq)
        break
      else:
        for i in range(freq, len(line[freq:])):
          signal.popleft()
          signal.append(line[i])
          if is_anyone_there(signal, freq):
            print(i + 1)
            break


def part_one():
  analyze_signal(4)


def part_two():
  analyze_signal(14)


if __name__ == '__main__':
  part_one()
  part_two()
