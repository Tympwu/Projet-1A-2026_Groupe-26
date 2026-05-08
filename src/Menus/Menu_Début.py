from ..DAO.Data_load import Data_loader
from ..Parsers.Tennis_parser import Tennis_Parser
from ..Parsers.Basketball_parser import Basketball_Parser
from ..Parsers.Volleyball_parser import Volleyball_Parser
from ..Parsers.League_of_legend_parser import League_of_legend_Parser
from ..Parsers.Football_E_parser import Football_European_leagues_Parser
from ..Menus.Menu import Menu
from ..Menus.Menu_Recherche import Recherche
from ..DAO.Export_data import Export_data
from ..Menus.Menu_Graph import Menu_Graphique


class Menu_Début(Menu):
    """ """

    def __init__(self):
        super().__init__()
        self.__password_admin: str = "azerty"
        self._sports: dict[int, str] = {
            1: "basketball",
            2: "football_european_leagues",
            3: "tennis",
            4: "league_of_legends",
            5: "volleyball",
            6: "badminton"}
        self.parser = None
        self.__graph_menu: Menu_Graphique = None
        self.sport_choosen: int = None
        self.team_sport: bool = True
        self.__recherche_data: Recherche | None = None

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
                self.admin = True
                print("Connexion réussie ! \U0001F513\n \n")
                connexion_reussie = True
            else:
                print("Mot de passe éronné !\n")

    def deconnect(self):
        """
        Fonction permettant de se déconnecter
        """
        result = self.menu_question(
            "Voulez-vous vraiment vous déconnecter ?",
            ["oui", "non"],
            {1: True, 2: False})
        if result:
            self.admin = False
        return

    def connect_deconnect(self):
        """
        Fonction permettant de faire l'intermédiaire entre la position connecté et pas connecté
        """
        if self.admin:
            self.deconnect()
        else:
            self.connect()

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
        League-of-Legends
        Volleyball


        A tout moment, si vous répondez 0 à une question cela permettra de revenir en arrière

        Application faîte par Alexandre Yu, Simon Langlois-Tino, Jean Pohardy et Timothé Pouplin
        """)

    def main_menu(self):
        """
        Fonction initiale permettant de faire tourner l'application
        """
        self.menu_question(
            "Bonjour, \nQue voulez-vous faire ?\n",
            ["Traiter une base de donnée",
             "Se connecter au / déconnecter du compte administrateur",
             "Obtenir de l'aide"],
            {1: self.proposition_sports, 2: self.connect_deconnect, 3: self.help},
            break_on_call=False)

    def proposition_sports(self):
        """Fonction permettant de choisir le sport qui nous intéresse et quelles données analyser"""
        while True:
            result = self.menu_question(
                "Quel sport voulez-vous étudier ?",
                ["Basketball", "Football européen", "Tennis", "League-of-Legends", "volleyball"],
                None)
            if result == 0:
                return
            else:
                self.sport_choosen = result
                self.__search = Data_loader(self._sports[result])
                self.__search.loader()
                self.search_parser()

    def search_parser(self):
        """
        Fonction permettant de lier et utiliser les bons parser correspondant aux sports
        """
        if self.sport_choosen == 1:  # Basketball
            self.initialize_parser(
                Basketball_Parser(), self._sports[self.sport_choosen], self.__search
            )
            self.parser.parse_equipes(self.search.dao["team"].data)
            print("Equipes sans joueurs chargées")
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargées et ajoutés dans les équipes")
            self.parser.parse_matchs(self.search.dao["game"].data, self.search.dao["team"].data)
            print("Matchs chargés\n")

        elif self.sport_choosen == 2:  # Football european
            self.initialize_parser(
                Football_European_leagues_Parser(), self._sports[self.sport_choosen], self.__search
            )
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargés")
            self.parser.parse_equipes(self.search.dao["equipe"].data)
            print("Equipes chargées")
            self.parser.parse_matchs(self.search.dao["match"].data,
                                     other=self.search.dao["country"].data)
            print("Matchs chargés")

        elif self.sport_choosen == 3:  # Tennis
            self.initialize_parser(Tennis_Parser(), self._sports[self.sport_choosen], self.__search)
            self.parser.parse_players(self.search.dao["atp_players_2024"].data, other="H")
            self.parser.parse_players(self.search.dao["wta_players_2024"].data, other="F")
            print("Joueurs chargés")
            self.parser.parse_matchs(self.search.dao["wta_matches_2024"].data)
            self.parser.parse_matchs(self.search.dao["atp_matches_2024"].data)
            print("Matchs chargés")
            self.team_sport = False

        elif self.sport_choosen == 4:  # leagues of legends
            self.initialize_parser(
                League_of_legend_Parser(), self._sports[self.sport_choosen], self.__search
            )
            self.parser.parse_equipes(self.search.dao["team"].data)
            print("Equipes sans joueurs chargées")
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargées et ajoutés dans les équipes")
            self.parser.parse_coachs(self.search.dao["coach"].data)
            print("Coachs chargées et ajouté dans les equipes")
            self.parser.parse_matchs(self.search.dao["match"].data, self.search.dao["team"].data)
            print("Matchs chargés")

        elif self.sport_choosen == 5:  # volleyball
            self.initialize_parser(
                Volleyball_Parser(), self._sports[self.sport_choosen], self.__search
            )
            self.parser.parse_equipes(self.search.dao["country"].data, other="H")
            self.parser.parse_equipes(self.search.dao["country"].data, other="F")
            print("Equipes sans joueurs chargées")
            self.parser.parse_players(self.search.dao["player_men"].data, other="H")
            self.parser.parse_players(self.search.dao["player_women"].data, other="F")
            print("Joueurs chargées et ajoutés dans les équipes")
            self.parser.parse_coachs(self.search.dao["coach_men"].data, other="H")
            self.parser.parse_coachs(self.search.dao["coach_women"].data, other="F")
            print("Coachs chargées et ajouté dans les equipes")
            self.parser.parse_matchs(
                self.search.dao["match_men"].data, self.search.dao["country"].data, sexe="H"
            )
            self.parser.parse_matchs(
                self.search.dao["match_women"].data, self.search.dao["country"].data, sexe="F"
            )
            print("Matchs chargés")

        # Création du module de rercherche des données
        self.__recherche_data = Recherche()

        # Création du module d'export des données correspondant et du modèle graphique
        self.__graph_menu = Menu_Graphique()
        self.__export_data = Export_data(self.__search)

        # Après avoir importé les données
        self.analyse_data()

    def analyse_data(self):
        choix = [
            "Visualiser les données", "Construire des graphiques des données",
            "Exporter les données", "Ajouter des données"]
        dict_choix = {
            1: self.__recherche_data.visualise_data,
            2: self.__graph_menu.main_menu,
            3: self.__export_data.menu_export_data,
            4: self.__export_data.add_data}
        if not self.admin:
            choix.pop(3)
            del dict_choix[4]
        self.menu_question(
            "Que voulez-vous faire désormais ?",
            choix,
            dict_choix
            )
