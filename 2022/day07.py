import os
import re
from collections import defaultdict


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'data', 'day07.txt')


def parse_file(line):
  file_regex = re.compile(r'^(\d+)\s(.*)')
  size, filename = file_regex.match(line).groups()
  return int(size), filename


def parse_dir(line, cur_dir):
  dir_regex = re.compile(r'^dir\s(.*)')
  dirname = dir_regex.match(line).group(1)
  if cur_dir == '/':
    return cur_dir + dirname
  else:
    return cur_dir + '/' + dirname


def parse_cd(line, cur_dir):
  command_regex = re.compile(r'^\$\scd\s(.*)')
  dirname = command_regex.match(line).group(1)

  if dirname == '..':
    dirs = cur_dir.split('/')
    if len(dirs) < 3:
      return '/'
    else:
      return '/'.join(cur_dir.split('/')[:-1])
  elif dirname == '/':
    return '/'
  else:
    if cur_dir == '/':
      return cur_dir + dirname
    else:
      return cur_dir + '/' + dirname


def parse_line(line, file_system, cur_dir):
  print(line, file_system, cur_dir)
  if line.startswith('$ cd'):
    dir_path = parse_cd(line, cur_dir)
    # Maybe delete this
    if dir_path not in file_system:
      file_system[dir_path] = 0
    cur_dir = dir_path
  elif line.startswith('$ ls'):
    pass
  elif line.startswith('dir'):
    dir_path = parse_dir(line, cur_dir)
    if dir_path not in file_system:
      file_system[dir_path] = 0
  else:
    size, filename = parse_file(line)
    # file_system[cur_dir + '/' + filename] = size

    file_system[cur_dir] += size
    # Add this size to all previous path directories
    for i in range(1, len(cur_dir.split('/'))):
      print(cur_dir.split('/'))
      print(i)
      dir_to_add = '/'.join(cur_dir.split('/')[:i])
      dir_to_add = dir_to_add if dir_to_add else '/'

      file_system[dir_to_add] += size

  return file_system, cur_dir


def part_one():
  cur_dir = '/'
  file_system = {'/': 0}
  total_size = 0

  with open(INPUT_FILE) as file:
    for line in file:
      print(cur_dir)
      _, cur_dir = parse_line(line, file_system, cur_dir)

  for dir_path, size in file_system.items():
    if size < 100000:
      total_size += size

  print(total_size)



def part_two():
  cur_dir = '/'
  file_system = {'/': 0}
  total_size = 0

  with open(INPUT_FILE) as file:
    for line in file:
      print(cur_dir)
      _, cur_dir = parse_line(line, file_system, cur_dir)

  file_system = sorted(file_system.items(), key=lambda x: x[1], reverse=True)

  needed_space = 30000000 - (70000000 - file_system[0][1])

  # loop file_system with index
  for i in range(len(file_system)):
    dir_path, size = file_system[i]
    if size < needed_space:
      print(file_system[i-1])
      break

if __name__ == '__main__':
  # part_one()
  part_two()
