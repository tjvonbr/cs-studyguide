def isValid(s: str) -> bool:
    mapping = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    openings = ["(", "{", "["]
    stack = []

    for char in s:
        if char in openings:
            stack.append(char)
        elif stack and char == mapping[stack[-1]]:
            stack.pop()
        else:
            return False

    if len(stack) == 0: return True

print(isValid("({[]]})"))