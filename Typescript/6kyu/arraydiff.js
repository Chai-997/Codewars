"use strict";
// Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
// It should remove all values from list a, which are present in list b keeping their order.
//   array_diff({ 1, 2}, 2, { 1}, 1, * z) == { 2}(z == 1)
// If a value is present in b, all of its occurrences must be removed from the other:
// array_diff({ 1, 2, 2, 2, 3}, 5, { 2}, 1, * z) == { 1, 3}(z == 2)
Object.defineProperty(exports, "__esModule", { value: true });
exports.arrayDiff = void 0;
// submitted
// export function arrayDiff(a: number[], b: number[]): number[] {
//   let c: number[] = a;
//   for (let i = 0; i < a.length; i++) {
//     if (b.indexOf(a[i]) > -1) {
//       c = c.filter((e, x) => e !== a[i]);
//     }
//   }
//   return c;
// }
// console.log(arrayDiff([1, 2, 3], [1, 2]))
// updated
function arrayDiff(a, b) {
    return a.filter(function (n) { return !b.includes(n); });
}
exports.arrayDiff = arrayDiff;
console.log(arrayDiff([1, 2, 3], [1, 2]));
//# sourceMappingURL=arraydiff.js.map