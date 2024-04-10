def encoder(password_input):
    for num in password_input:
        if num < 7:
            num += 3
        else:
            num -= 7
    return password_input
