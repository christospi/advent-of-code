# frozen_string_literal: true

INPUT_FILE = File.join(__dir__, $PROGRAM_NAME.sub('2023/', 'data/').sub('rb', 'txt'))

def part1
  File.readlines(INPUT_FILE).map do |l|
    nums = l.delete('^0-9')
    "#{nums[0]}#{nums[-1]}".to_i
  end.sum
end

def part2
  w2n = {
    'one' => '1', 'two' => '2', 'three' => '3', 'four' => '4', 'five' => '5',
    'six' => '6', 'seven' => '7', 'eight' => '8', 'nine' => '9'
  }

  File.readlines(INPUT_FILE).map do |l|
    # This f*cked me up a bit; we should not consume matches, so we use a positive
    # lookahead to find matches and a capture group to get the match we want.
    found = l.scan(/(?=(#{w2n.keys.join('|')}|\d))/).flatten.map do |d|
      w2n[d] || d
    end

    "#{found[0]}#{found[-1]}".to_i
  end.sum
end

puts "Part 1: #{part1}"
puts "Part 2: #{part2}"
