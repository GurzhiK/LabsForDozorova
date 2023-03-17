n = input("Введите число:")
max_digit = max(n) 
result = n.replace(max_digit, max_digit*2)
print(result)