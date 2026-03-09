# Take a large integer representing total seconds (e.g., 10000) and convert it into Hours : Minutes : Seconds using floor division and modulo.\
total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
total_seconds %= 3600
minutes = total_seconds // 60
total_seconds %= 60
seconds = total_seconds
print(f"Deconstrcted Time = {hours}:{minutes}:{seconds}")
