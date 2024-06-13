// In this example you have to validate if a user input string is alphanumeric
// The given string is not nil / null / NULL / None, so you don't have to check that.

// The string has the following conditions to be alphanumeric:

// At least one character("" is not valid)
// Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
// No whitespaces / underscore

export function alphanumeric(string: string): boolean {
  let regex: RegExp = new RegExp("^[a-zA-Z0-9]*$")
  return regex.exec(string) && string.length != 0 ? true : false;
}

console.log(alphanumeric("Mazinkaiser345"))