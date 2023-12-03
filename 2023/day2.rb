# frozen_string_literal: true

INPUT_FILE = File.join(__dir__, $PROGRAM_NAME.sub('2023/', 'data/').sub('rb', 'txt'))

def part1
  rules = { 'red' => 12, 'green' => 13, 'blue' => 14 }

  File.readlines(INPUT_FILE).map do |l|
    id, data = l.split(':')
    id = id.match(/Game (\d+)/)[1].to_i

    sets = data.split(';')
    valid = true

    sets.map do |set|
      red, green, blue = set.scan(/(\d+) red|(\d+) green|(\d+) blue/).transpose.map do |g|
        g.map.compact.first.to_i
      end

      if red > rules['red'] || green > rules['green'] || blue > rules['blue']
        valid = false
        break
      end
    end

    valid ? id : nil
  end.compact.sum
end

def part2
  File.readlines(INPUT_FILE).map do |l|
    data = l.split(':').last
    sets = data.split(';')

    colors_per_set = sets.map do |set|
      # For each set, it returns an array of [red, green, blue] values.
      set.scan(/(\d+) red|(\d+) green|(\d+) blue/).transpose.map do |g|
        g.map.compact.first.to_i
      end
    end

    # Group same colors together and pick the max value (i.e., the min required to be possible).
    colors_per_set.transpose.map(&:max).reduce(:*)
  end.sum
end

puts "Part 1: #{part1}"
puts "Part 2: #{part2}"
