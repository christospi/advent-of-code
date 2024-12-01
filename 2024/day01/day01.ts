import * as fs from "fs";
import * as readline from "readline";

const filePath = "data/input.txt";

const extractNumbers = (line: string): [number, number] | null => {
  const numbers = line.split(/\s+/).map((n) => parseInt(n));
  return numbers.length === 2 ? [numbers[0], numbers[1]] : null;
};

const processInput = async (filePath: string): Promise<number[][]> => {
  const locationIds1: number[] = [];
  const locationIds2: number[] = [];

  const fileStream = fs.createReadStream(filePath);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  return new Promise((resolve, reject) => {
    rl.on("line", (line: string) => {
      const numbers = extractNumbers(line);
      if (numbers) {
        locationIds1.push(numbers[0]);
        locationIds2.push(numbers[1]);
      }
    });

    rl.on("close", () => {
      resolve([locationIds1, locationIds2]);
    });

    rl.on("error", (err) => {
      reject(err);
    });
  });
};

const solvePartOne = async () => {
  try {
    const [locationIds1, locationIds2] = await processInput(filePath);

    locationIds1.sort((a, b) => a - b);
    locationIds2.sort((a, b) => a - b);

    const totalDiffSum = locationIds1.reduce((acc, locId, index) => {
      if (index < locationIds2.length) {
        return acc + (Math.abs(locId - locationIds2[index]));
      }

      return acc; // Skip extra elements if arrays differ in length
    }, 0);

    console.log("Total sum:", totalDiffSum);
  } catch (err) {
    console.error(err);
  }
};

const solvePartTwo = async () => {
  try {
    const [locationIds1, locationIds2] = await processInput(filePath);

    const locationIdsCounter = new Map<number, number>();

    locationIds2.forEach((locId) => {
      locationIdsCounter.set(locId, (locationIdsCounter.get(locId) || 0) + 1);
    });

    const similarityScore = locationIds1.reduce((acc, locId) => {
      const occurences = locationIdsCounter.get(locId) || 0;

      return acc + (occurences * locId)
    }, 0);

    console.log("Similarity Score:", similarityScore);
  } catch (err) {
    console.error(err);
  }
};

solvePartOne();
solvePartTwo();
