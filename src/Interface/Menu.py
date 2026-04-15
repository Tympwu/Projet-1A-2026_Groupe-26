from ..Query.recherche import Recherche
from ..Query.Parser import Parser
from ..Query.Tennis_parser import Tennis_Parser
from ..Query.Basketball_parser import Basketball_Parser
# from ..Query.Badminton_parser import Badminton_Parser
# from ..Query.Volleyball_parser import Volleyball_Parser
from ..Query.League_of_legend_parser import League_of_legend_Parser
from ..Query.Football_E_parser import Football_European_leagues_Parser


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
        self.__parser: Parser = None
        self.__search: Recherche = None
        self.sport_choosen: int = None

    @property
    def parser(self):
        return self.__parser

    @property
    def search(self):
        return self.__search

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
            mdp = input("Mot de passe (0 pour annuler) :\n")
            if mdp == "0":
                return
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
                    return

    def help(self):
        """Fonction d'aide indiquant différentes informations sur l'application
        """

        print("""-------------------------------------------
        Application permettant de traiter et d'analyser des données sur des bases de données
        de différents sports / e-sports.
        Pour l'instant les sports / e-sports supportés sont :
        Basketball
        Football européen
        Tennis
        Volleyball
        League-of-Legends


        A tout moment, si vous répondez 0 à une question cela permettra de revenir en arrière

        Application faîte par Alexandre Yu, Simon Langlois-Tino, Jean Pohardy et Timothé Pouplin
        """)

    def answer_question(self, autorise_value: set):
        result: str = input("Réponse : ")
        if not result.isnumeric():
            print("La valeur renseignée n'est pas valide")
        elif int(result) not in autorise_value:
            print("La valeur renseignée n'est pas correct")
        else:
            result = int(result)
        return result

    def main_menu(self):
        """
        Fonction principale permettant de faire tourner l'application
        """
        print("Bonjour, \n Que voulez-vous faire ?\n")
        while True:
            print("-------------------------------------------")
            print("1. Traiter une base de donnée\n2. Se connecter avec un compte administrateur")
            print("3. Obtenir de l'aide vis-à-vis de l'application\n\n0. Quitter l'application")
            result = self.answer_question({1, 2, 3, 0})
            if result == 0:
                return
            elif result == 2:
                self.connect()
            elif result == 1:
                self.proposition_sports()
            else:
                self.help()

    def proposition_sports(self):
        """Fonction permettant de choisir le sport qui nous intéresse et quelles données analyser"""
        while True:
            print("-------------------------------------------")
            print("""Quel sport voulez-vous étudier ?
            1. Basketball
            2. Football européen
            3. Tennis
            4. Volleyball
            5. League-of-Legends

            0. Revenir en arrière
            """)
            result = self.answer_question({0, 1, 2, 3, 4, 5})
            if result == 0:
                return
            else:
                self.sport_choosen = result
                self.__search = Recherche(self._sports[result])
                self.search.loader()
                return self.search_parser()

    def search_parser(self):
        """
        Fonction permettant de lier et utiliser les bons parser correspondant aux sports
        """
        if self.sport_choosen == 1:  # Basketball
            self.__parser = Basketball_Parser()
            self.parser.parse_equipes(self.search.dao["team"].data)
            print("Equipe sans joueurs chargées")
            print(self.parser.dict_equipe)
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargées et ajoutés dans les équipes\n")
            print(self.parser.dict_player)
            print("\n")
            print(self.parser.dict_equipe)
            self.parser.parse_matchs(self.search.dao["game"].data, self.search.dao["team"].data)
            print("Macth chargés\n")

        if self.sport_choosen == 2:  # Football european
            self.__parser = Football_European_leagues_Parser()
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargés\n")
            self.parser.parse_equipes(self.search.dao["equipe"].data)
            print("Equipes chargées\n")
            self.parser.parse_matchs(self.search.dao["match"].data,
                                     other=self.search.dao["country"].data)
            print("Matchs chargés\n")
            print(self.parser.dict_matchs)

        if self.sport_choosen == 3:  # Tennis
            self.__parser = Tennis_Parser()
            self.parser.parse_players(self.search.dao["atp_players_2024"].data, other="H")
            self.parser.parse_players(self.search.dao["wta_players_2024"].data, other="F")
            print("Joueurs chargés\n")
            print(self.parser.dict_player)

        if self.sport_choosen == 5:  # leagues of legends
            self.__parser = League_of_legend_Parser()
            self.parser.parse_equipes(self.search.dao["team"].data)
            print("Equipe sans joueurs chargées")
            print(self.parser.dict_equipe)
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargées et ajoutés dans les équipes\n")
            print(self.parser.dict_player)
            print("\n")
            print(self.parser.dict_equipe)
            self.parser.parse_coach(self.search.dao["coach"].data)
            print(self.parser.dict_coach)
            print("Coach chargées et ajouté dans les equipes\n")
            self.parser.parse_matchs(self.search.dao["match"].data, self.search.dao["team"].data)
            print("Macth chargés\n")

        # Après avoir importé les données
        self.analyse_data()

    def analyse_data(self):
        while True:
            print("-------------------------------------------")
            print("Que voulez-vous faire désormais ?")
            print("1. Visualiser des données")
            print("2. Analyser des liens")
            print("3. Ajouter des données")
            print("4. Exporter des données\n")
            print("0. Revenir en arrière\n\n")
            result = self.answer_question({1, 2, 3, 4})
            fonctions_possible = {1: self.visualise_data, 2: self.analyse_link,
                                  3: self.add_data, 4: self.export_data}
            if result == 0:
                return
            else:
                fonctions_possible[result]()

    def visualise_data(self):
        while True:
            print("-------------------------------------------")
            print("Que voulez-vous voir ?")
            print("1. Les joueurs")
            print("2. Les équipes")
            print("3. Les matchs\n")
            print("0. Revenir en arrière\n\n")
            result = self.answer_question({0, 1, 2, 3})
            result_match = {1: "joueurs", 2: "equipes", 3: "match"}
            if result == 0:
                return
            else:
                self.visualise_precise_data(result_match[result])

    def visualise_precise_data(self, wanted: str):
        while True:
            print("-------------------------------------------")
            print("Voulez-vous voir un élément précis ou l'ensemble ?")
            print("Pour un élément précis notez son indice, sinon juste validez")
            print("0. Revenir en arrière\n\n")
            result = input("Réponse : ")
            if result == "":
                print("hi")
            if not result.isnumeric():
                print("La valeur renseignée n'est pas valide")
            elif result == "0":
                return
            else:
                result = int(result)
     






    def analyse_link(self):
        pass

    def add_data(self):
        pass

    def export_data(self):
        pass
