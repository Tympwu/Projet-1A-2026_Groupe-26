from ..Query.recherche import Recherche

class Menu:
    """ """

    def __init__(self):
        self.__admin: bool = False
        self.__password_admin: str = "azerty"
        self._sports: dict[int, str] = {
            1: "basketball", 
            2: "football_european_leagues",
            5: "league_of_legends",
            3: "tennis",
            4: "volleyball"}

    def connect(self):
        """
        Fonction permettant de se connecter pour obtenir des droits administrateurs

        Returns
        -------
        int : Renvoie 0 si tout s'est bien passé, -1 si l'individu à annulé
        """
        print("-------------------------------------------")
        connexion_reussie = False
        mdp = ""
        while not connexion_reussie:
            mdp = input("Mot de passe (-1 pour annuler) :\n")
            if mdp == "-1":
                break
            elif mdp == self.__password_admin:
                self.__admin = True
                print("Connexion réussie !\n \n")
                connexion_reussie = True
            else:
                print("Mot de passe éronné !\n")

    def deconnect(self):
        """
        Fonction permettant de se déconnecter
        """
        print("-------------------------------------------")
        confirmation = ""
        while confirmation != "oui":
            confirmation = input(
                "Voulez-vous vraiment vous déconnecter ? (oui / non)\n"
            )
            if not confirmation.isalpha():
                print("La réponse doit être des caractères ! \n")
            else:
                if confirmation.lower() not in ("oui", "non"):
                    print("La réponse n'est pas valide")
                elif confirmation.lower() == "oui":
                    self.__admin = False
                else:
                    break

    def help(self):
        """Fonction d'aide indiquant différentes informations sur l'application
        """

        print("""-------------------------------------------\n
        Application permettant de traiter et d'analyser des données sur des bases de données
        de différents sports / e-sports.\n
        Pour l'instant les sports / e-sports supportés sont : \n
        Basketball\n
        Football européen\n
        Tennis\n
        Volleyball\n
        League-of-Legends\n\n

        A tout moment, si vous répondez -1 à une question cela permettra de revenir en arrière\n\n

        Application faîte par Alexandre Yu, Simon Langlois-Tino, Jean Pohardy et Timothé Pouplin
        """)

    def proposition_sports(self):
        """Fonction permettant de choisir le sport qui nous intéresse et quelles données analyser"""
        print("-------------------------------------------")
        while True:
            print("""Quel sport voulez-vous étudier ?\n
            1. Basketball\n
            2. Football européen\n
            3. Tennis\n
            4. Volleyball\n
            5. League-of-Legends\n\n

            -1. Revenir en arrière
            """)
            result = input("Indiquez votre réponse : ")
            if not result.isalnum():
                print("Le résultat doit être un entier")
            elif int(result) not in {-1, 1, 2, 3, 4, 5}:
                print("L'entier renseigné n'est pas valide")
            else:
                result = int(result)
                if result == -1:
                    break
                else:
                    search = Recherche(self._sports[result])
                    search.cherche()
                    break

    def main_menu(self):
        """
        Fonction principale permettant de faire tourner l'application
        """
        print("-------------------------------------------")
        print("Bonjour, \n Que voulez-vous faire ?\n")
        while True:
            print("1. Traiter une base de donnée\n2. Se connecter avec un compte administrateur")
            print("3. Obtenir de l'aide vis-à-vis de l'application\n\n-1. Quitter l'application")
            result: str = input("Réponse : ")
            if not result.isalnum():
                print("La valeur renseignée n'est pas valide")
            elif int(result) not in {1, 2, 3, -1}:
                print("La valeur renseignée n'est pas correct")
            else:
                result = int(result)
                if result == -1:
                    break
                elif result == 2:
                    self.connect()
                elif result == 1:
                    self.proposition_sports()
                else:
                    self.help()
        
