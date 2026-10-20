import getpass

# (question, weight, tip)
questions = [
    ("Do you use different passwords for different accounts?", 20,
     "If one site gets breached, all your accounts with the same password are vulnerable. Use a unique password everywhere."),
    ("Do you use two-factor authentication (2FA) wherever possible?", 20,
     "Enable 2FA on at least your email, bank and social media. Even with your password, an attacker can't get in. Prefer an authenticator app, but SMS or email codes are better than nothing."),
    ("Do you use a password manager?", 5,
     "A manager (e.g. Bitwarden or NordPass) creates and remembers strong passwords for you."),
    ("Do you update your devices and apps regularly?", 15,
     "Updates fix security holes. Turn on automatic updates."),
    ("Do you check the sender before clicking a link in an email?", 10,
     "Phishing is the most common attack. Check the sender address and hover over the link before you click."),
    ("Do you regularly back up your important files?", 10,
     "A backup saves you from ransomware or a broken drive."),
    ("Do you have a screen lock (PIN/password) on your phone and PC?", 20,
     "Without a screen lock, anyone who finds your device has instant access to everything."),
]


def ask_question(question):
    while True:
        answer = input(question + " (Yes/No): ").strip().lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        print("Please answer Yes or No.")


def rate(score):
    if score >= 90:
        return ("Excellent",
                "You are very well protected, and it shows that you take security seriously. "
                "Your habits make you a hard target for most attackers. "
                "Keep your good routines going and stay alert for new threats.")
    elif score >= 80:
        return ("Strong",
                "You are well protected and clearly put real effort into your security. "
                "Only a few small gaps remain. "
                "Closing them will make you nearly untouchable for common attacks.")
    elif score >= 60:
        return ("Decent",
                "You have a solid base, but some important gaps remain. "
                "An attacker could still find an easy way in through them. "
                "Work through the tips below, starting with the first one.")
    elif score >= 40:
        return ("Weak",
                "Your security has serious gaps, and you are an easy target for common attacks. "
                "A single leaked password or phishing mail could cause real damage. "
                "Start with the top tips below, they will improve your score the fastest.")
    elif score >= 20:
        return ("Poor",
                "Most of your accounts and devices are poorly protected. "
                "It is likely only a matter of time before something goes wrong. "
                "Take the tips below seriously and fix them one by one, starting today.")
    return ("Very weak",
            "You are barely protected at the moment, which suggests security is not on your radar yet. "
            "Attackers will find you an easy and attractive target. "
            "The good news is that every tip below is quick to fix and makes an immediate difference.")


def test_password():
    """Rates a password out of 10: up to 6 points for length, 1 point per character type."""
    password = getpass.getpass("\nType the password you want to test (it stays hidden): ")
    length = len(password)

    # Length criteria (max 6 points)
    if length >= 15:
        length_points, length_label = 6, "Excellent"
    elif length >= 12:
        length_points, length_label = 5, "Good"
    elif length >= 9:
        length_points, length_label = 3, "Better, but not good yet"
    else:
        length_points, length_label = 1, "Weak"

    # Character criteria (1 point each)
    checks = [
        ("Uppercase letter", any(c.isupper() for c in password)),
        ("Lowercase letter", any(c.islower() for c in password)),
        ("Number", any(c.isdigit() for c in password)),
        ("Special character", any(not c.isalnum() for c in password)),
    ]
    char_points = sum(1 for _, passed in checks if passed)

    total = length_points + char_points

    print("\n--- Password test ---")
    print(f"Length ({length} characters): {length_label} ({length_points}/6)")
    for name, passed in checks:
        print(f"{name}: {'Yes' if passed else 'Missing'} ({1 if passed else 0}/1)")

    print(f"\nPassword score: {total}/10")
    if total >= 9:
        print("Excellent. This password is long and varied, which makes it very hard to crack.")
    elif total >= 7:
        print("Good. This is a solid password, but a few extra characters or types would make it stronger.")
    elif total >= 5:
        print("Average. It can still be cracked fairly quickly, so make it longer and more varied.")
    elif total >= 3:
        print("Weak. Attackers could crack this quickly. Use at least 12 characters with all character types.")
    else:
        print("Very weak. Change this password as soon as possible.")


score = 0
tips = []

for question, weight, tip in questions:
    if ask_question(question):
        score += weight
    else:
        tips.append((weight, tip))

label, comment = rate(score)
print(f"\nScore: {score}/100 - {label}")
print(comment)

if tips:
    print("\nTips (most important first):")
    tips.sort(reverse=True)
    for weight, tip in tips:
        print(f"- {tip}")

# Bonus: password tester (not part of the score)
print()
if ask_question("Bonus: would you like to test how strong your password is?"):
    test_password()
