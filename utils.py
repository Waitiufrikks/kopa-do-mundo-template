from datetime import datetime
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


def data_processing(team):
    current_year = datetime.now().year
    total_years_cup = list(range(1930, current_year, 4))

    team_first_cup = int(team["first_cup"][:4])

    if team["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if team_first_cup not in total_years_cup:
        raise InvalidYearCupError("there was no world cup this year")

    if team["titles"] > len(total_years_cup) - total_years_cup.index(team_first_cup):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
    print(total_years_cup)


test = {
    "name": "Brasil",
    "titles": 5,
    "top_scorer": "Pelé",
    "fifa_code": "BRA",
    "first_cup": "1930-08-18",
}

data_processing(test)
