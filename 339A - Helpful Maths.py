numbers = input().split("+")
numbers.sort()
result = "".join(f"{num}+" for num in numbers)
print(result[:-1])