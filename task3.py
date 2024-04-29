def check_symmetry(symbols):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    pairs = {')': '(', '}': '{', ']': '['}

    for symbol in symbols:
        if symbol in opening_brackets:
            stack.append(symbol)
        elif symbol in closing_brackets:
            if not stack or stack[-1] != pairs[symbol]:
                return "Несиметрично"
            stack.pop()

    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


if __name__ == "__main__":
    input_str = input("Введіть рядок для перевірки на симетричність: ")
    result = check_symmetry(input_str)
    print(f"{input_str} - {result}")
