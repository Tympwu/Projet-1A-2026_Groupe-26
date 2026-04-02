from ..Query.recherche import recherche

class Menu:
    """ """

    def __init__(self):
        self.__admin: bool = False
        self.__password_admin: str = "azerty"

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
        
