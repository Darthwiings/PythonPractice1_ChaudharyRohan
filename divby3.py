#given a list of integers, iterate through the list and print numbers that are ONLY divisible by 3
numList = [3,10,33,12,5,8,50,100]
print("Given this list of integers: ", numList)
print("These numbers are divisible by 3: ")
#complete the code below to print numbers only divisible by 3
for x in range(0,len(numList)):
    if numList[x] % 3  == 0:
        print(numList[x])
    
