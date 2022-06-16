largest= None
smallest= None
while True:
    num = input("Enter a number? ")
    try:
        if num == "done":
            break
        else:
            num=int(num)
        if num>largest:
            largest=num
        if num<smallest:
            smallest=num
    except:
        print("invalid input")
print(largest)
print("The smallest number is ",smallest)