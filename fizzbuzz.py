def fizzbuzz(num):
   if num % 2 == 0 and num % 5 == 0 :
      return "fizzbuzz"
   elif num % 2 == 0:
      return "fizz"
   elif num % 5==0:
      return "buzz" 
   else :
      return num 
   
print(fizzbuzz(100))   
