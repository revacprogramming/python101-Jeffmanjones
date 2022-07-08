
def add(a, b):
    pass  

def output(a, b, sum):
    pass  

def main():
    a=float(input("Enter a number: ")) 
    b=float(input("Enter a number: "))
    sum=a+b
    add(a, b)
    output(a, b, sum)
    print("The sum of ",a," and ",b," is ",sum)

if __name__ == '__main__':
    main()