from ..Analysis.Graphique import Graphique
from ..Analysis.Histogramme import Histogramme


class Menu_Graphique()
    """
    Menu permettant de gérer l'affichage des graphiques et autre
    """
    def __init__(self, parser, sport):
        self.parser = parser
        self.sport = sport
        self.hist = 

    def answer_question(self, autorise_value: set):
        result: str = input("Réponse : ")
        if not result.isnumeric():
            print("La valeur renseignée n'est pas valide")
            result = -1
        elif int(result) not in autorise_value:
            print("La valeur renseignée n'est pas correct")
            result = -1
        else:
            result = int(result)
        return result
    
    def main_menu(self):
        """
        Fonction permettant de savoir quelles graphique présenter
        """
        while True:
            print("-------------------------------------------")
            print("Que voulez-vous voir ?")
            print("1. Histogramme")
            print("2. ")
            print("3. \n")
            print("0. Revenir en arrière\n\n")
            result = self.answer_question({0, 1, 2, 3})
            result_match = {
                1: self.menu_recherche_joueurs,
                2: self.menu_recherche_equipe,
                3: self.menu_recherche_match
            }
            if result == 0:
                return
            elif result != -1:
                if result == 2 and self.sport in {"tennis"}:
                    print("Il n'y a pas d'équipe dans ce sport")
                else:
                    result_match[result]()