vragen = [
    "Gebruik je verschillende wachtwoorden voor verschillende accounts?",
    "Gebruik je twee-factor-authenticatie (2FA) waar mogelijk?",
    "Gebruik je een wachtwoordmanager?",
    "Update je je apparaten en apps regelmatig?",
    "Controleer je de afzender voordat je op een link in een mail klikt?",
]

def stel_vraag(vraag):
    while True:
        antwoord = input(vraag + " (j/n): ").strip().lower()
        if antwoord in ("j", "n"):
            return antwoord == "j"
        print("Antwoord met j of n.")

def beoordeel(score, totaal):
    procent = score / totaal * 100
    if procent >= 80:
        return "Sterk! Je bent goed bezig."
    elif procent >= 50:
        return "Redelijk, maar er is ruimte voor verbetering."
    return "Pas op, je hebt risico's. Begin met een wachtwoordmanager."

score = 0
for vraag in vragen:
    if stel_vraag(vraag):
        score += 1

print(f"\nScore: {score}/{len(vragen)}")
print(beoordeel(score, len(vragen)))
