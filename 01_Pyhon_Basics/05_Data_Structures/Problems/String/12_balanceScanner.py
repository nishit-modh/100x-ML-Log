# 12. THE BALANCED SCANNER
# Problem: Check if the parentheses in a string are balanced.
# Every opening "(" must have a closing ")".
# Input: "(a + b) * (c - d)" -> True
# Input: "((a + b)" -> False

p_string = input("Parentheses string: ")
balance = True

#=================================
# First attempt --> Failed
#=================================
# INTENT: Quick check if numbers match.
# REALITY: Good start, but ")( " would pass this check.
if p_string.count("(") != p_string.count(")"):
    balance = False
else:
    inner_balance = True
    for i, char in enumerate(p_string):
        if char == "(":
            # INTENT: Assume this '(' is unbalanced until we find its pair.
            inner_balance = False 
            
            # INTENT: Scan the rest of the string for a closing ')'
            # PROBLEM: This finds ANY ')' even if that ')' was already used 
            # by a different '(' earlier!
            for j in p_string[i + 1 :]: 
                if j == ")":
                    inner_balance = True
                    # If we find one, we say we are balanced.
                    # But we don't 'consume' the bracket.

    balance = inner_balance 

print(balance)

#======================================
# climber - original idea was this but didn't code it
#======================================
p_string = input("Parentheses string: ")
is_balanced = True
count = 0

for char in p_string:
    if char == "(":
        count += 1
    if char == ")":
        count -= 1
    if count < 0:
        is_balanced = False
        break
if count != 0 :
    is_balanced = False
print(f"Parentheses for {p_string} are Balanced: {is_balanced}")