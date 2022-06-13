def count_char(password):
    count = 0
    for i in password:
        count +=1

    return count


def check_if_valid_password(password):
    max = 10
    if count_char(password) < max:
        return False
    return True

res = check_if_valid_password("Bonjour")

if res == True:
    print("password is valid")
else:
    print("password is invalid")