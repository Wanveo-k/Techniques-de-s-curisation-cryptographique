import string

def cesar():
    
    message = input("Quel est ton mot chiffré en césar?")
    clé = int(input("Quel est le décalage?"))
    print(message, clé)
    
    message_chiffre = ""
    valeurs = []
    for lettre in message:
        if lettre.isalpha():
            base = ord('a') if lettre.islower() else ord('A')
            code = chr((ord(lettre) - base + clé) % 26 + base)
            message_chiffre += code
    else:
            message_chiffre += lettre


    print("Le message chiffré est: ", message_chiffre)


cesar()



