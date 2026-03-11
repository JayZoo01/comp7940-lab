# Write a function that prints all factors of the given parameter x
def print_factor(x):
    # your code here
    for i in range(1,x+1):
        if x % i == 0:
            print(i)

if __name__ == "__main__":
    print_factor(100)
