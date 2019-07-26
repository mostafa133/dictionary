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

'''**args+ tuple'''
להדפיס את המספרים רק שמופיעים פעם אחת ברשימה
def getuniqueTuple(*args):
    l1= []
    for n in args:
        if args.count(n)==1:
            l1.append(n)

    return tuple(l1)

print(getuniqueTuple(88,88,9,9,6,8))
