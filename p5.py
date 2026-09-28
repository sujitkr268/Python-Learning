number = [12,5,8,20,3,15]
largest=number[0]
smallest=number[0]
total=0
even=0
greater=[]
for num in number:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total=total+num
    if num % 2==0:
        even=even+num
    if num >10:
        greater.append(num)


avg=total/len(number)
print("largest:",largest)
print("smallest:",smallest)
print("Sum:",total)
print("Average:",avg)
print("Even:",even)
print("greater than 10:",greater)
