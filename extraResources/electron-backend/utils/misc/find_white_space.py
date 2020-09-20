def find_white_space(number, text):
    count = 0
    for index in range(len(text)):
        if count == number:
            return index - 1
        if text[index] == ' ':
            count = count + 1
    return len(text)
