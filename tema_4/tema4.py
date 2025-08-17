# Tema 4

# PIN predefinit (conform cerinței)
pin = "199420"

# Transformă PIN-ul în litere mici
pin_lower = pin.lower()

# Evaluează lungimea PIN-ului
lungime = len(pin_lower)

if lungime < 6:
    print("Parolă slabă")
elif 6 <= lungime <= 10:
    print("Parolă medie")
else:
    print("Parolă sigură")
