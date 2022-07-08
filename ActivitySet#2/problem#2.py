
def add(a, b):
    sum=a+b
    return sum
    pass  

def output(a, b, sum):
    print("The sume of ",a," and ",b," is ",sum)
    pass  

def main():
    a=float(input("Enter a number: ")) 
    b=float(input("Enter a number: "))
    sum = add(a, b)
    output(a, b, sum)

if __name__ == '__main__':
    main()