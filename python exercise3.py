# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
for i in range(len(l)):
    for j in range(1,l[i]+1):
        if l[i]%j==0:
            print(j)

# your code here
