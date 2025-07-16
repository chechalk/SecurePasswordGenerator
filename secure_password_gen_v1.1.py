import random
import string
import secrets
import math
import os
import sys

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

AMBIGUOUS_CHARS = {'O', '0', 'I', 'l', '1'}

def get_char_sets(include_upper=True, include_lower=True, include_digits=True, include_symbols=True, exclude_ambiguous=False):
    sets = []
    if include_upper:
        sets.append(set(string.ascii_uppercase))
    if include_lower:
        sets.append(set(string.ascii_lowercase))
    if include_digits:
        sets.append(set(string.digits))
    if include_symbols:
        sets.append(set("!@#$%^&*()-_=+[]{};:,.<>?"))

    if exclude_ambiguous:
        sets = [s - AMBIGUOUS_CHARS for s in sets]

    return sets

def generate_password(length=16, include_upper=True, include_lower=True, include_digits=True, include_symbols=True, exclude_ambiguous=False):
    char_sets = get_char_sets(include_upper, include_lower, include_digits, include_symbols, exclude_ambiguous)

    if not char_sets:
        raise ValueError("At least one character type must be selected.")

    all_chars = set().union(*char_sets)
    if not all_chars:
        raise ValueError("Character sets are empty after exclusions.")

    password_chars = [secrets.choice(list(s)) for s in char_sets]

    while len(password_chars) < length:
        password_chars.append(secrets.choice(list(all_chars)))

    random.shuffle(password_chars)

    return "".join(password_chars)

def entropy(password):
    # Estimate entropy: log2(possible_char_set_size ^ length)
    char_sets = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        "!@#$%^&*()-_=+[]{};:,.<>?"
    ]
    pool_size = 0
    for s in char_sets:
        if any(c in s for c in password):
            pool_size += len(s)
    if pool_size == 0:
        pool_size = 1
    return round(math.log2(pool_size) * len(password), 2)

def password_strength(password):
    length = len(password)
    categories = 0
    if any(c.islower() for c in password):
        categories += 1
    if any(c.isupper() for c in password):
        categories += 1
    if any(c.isdigit() for c in password):
        categories += 1
    if any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in password):
        categories += 1

    ent = entropy(password)

    if length >= 12 and categories >= 3 and ent >= 60:
        return "Strong"
    elif length >= 8 and categories >= 2 and ent >= 40:
        return "Moderate"
    else:
        return "Weak"

def save_history(passwords, filename="password_history.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        for pwd in passwords:
            f.write(pwd + "\n")

def main():
    print("=== Secure Password Generator v2 ===")
    try:
        length = int(input("Password length (recommended >=12): ") or "16")
    except ValueError:
        print("Invalid length, defaulting to 16.")
        length = 16

    include_upper = input("Include UPPERCASE? (Y/n): ").strip().lower() != 'n'
    include_lower = input("Include lowercase? (Y/n): ").strip().lower() != 'n'
    include_digits = input("Include digits? (Y/n): ").strip().lower() != 'n'
    include_symbols = input("Include symbols? (Y/n): ").strip().lower() != 'n'
    exclude_ambiguous = input("Exclude ambiguous chars like 'O', '0', 'I', 'l'? (y/N): ").strip().lower() == 'y'

    try:
        count = int(input("How many passwords to generate? (default 1): ") or "1")
    except ValueError:
        count = 1

    passwords = []
    for _ in range(count):
        try:
            pwd = generate_password(length, include_upper, include_lower, include_digits, include_symbols, exclude_ambiguous)
            passwords.append(pwd)
        except ValueError as e:
            print(f"Error: {e}")
            return

    for i, pwd in enumerate(passwords, 1):
        strength = password_strength(pwd)
        ent = entropy(pwd)
        print(f"\nPassword {i}: {pwd}")
        print(f" Strength: {strength} | Entropy: {ent} bits")

    save_choice = input("\nSave these passwords to a file? (y/N): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter filename (default password_history.txt): ").strip() or "password_history.txt"
        save_history(passwords, filename)
        print(f"Saved to {filename}")

    if CLIPBOARD_AVAILABLE and count == 1:
        copy_choice = input("Copy the password to clipboard? (Y/n): ").strip().lower()
        if copy_choice != 'n':
            pyperclip.copy(passwords[0])
            print("Password copied to clipboard!")

if __name__ == "__main__":
    main()
