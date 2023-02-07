n=int(input("Enter the number of terms to be printed:")) 
a=sum=0
b=count=1
print("Fibonacci Series: "," ")
while(count <= n):
  print(sum," ")
  count += 1
  a = b
  b = sum
  sum = a + b
