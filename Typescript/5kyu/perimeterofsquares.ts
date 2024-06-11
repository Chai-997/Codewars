// The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8.
// It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 

// Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed
// in the same manner as in the drawing:

// alternative text

// Hint:
// See Fibonacci sequence

// Ref:
// http://oeis.org/A000045

// The function perimeter has for parameter n where n + 1 is the number of squares(they are numbered from 0 to n)
// and returns the total perimeter of all the squares.

//   perimeter(5)  should return 80
// perimeter(7)  should return 216

/**
 * @param n n+1 number if squares within the rectangle
 * @returns perimeter of all squares contained within the rectangle
 */
export const perimeter = (n: number): number => {
  let perimeter: number = 0
  let fib: number[] = [0, 1];

  for (let i: number = 2; i <= n + 1; i++) {
    fib[i] = fib[i - 2] + fib[i - 1];
    perimeter += fib[i]
  }

  perimeter = (perimeter + 1) * 4

  return perimeter
}

console.log(perimeter(5))