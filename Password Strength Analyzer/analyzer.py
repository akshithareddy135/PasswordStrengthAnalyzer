import string
import math


# -------------------------------
# Character Checks
# -------------------------------

def has_uppercase(password):
    return any(char.isupper() for char in password)


def has_lowercase(password):
    return any(char.islower() for char in password)


def has_number(password):
    return any(char.isdigit() for char in password)


def has_special(password):
    return any(char in string.punctuation for char in password)


# -------------------------------
# Common Password Detection
# -------------------------------

def load_common_passwords():
    try:
        with open("common_passwords.txt", "r", encoding="utf-8") as file:
            return {line.strip().lower() for line in file}
    except FileNotFoundError:
        return set()


def is_common_password(password, common_passwords):
    return password.lower() in common_passwords


# -------------------------------
# Repeated Character Detection
# -------------------------------

def has_repeated_characters(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False


# -------------------------------
# Sequential Pattern Detection
# -------------------------------

def has_sequential_pattern(password):
    sequences = [
        "1234567890",
        "abcdefghijklmnopqrstuvwxyz",
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    ]

    password = password.lower()

    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i + 3] in password:
                return True

    return False


# -------------------------------
# Character Diversity
# -------------------------------

def character_diversity(password):
    diversity = 0

    if has_uppercase(password):
        diversity += 1

    if has_lowercase(password):
        diversity += 1

    if has_number(password):
        diversity += 1

    if has_special(password):
        diversity += 1

    return diversity


# -------------------------------
# Entropy Calculation
# -------------------------------

def calculate_entropy(password):

    charset_size = 0

    if has_lowercase(password):
        charset_size += 26

    if has_uppercase(password):
        charset_size += 26

    if has_number(password):
        charset_size += 10

    if has_special(password):
        charset_size += 32

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)

    return round(entropy, 2)


# -------------------------------
# Crack Time Estimation
# -------------------------------

def estimate_crack_time(entropy):

    guesses_per_second = 1_000_000_000

    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} seconds"

    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"

    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"

    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"

    else:
        return f"{seconds/31536000:.2f} years"


# -------------------------------
# Score Calculation
# -------------------------------

def calculate_score(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if has_uppercase(password):
        score += 1

    if has_lowercase(password):
        score += 1

    if has_number(password):
        score += 1

    if has_special(password):
        score += 1

    if character_diversity(password) == 4:
        score += 1

    if has_repeated_characters(password):
        score -= 1

    if has_sequential_pattern(password):
        score -= 1

    return max(score, 0)


# -------------------------------
# Strength Rating
# -------------------------------

def get_strength(score):

    if score <= 2:
        return "Weak"

    elif score <= 5:
        return "Medium"

    return "Strong"


# -------------------------------
# Recommendations
# -------------------------------

def get_recommendations(password):

    recommendations= []

    if len(password) < 12:
        recommendations.append(
            "Increase password length to at least 12 characters."
        )

    if not has_uppercase(password):
        recommendations.append(
            "Add uppercase letters."
        )

    if not has_lowercase(password):
        recommendations.append(
            "Add lowercase letters."
        )

    if not has_number(password):
        recommendations.append(
            "Add numbers."
        )

    if not has_special(password):
        recommendations.append(
            "Add special characters."
        )

    if has_repeated_characters(password):
        recommendations.append(
            "Avoid repeated characters."
        )

    if has_sequential_pattern(password):
        recommendations.append(
            "Avoid sequential patterns like 123 or abc."
        )

    return recommendations