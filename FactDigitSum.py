def fact(num): # Returns the sum of factorial of digits.
  if num > 1:
     factorial = num*fact(num-1)
  elif num == 1 or num == 0:
      return 1
  return factorial

def FactSumDigits(n):
  mylist = []
  y = str(n)
  for i in y:
    mylist.append(i)
  sumup = 0
  for digit in mylist:
    sumup += fact(int(digit))
  return sumup


x = FactSumDigits(21)
print(x)
