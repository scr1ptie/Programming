from decimal import Decimal, getcontext 
  
getcontext().prec = 3
  
result = Decimal('3') / Decimal('9') 
print(result) 


print(Decimal(str(value1)) / Decimal(str(n)))
print(Decimal(str(value2)) / Decimal(str(n)))
print(Decimal(str(value3)) / Decimal(str(n)))
