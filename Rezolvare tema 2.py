# Exercitiul 1
numar_1, numar_2 = 10, 5
print("Numerele dvs sunt:", numar_1, "si", numar_2)
print("Adunare:", numar_1 + numar_2)
print("Scadere:", numar_1 - numar_2)
print("Inmultire:", numar_1 * numar_2)
print("Impartire:", numar_1 / numar_2)
print("Impartire intreaga:", numar_1 // numar_2)
print("Restul impartirii:", numar_1 % numar_2)
print("\n")

# Exercitiul 2
lungime, latime = 10, 5
print("Lungimea este", lungime, "si latimea este", latime)
print("Perimetrul este", 2 * (lungime + latime))
print("Aria este", lungime * latime)
print("\n")

# Exercitiul 3
numar1, numar2 = 10, 5
print("Numarul", numar1, "este mai mare decat", numar2, numar1 > numar2)
print("Numarul", numar1, "este mai mic decat", numar2, numar1 < numar2)
print("Numarul", numar1, "este egal cu", numar2, numar1 == numar2)
print("\n")

# Exercitiul 4
numar_input = 10
print(str(numar_input) + " este " + ["par", "impar"][numar_input % 2])
print("\n")

# Exercitiul 5
an_nastere = 2015
an_curent = 2025
print("Dvs aveti", an_curent - an_nastere, "ani.")
print("\n")

# Exercitiul 6
secunde_totale = 36000
numar_ore = secunde_totale // 3600
secunde_ramase = secunde_totale % 3600
minute = secunde_ramase // 60
secunde = secunde_ramase % 60
print(numar_ore, "ore,", minute, "minute,", secunde, "secunde")
print("\n")
