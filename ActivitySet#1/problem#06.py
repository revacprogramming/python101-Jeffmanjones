# Loops & Iterators

largest = None
smallest = None

while True:
    num = input("Enter a number? ")
    try if num == "done":
        break
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
except print(num)

print("Maximum", largest)
print("Minimum", smallest)