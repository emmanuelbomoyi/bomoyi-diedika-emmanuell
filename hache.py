# =========================================================
#  TP DE CRYPTOGRAPHIE
#  Fonction de hachage personnalisée
#
#  Auteur : emmanuel bomoyi diedika
#  Langage : Python
# =========================================================

import time


class HashEmmanuel:
    """
    Classe représentant une fonction de hachage personnalisée.
    """

    def __init__(self):
        # Nombre premier utilisé pour améliorer la dispersion
        self.prime = 31

        # Modulo pour limiter la taille du hash
        self.modulo = 1000000007

    def generer_hash(self, message):
        """
        Génère une valeur de hachage à partir d'un message.

        Paramètre :
            message (str) : texte à hacher

        Retour :
            int : valeur du hash
        """

        hash_value = 7

        for index, caractere in enumerate(message):

            # Transformation ASCII
            ascii_value = ord(caractere)

            # Calcul du hash
            hash_value = (
                hash_value * self.prime
                + ascii_value
                + index
            ) % self.modulo

        return hash_value


# =========================================================
# PROGRAMME PRINCIPAL
# =========================================================

def afficher_entete():
    print("=" * 55)
    print("      TP DE CRYPTOGRAPHIE - FONCTION DE HACHAGE")
    print("=" * 55)
    print()


def main():

    afficher_entete()

    texte = input("Entrez un message à hacher : ")

    debut = time.time()

    # Création de l'objet hash
    hash_obj = HashBenjamin()

    # Génération du hash
    resultat = hash_obj.generer_hash(texte)

    fin = time.time()

    print("\n---------- RESULTAT ----------")
    print(f"Message           : {texte}")
    print(f"Valeur de hash    : {resultat}")
    print(f"Longueur message  : {len(texte)} caractères")
    print(f"Temps d'exécution : {(fin - debut):.6f} seconde(s)")
    print("--------------------------------")


# =========================================================
# EXECUTION
# =========================================================

if __name__ == "__main__":
    main()
