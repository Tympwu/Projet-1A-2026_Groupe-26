# import pandas as pd

from src.Interface.Menu import Menu
from src.DAO.interaction import DAO

Interface = Menu()

#Interface.main_menu()

from src.Model.Competition import Competition

test = Competition("tennis", 15, "Manchester")
print(test)