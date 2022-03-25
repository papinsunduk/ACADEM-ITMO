def greetings(input, print):
    """Функция приветствия"""
    s = input('What is your name?')
    if len(s) < 1:
        print('Hello, World!')
    elif ord(s[0]) in range(ord('A'), ord('Z')) and (all(ord(j) in range(ord('a'), ord('z')) for j in s[1::]) == 1 and len(s) >= 1):
        print('Hello, %s!' % s)
    else:
        print('Hello, World!')
