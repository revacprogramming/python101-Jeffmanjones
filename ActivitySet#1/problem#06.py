largest= -1
smallest= 10000
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
print("Maximum", largest)
print("Minimum", smallest)