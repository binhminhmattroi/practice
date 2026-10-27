x = 121

# store the number in an array
result = []

# Loop until the number becomes 0
while x > 0:
    digit = x % 10      # 1. Get the last digit
    result.append(digit) # 2. Add it to the array
    x = x // 10         # 3. Chop off the last digit

print(result)  # Output: [3, 2, 1, 1, 2, 1]
for i in range(len(result) // 2):
    first_val = result[i]
    last_val = result[-1 - i]  # Negative indexing scans from the right
    
    print(f"Comparing index {i} ({first_val}) with index {len(result)-1-i} ({last_val})")
    
    if first_val == last_val:
        print("-> They match!")
    else:
        print("-> They do not match!")
