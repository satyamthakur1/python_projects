import secrets
import string

def generate_unique_password(length=20):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    # Custom subset of symbols to avoid characters that may look too similar
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?"

    # Combine into one full character set
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure the password contains at least one from each pool for complexity.
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill the remaining positions using cryptographically secure 32-bit random numbers.
    # The use of randbits gives us additional bit-level randomness for indexing.
    for i in range(length - 4):
        rand_num = secrets.randbits(32)
        idx = rand_num % len(all_chars)
        password_chars.append(all_chars[idx])

    # --- Unique twist begins here ---
    # Split the list into two halves.
    half = len(password_chars) // 2
    first_half = password_chars[:half]
    second_half = password_chars[half:]

    # Reverse the first half to introduce nonlinearity.
    first_half.reverse()

    # Interleave the two halves, so that the overall structure is less predictable.
    interleaved = []
    # Zip may leave out an extra character if the halves are unequal, so handle that.
    for a, b in zip(first_half, second_half):
        interleaved.append(a)
        interleaved.append(b)
    if len(first_half) != len(second_half):
        interleaved.append(first_half[-1] if len(first_half) > len(second_half) else second_half[-1])
    # --- Unique twist ends here ---

    # Finally, perform a secure shuffle on the interleaved list.
    for i in range(len(interleaved) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        interleaved[i], interleaved[j] = interleaved[j], interleaved[i]

    return ''.join(interleaved)

if __name__ == "__main__":
    password = generate_unique_password(20)
    print("Unique Secure Password:", password)
