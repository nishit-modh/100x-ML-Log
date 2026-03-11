# 13. THE DIAMOND OF EXCLUSION
# Print a diamond pattern of stars.

N = int(input("Enter odd length: "))

if N % 2 == 0:
    print("Please enter an odd number for a perfect diamond.")
else:
    mid = N // 2  # The center index
    
    for i in range(N):
        # 1. Calculate distance from the center row
        # If N=5, mid=2. When i=0, distance is 2. When i=4, distance is 2.
        distance = abs(mid - i)
        
        # 2. Spaces = distance from center
        print(" " * distance, end="")
        
        # 3. Stars = Total width - (2 * distance)
        print("*" * (N - 2 * distance))