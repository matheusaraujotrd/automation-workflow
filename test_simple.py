user = password = None

with open("credential.txt", encoding="utf-8") as f:
    for line in f:
        if line.startswith("user:"):
            user = line[5:].strip()
        elif line.startswith("pass:"):
            password = line[5:].strip()

if user is None or password is None:
    raise ValueError("Missing credentials")

print(user, password)