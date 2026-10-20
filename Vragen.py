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
