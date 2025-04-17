import secrets
import string

def generate_unique_password(length=20):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?"

    # Combine into one full character set
    all_chars = lowercase + uppercase + digits + symbols

    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # The use of randbits gives us additional bit-level randomness for indexing.
    for i in range(length - 4):
        rand_num = secrets.randbits(32)
        idx = rand_num % len(all_chars)
        password_chars.append(all_chars[idx])

    # Split the list into two halves.
    half = len(password_chars) // 2
    first_half = password_chars[:half]
    second_half = password_chars[half:]

    first_half.reverse()

    interleaved = []
    # Zip may leave out an extra character if the halves are unequal, so handle that.
    for a, b in zip(first_half, second_half):
        interleaved.append(a)
        interleaved.append(b)
    if len(first_half) != len(second_half):
        interleaved.append(first_half[-1] if len(first_half) > len(second_half) else second_half[-1])

    for i in range(len(interleaved) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        interleaved[i], interleaved[j] = interleaved[j], interleaved[i]

    return ''.join(interleaved)

if __name__ == "__main__":
    password = generate_unique_password(20)
    print("Unique Secure Password:", password)
