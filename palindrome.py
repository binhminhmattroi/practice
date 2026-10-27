x = 121

result = list(map(int, str(x)))

for i in range(len(result) // 2):
    first_val = result[i]
    last_val = result[-1 - i]  # Negative indexing scans from the right
    
    print(f"Comparing index {i} ({first_val}) with index {len(result)-1-i} ({last_val})")
    
    if first_val == last_val:
        print("-> They match!")
    else:
        print("-> They do not match!")
