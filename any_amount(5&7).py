def change(amount):
 if(amount == 0):
  return([])
 elif (amount %  5 == 0):
  return([5] + change(amount - 5))
 elif(amount % 7 == 0):
  return([7] + change(amount - 7))
 else:
  return([5]+change(amount-5))

