"""
2. The Intelligent Game Difficulty Scaler
A game adjusts difficulty based on player_rank (1-100) and win_streak (int).
A "Newbie" rank (below 20) should never face "Hard" difficulty, regardless of streak.
Mid-ranks (20-60) only face "Hard" if their streak is high; otherwise, they stay "Normal."
High ranks (above 60) face "Hard" by default, but if they have a losing streak (negative number), they get dropped to "Normal."
Goal: Print the Difficulty Level.
"""
player_rank = int(input("Enter your rank: "))
win_streak = int(input("Current win straek: "))
if player_rank < 20: 
    difficulty = "Normal"
elif player_rank <= 60:
    difficulty = "Normal"
    if win_streak > 3:
        difficulty = "Hard"
else:
    difficulty = "Hard"
    if win_streak < -3:
        difficulty = "Normal"
print(difficulty)