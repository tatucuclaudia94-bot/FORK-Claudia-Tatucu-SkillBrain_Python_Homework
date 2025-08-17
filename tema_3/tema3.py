# Tema 3

# Informații salvate (user și parolă corecte)
user_corect = "Claudia"
parola_corecta = "687194"

# Citim datele introduse de utilizator
user_introdus = input("Introduceți numele de utilizator: ")
parola_introdusa = input("Introduceți parola: ")

# Verificăm cele 3 situații cerute
if user_introdus == user_corect and parola_introdusa == parola_corecta:
    print("Acces permis.")
elif (user_introdus == user_corect and parola_introdusa != parola_corecta) or \
     (user_introdus != user_corect and parola_introdusa == parola_corecta):
    print("User/Password incorect.")
else:
    print("Acces respins.")
