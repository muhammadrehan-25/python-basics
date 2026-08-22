def process_username(username):
    username= username.strip()
    username=username.lower()
    return username
result=process_username("    REHAN123     ")
print(result)