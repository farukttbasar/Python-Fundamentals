
while True:
    sequence = input("Enter DNA sequence (A, T, G, C): ").upper().strip()
    
    is_valid = True
    if not sequence: 
        is_valid = False
    else:
        for char in sequence:
            if char not in ["A", "T", "G", "C"]:
                is_valid = False
                break
    
    if is_valid:
        break
    else:
        print("Invalid input! Please enter ONLY A, T, G, and C. (No numbers or other letters).")


while True:
    base_to_count = input("Which nucleobase to count? (A, T, G, C): ").upper().strip()
    
    if base_to_count in ["A", "T", "G", "C"]:
        break
    else:
        print("Invalid input! Please choose one: A, T, G, or C.")


counter = 0
for base in sequence:
    if base == base_to_count:
        counter += 1 

print("-" * 30)
print(f"Analysis Results for: {sequence}")
print(f"The nucleobase '{base_to_count}' appears {counter} times in the sequence.")
print("-" * 30)
    


