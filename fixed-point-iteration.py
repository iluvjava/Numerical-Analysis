InitialsConditions = [3, 5, 7]

def fix_point_itr(results, x0, func, maxItr = 6):
  """
    result: (Array)
      The results of the iteration will be appended to the given array.
    x0: (number)
      The initial condition of the iteration.
    func: (Lambda function)
      A function that represent the fixed point iteration.
    maxItr: (int)
      Positive int, representing the number of maximum iteration.
  """
  if(maxItr == 0):
    return
  results.append(x0)
  fix_point_itr(results, func(x0), func, maxItr - 1)
  return

def main():
  for c in InitialsConditions:
    results = []
    fix_point_itr(results, c, lambda x: (x**2 + c)/(2*x))
    print(results)

if __name__ == "__main__":
  main()