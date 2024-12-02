import * as fs from 'fs';
import * as readline from 'readline';

const filePath = "data/input.txt";

const extractNumbers = (line: string): number[] | null => {
  const numbers: number[] = line.split(/\s+/).map((n) => parseInt(n));
  return numbers.length > 0 ? numbers : null;
}

const isReportSafe = (numbers: number[]): [boolean, number] => {
  let isUnsafe = false;
  let problematicIndex = -1;

  if (numbers) {
    let orderDescending = false;
    let hasProperOrder = false;
    let hasProperDifference = false;
    let difference = 0;

    for (let index = 0; index < numbers.length; index++) {
      if (index === 0) {
        continue;
      } else if (index === 1) {
        // The first two numbers determine the order
        orderDescending = numbers[index] < numbers[index - 1];
      }

      hasProperOrder = orderDescending ? numbers[index] < numbers[index - 1] : numbers[index] > numbers[index - 1];
      difference = Math.abs(numbers[index] - numbers[index - 1]);
      hasProperDifference = difference >= 1 && difference <= 3;

      if (!hasProperOrder || !hasProperDifference) {
        isUnsafe = true;
        problematicIndex = index;
        break;
      }
    }

    return [!isUnsafe, problematicIndex];
  } else {
    return [false, -1];
  }
};

const solvePartOne = async (filePath: string): Promise<number> => {
  let safeReportsCount: number = 0;

  const fileStream = fs.createReadStream(filePath);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  return new Promise((resolve, reject) => {
    rl.on("line", (line: string) => {
      const numbers = extractNumbers(line);

      if (!numbers) {
        return;
      }

      const [isSafe, _] = isReportSafe(numbers);

      if (isSafe) {
        safeReportsCount++;
      }
    });

    rl.on("close", () => {
      resolve(safeReportsCount);
    });

    rl.on("error", (err) => {
      reject(err);
    });
  });
};

const solvePartTwo = async (filePath: string): Promise<number> => {
  let safeReportsCount: number = 0;

  const fileStream = fs.createReadStream(filePath);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  return new Promise((resolve, reject) => {
    rl.on("line", (line: string) => {
      const numbers = extractNumbers(line);

      if (!numbers) {
        return;
      }

      const [isSafe, problematicIndex] = isReportSafe(numbers);

      if (isSafe) {
        safeReportsCount++;
      } else {
        let indicesToRemove: number[] = [];

        indicesToRemove.push(problematicIndex);
        if (problematicIndex > 1) {
          indicesToRemove.push(problematicIndex - 2);
          indicesToRemove.push(problematicIndex - 1);
        }
        if (problematicIndex > 0) {
          indicesToRemove.push(problematicIndex - 1);
        }

        for (const index of indicesToRemove) {
          const newNumbers = numbers.filter((_, i) => i !== index);
          const [isSafe, _] = isReportSafe(newNumbers);

          if (isSafe) {
            safeReportsCount++;
            break;
          }
        }
      }
    });

    rl.on("close", () => {
      resolve(safeReportsCount);
    });

    rl.on("error", (err) => {
      reject(err);
    });
  });
};

solvePartOne(filePath).then((result) => {
  console.log("Safe reports count:", result);
});

solvePartTwo(filePath).then((result) => {
  console.log("Safe reports count after fixing:", result);
});