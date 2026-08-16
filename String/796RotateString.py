def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    double_s = s + s

    return goal in double_s


s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))
