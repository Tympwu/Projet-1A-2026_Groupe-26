from ..Query.data_load import Data_loader
from ..Query.Parser import Parser
from ..Query.Tennis_parser import Tennis_Parser
from ..Query.Basketball_parser import Basketball_Parser
# from ..Query.Badminton_parser import Badminton_Parser
# from ..Query.Volleyball_parser import Volleyball_Parser
from ..Query.League_of_legend_parser import League_of_legend_Parser
from ..Query.Football_E_parser import Football_European_leagues_Parser
from ..Analysis.Match_printer import Match_printer
from ..Analysis.Joueur_printer import Joueur_printer
from ..Analysis.Equipe_printer import Equipe_printer
from ..Interface.Menu import Menu
from ..Interface.Menu_Recherche import Recherche
from ..DAO.export_data import Export_data


class Menu_Début(Menu):
    """ """

    def __init__(self):
        super().__init__()
        self.__password_admin: str = "azerty"
        self._sports: dict[int, str] = {
            1: "basketball",
            2: "football_european_leagues",
            3: "tennis",
            4: "volleyball",
            5: "league_of_legends",
            6: "Badminton"}
        self.parser: Parser = None
        self.__search: Data_loader = None
        self.sport_choosen: int = None
        self.team_sport: bool = True
        self.__recherche_data: Recherche | None = None
        self.__match_printer: Match_printer = None
        self.__equipe_printer: Equipe_printer = None
        self.__joueur_printer: Joueur_printer = None

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
        Volleyball
        League-of-Legends


        A tout moment, si vous répondez 0 à une question cela permettra de revenir en arrière

        Application faîte par Alexandre Yu, Simon Langlois-Tino, Jean Pohardy et Timothé Pouplin
        """)

    def main_menu(self):
        """
        Fonction initiale permettant de faire tourner l'application
        """
        self.menu_question(
            "Bonjour, \n Que voulez-vous faire ?\n",
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
                ["Basketball", "Football européen", "Tennis", "Volleyball", "League-of-Legends"],
                None)
            if result == 0:
                return
            else:
                self.sport_choosen = result
                self.__search = Data_loader(self._sports[result])
                self.search.loader()
                self.search_parser()

    def search_parser(self):
        """
        Fonction permettant de lier et utiliser les bons parser correspondant aux sports
        """
        if self.sport_choosen == 1:  # Basketball
            self.initialize_parser(Basketball_Parser())
            self.parser.parse_equipes(self.search.dao["team"].data)
            print("Equipe sans joueurs chargées")
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargées et ajoutés dans les équipes")
            self.parser.parse_matchs(self.search.dao["game"].data, self.search.dao["team"].data)
            print("Match chargés\n")

        elif self.sport_choosen == 2:  # Football european
            self.initialize_parser(Football_European_leagues_Parser())
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargés")
            self.parser.parse_equipes(self.search.dao["equipe"].data)
            print("Equipes chargées")
            self.parser.parse_matchs(self.search.dao["match"].data,
                                     other=self.search.dao["country"].data)
            print("Matchs chargés")

        elif self.sport_choosen == 3:  # Tennis
            self.initialize_parser(Tennis_Parser())
            self.parser.parse_players(self.search.dao["atp_players_2024"].data, other="H")
            self.parser.parse_players(self.search.dao["wta_players_2024"].data, other="F")
            print("Joueurs chargés")
            self.parser.parse_matchs(self.search.dao["wta_matches_2024"].data)
            self.parser.parse_matchs(self.search.dao["atp_matches_2024"].data)
            print("Matchs chargés")
            self.team_sport = False

        elif self.sport_choosen == 5:  # leagues of legends
            self.initialize_parser(League_of_legend_Parser())
            self.parser.parse_equipes(self.search.dao["team"].data)
            print("Equipe sans joueurs chargées")
            self.parser.parse_players(self.search.dao["player"].data)
            print("Joueurs chargées et ajoutés dans les équipes")
            self.parser.parse_coach(self.search.dao["coach"].data)
            print("Coach chargées et ajouté dans les equipes")
            self.parser.parse_matchs(self.search.dao["match"].data, self.search.dao["team"].data)
            print("Macth chargés")

        # Création des printer correspondants
        self.__joueur_printer = Joueur_printer(self.parser.dict_player)
        self.__equipe_printer = Equipe_printer(self.parser.dict_equipe)
        self.__match_printer = Match_printer(self.parser.dict_matchs, team_sport=self.team_sport)

        # Création du module de rercherche des données
        self.__recherche_data = Recherche(self._sports[self.sport_choosen], {
            "matchs": self.__match_printer,
            "joueurs": self.__joueur_printer,
            "equipes": self.__equipe_printer}
        )

        # Création du module d'export des données correspondant
        self.__export_data = Export_data()

        # Après avoir importé les données
        self.analyse_data()

    def analyse_data(self):
        self.menu_question(
            "Que voulez-vous faire désormais ?",
            ["Visualiser des données", "Analyser des liens",
             "Ajouter des données", "Exporter des données"],
            {1: self.__recherche_data.visualise_data,
             2: self.analyse_link,
             3: self.__export_data.add_data,
             4: self.__export_data.export_data}
            )
        # Créer des modules dans des fichiers à part pour chacune de ces catégories,
        # visualiser données est quasiment fait, analyser données en train d'être fait
        # partiellement par Jean, le 3 pour l'instant on abandonne et le 4 peut être fait
        # rapidement

    def analyse_link(self):
        pass
