

def vigenere_chiffre():
    message = input("Quel est ton message à chiffrer ? ")
    cle = input("Quelle est la clé ? ")
    print(f"tu veux chiffrer {message}, avec {cle} comme clé.")

    cle_repetee = ""
    i = 0

    for lettre in message:
        if lettre.isalpha():
            cle_repetee += cle[i % len(cle)]
            i += 1
        else:
            cle_repetee += lettre  # On garde l'espace ou ponctuation pour rester calé

    print("Le message chiffré est: ", message)



def vigenere_dechiffre():
    message = input("Quel est ton message chiffré ? ")
    cle = input("Quelle est la clé ? ")
    print(f"tu veux déchiffrer {message}, avec {cle} comme clé.")


    print("Le message déchiffré est: ", message)




choix = int(input("Souhaitez-vous chiffrer = 0 ou déchiffrer =1 un message? : "))

if choix == 0:
    vigenere_chiffre()
elif choix == 1:
    vigenere_dechiffre()

