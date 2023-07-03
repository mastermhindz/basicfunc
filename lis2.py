import random

def generate_password():
    characters =string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

passwords = set()
while len(passwords) < 15:
    passwords.add(generate_password())

for password in passwords:
    print(password)