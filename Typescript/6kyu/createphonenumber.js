"use strict";
// Write a function that accepts an array of 10 integers(between 0 and 9),
// that returns a string of those numbers in the form of a phone number.
Object.defineProperty(exports, "__esModule", { value: true });
exports.createPhoneNumber = void 0;
//   Example
// createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
// The returned format must be correct in order to complete this challenge.
//   Don't forget the space after the closing parentheses!
function createPhoneNumber(n) {
    return "(".concat(n[0]).concat(n[1]).concat(n[2], ") ").concat(n[3]).concat(n[4]).concat(n[5], "-").concat(n[6]).concat(n[7]).concat(n[8]).concat(n[9]);
}
exports.createPhoneNumber = createPhoneNumber;
console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));
//# sourceMappingURL=createphonenumber.js.map