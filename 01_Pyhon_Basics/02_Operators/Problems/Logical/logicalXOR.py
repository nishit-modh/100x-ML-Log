# Take two boolean inputs (e.g., is_raining, has_umbrella). Print True only if one is true and the other is false (but not both!).
rain = input("Is it raining?(T/F): ")
umbrella = input("Do you have umbrella?(T/F): ")
is_raining = rain == "T"
has_umbrella = umbrella == "T"
print(
    "Are you an Idiot?: ",
    ((is_raining or has_umbrella) and not (is_raining and has_umbrella)),
)
"""
Logical equation for XOR:
(A or B) and not (A and B)
"""
