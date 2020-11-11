def isMatch(text, pattern):
    start = 0
    textLen = len(text)
    patternLen = len(pattern)
    for index, char in enumerate(pattern):
        if char == "?":
            start += 1
        elif char == "*":
            while (textLen-start) > (patternLen-(index+1)):
                start += 1
        elif char != text[start]:
            return False
        else:
            start += 1
    return True


print("  ? denotes one char matching while * denotes sequence of chars matching!")
text = input("Enter the text: ")
pattern = input("Enter pattern to search for text: ")
print(isMatch(text, pattern))
