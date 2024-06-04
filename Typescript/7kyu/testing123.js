"use strict";
// Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Object.defineProperty(exports, "__esModule", { value: true });
exports.number = void 0;
// Write a function which takes a list of strings and returns each line prepended by the correct number.
// The numbering starts at 1. The format is n: string.Notice the colon and space in between.
//   Examples: (Input-- > Output)
//   []-- > []
//   ["a", "b", "c"]-- > ["1: a", "2: b", "3: c"]
function number(array) {
    return array.map(function (n, i) { return "".concat(i + 1, ": ").concat(n); });
}
exports.number = number;
console.log(number(["a", "b", "c"]));
//# sourceMappingURL=testing123.js.map