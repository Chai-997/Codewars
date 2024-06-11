// Given a string of words, you need to find the highest scoring word.
// Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
// For example, the score of abad is 8(1 + 2 + 1 + 4).
// You need to return the highest scoring word as a string.
// If two words score the same, return the word that appears earliest in the original string.
// All letters will be lowercase and all inputs will be valid.

export const high = (str: string): string => {
  let highest: [number, string] = [0, ""]
  let score: number

  str.split(" ").forEach((word) => {
    score = 0
    for (let i: number = 0; i < word.length; i++) {
      score += word.toLowerCase().charCodeAt(i) - 96
    }

    if (score > highest[0]) {
      highest[0] = score
      highest[1] = word
    }
  })

  return highest[1]
}

console.log(high("a b d c"))