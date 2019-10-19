"""
A demonstration for Horner's method, using it to compute 
nth degree polynomial efficiently.
"""

def poly_eval(x: float, coefficients: list, recur_depth = 0)-> float:
  """
    compute: a_0 + a_1*x + a_2*x ... + a_n*x^n in a efficient manner.
    x: (number)
      The value to of the x in the polynomial. 
    coefficients: (list)
      A list of numbers representing the coefficients of the polynomial 
      in ascending order. 
    recur_depth: 
      For function to keep track of the recursion.
  """
  if recur_depth >= len(coefficients):
    return 0
  a = coefficients[recur_depth]
  return a + x*(poly_eval(x, coefficients, recur_depth + 1))


def main():
  print(poly_eval(2, [1, 1, 1, 1]))

if __name__ == "__main__":
  main()