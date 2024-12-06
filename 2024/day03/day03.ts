import * as fs from "fs";
import * as readline from "readline";

const filePath = "data/input.txt";

const parseLine = (line: string): number => {
  let lineMulSum = 0;
  const regex = /mul\((\d{1,3}\,\d{1,3})\)/g;

  for (const match of line.matchAll(regex)) {
    if (match[1]) {
      lineMulSum += match[1]
        .split(",")
        .reduce((acc, curr) => acc * parseInt(curr), 1);
    }
  }

  return lineMulSum;
};

const parseLineWithEnablers = (line: string, enabledStatus: boolean): [number, boolean] => {
  let lineMulSum = 0;
  let enabled = enabledStatus;

  const sickRegex = /(do\(\))|mul\((\d{1,3}\,\d{1,3})\)|(don't\(\))/g;

  for (const match of line.matchAll(sickRegex)) {
    if (match[1]) {
      enabled = true;
    } else if (match[3]) {
      enabled = false;
    } else if (match[2] && enabled) {
      lineMulSum += match[2]
        .split(",")
        .reduce((acc, curr) => acc * parseInt(curr), 1);
    }
  }

  return [lineMulSum, enabled];
};

const solvePart = (filePath: string, part: number): number => {
  let totalMulSum = 0;
  let enabledStatus = true;

  const fileStream = fs.createReadStream(filePath);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  rl.on("line", (line: string) => {
    if (part === 1) {
      totalMulSum += parseLine(line);
    } else if (part === 2) {
      const [lineMulSum, enabled] = parseLineWithEnablers(line, enabledStatus);
      totalMulSum += lineMulSum;
      enabledStatus = enabled;
    }
  });

  rl.on("close", () => {
    console.log(totalMulSum);
  });

  return totalMulSum;
};

solvePart(filePath, 1);
solvePart(filePath, 2);
