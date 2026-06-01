from analyzer import *

def main():

    print("=" * 50)
    print("PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    password = input("\nEnter Password: ")

    common_passwords = load_common_passwords()

    score = calculate_score(password)
    strength = get_strength(score)

    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    recommendations = get_recommendations(password)

    print("\n" + "=" * 50)
    print("PASSWORD ANALYSIS REPORT")
    print("=" * 50)

    print(f"Length                : {len(password)}")
    print(f"Uppercase Letters     : {has_uppercase(password)}")
    print(f"Lowercase Letters     : {has_lowercase(password)}")
    print(f"Numbers               : {has_number(password)}")
    print(f"Special Characters    : {has_special(password)}")

    print(f"\nCharacter Diversity   : {character_diversity(password)}/4")
    print(f"Entropy               : {entropy} bits")
    print(f"Estimated Crack Time  : {crack_time}")

    print(f"\nScore                 : {score}")
    print(f"Strength Rating       : {strength}")

    if is_common_password(password, common_passwords):
        print("\n⚠ WARNING: Common password detected!")

    if has_repeated_characters(password):
        print("⚠ Repeated characters detected!")

    if has_sequential_pattern(password):
        print("⚠ Sequential pattern detected!")

    print("\nRecommendations:")

    if recommendations:
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("- Excellent password. No recommendations.")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()