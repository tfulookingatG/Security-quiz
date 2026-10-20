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
    if score >= 80:
        return "Strong! You're doing well."
    elif score >= 50:
        return "Decent, but there is room for improvement."
    return "Watch out, you have risks."


score = 0
tips = []

for question, weight, tip in questions:
    if ask_question(question):
        score += weight
    else:
        tips.append((weight, tip))

print(f"\nScore: {score}/100")
print(rate(score))

if tips:
    print("\nTips (most important first):")
    tips.sort(reverse=True)
    for weight, tip in tips:
        print(f"- {tip}")
