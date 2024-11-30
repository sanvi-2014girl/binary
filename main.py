def longest_consecutive_ones(n):
    max_count = 0
    current_count = 0
    while n > 0:
        if n % 2 == 1:
            current_count += 1
            max_count = max(max_count,current_count)
        else:
            current_count = 0
        n = n // 2
    return max_count
num = int(input("Enter a number: "))
result = longest_consecutive_ones(num)
print(f"The longest consecutive 1's in the binary reprenstation of {num} is {result}")