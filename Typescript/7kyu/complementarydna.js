"use strict";
// Deoxyribonucleic acid(DNA) is a chemical found in the nucleus of cells and carries the "instructions"
// for the development and functioning of living organisms.
Object.defineProperty(exports, "__esModule", { value: true });
exports.Kata = void 0;
var Kata = /** @class */ (function () {
    function Kata() {
    }
    // A <-> T
    // G <-> C
    Kata.dnaStrand = function (dna) {
        var chars = { A: 'T', T: 'A', G: 'C', C: 'G' };
        return dna.replace(/[ATGC]/g, function (c) { return chars[c]; });
    };
    return Kata;
}());
exports.Kata = Kata;
console.log(Kata.dnaStrand("ATTGCCTAC"));
//# sourceMappingURL=complementarydna.js.map