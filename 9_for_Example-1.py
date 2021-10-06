# Create a sequence of numbers from 0 to 5, and print each item in the sequence:
x = range(6)
for n in x:
    print(n)

# Example 2. Create a sequence of numbers from 3 to 5, and print each item in the sequence:

x = range(3, 6)
for n in x:
    print(n)

# Example 3. Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
x = range(3, 20, 2)
for n in x:
    print(n)

# Example 4. Calculate sum for various range()
# (A)
mysum = 0
for i in range(10):
  mysum += i
  print(mysum)

#(B)
mysum = 0
for i in range(7, 10):
    mysum += i
    print(mysum)

# (C)
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        mysum += 1
    print(mysum)

# Example 5. Display Even Numbers from a given list
EvenNumbers=[22,68,98,34,12]
for index in range(len(EvenNumbers)):
  print('Current Number:',EvenNumbers[index])
print('Even Numbers!')
