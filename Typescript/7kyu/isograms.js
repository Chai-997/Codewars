"use strict";
// An isogram is a word that has no repeating letters, consecutive or non - consecutive.
// Implement a function that determines whether a string that contains only letters is an isogram.
// Assume the empty string is an isogram.Ignore letter case.
Object.defineProperty(exports, "__esModule", { value: true });
exports.isIsogram = void 0;
// Example: (Input-- > Output)
// "Dermatoglyphics" -- > true
// "aba" -- > false
// "moOse" -- > false(ignore letter case)
// submitted
// export function isIsogram(str: string): boolean {
//   str = str.toLowerCase();
//   let temp: string = str;
//   let ans: boolean = true;
//   for (let i: number = 0; i < str.length; i++) {
//     temp = temp.slice(1);
//     if (temp.includes(str[i])) {
//       ans = false;
//     }
//   }
//   return ans;
// }
// update
function isIsogram(str) {
    return (new Set(str.toLowerCase())).size === str.length;
}
exports.isIsogram = isIsogram;
console.log(isIsogram("Dermatoglyphics"));
//# sourceMappingURL=isograms.js.map