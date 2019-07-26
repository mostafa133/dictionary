def mySum(*args):
   sum = 0
   for items in args :
       sum = sum + items
   return sum
print (mySum(6, 77, -5, 99.7))

**-*-*****-
def printDictionary(**kwargs):
    for k, v in kwargs.items():
        print(f'key: {k} value: {v}')
printDictionary()
printDictionary(name= 'mostafa', age=27, city= 'kawkab')
