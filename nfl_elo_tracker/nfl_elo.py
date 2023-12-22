import http.client
import json
import matplotlib.pyplot as plt
import sys

# Possible changes to make:
# Playoff games become more important
# Alternatively, playoff wins boost your score but playoff losses do not hurt it
# The points gained come at the expense of every non-playoff team
# A 30-point win has a greater impact on your score than a 1-point win
# Change starting ELO totals based on which teams were the best coming into 2002
# This should be straightforward, the higher a team picks in the draft the lower their ELO is


# This value holds every Elo rating by week, with all teams starting at 1000
# at the beginning of the 2002 season. 
# Is this fair? No. I might change it.
elos_dict = {'bears':[(1000, "0-2002")], 'packers':[(1000, "0-2002")], 'vikings':[(1000, "0-2002")], 'lions':[(1000, "0-2002")], \
        'eagles':[(1000, "0-2002")], 'giants':[(1000, "0-2002")], 'commies':[(1000, "0-2002")], 'cowboys':[(1000, "0-2002")], \
        'niners':[(1000, "0-2002")], 'seahawks':[(1000, "0-2002")], 'rams':[(1000, "0-2002")], 'cardinals':[(1000, "0-2002")], \
        'buccaneers':[(1000, "0-2002")], 'panthers':[(1000, "0-2002")], 'saints':[(1000, "0-2002")], 'falcons':[(1000, "0-2002")], \
        'bills':[(1000, "0-2002")], 'dolphins':[(1000, "0-2002")], 'patriots':[(1000, "0-2002")], 'jets':[(1000, "0-2002")], \
        'chiefs':[(1000, "0-2002")], 'chargers':[(1000, "0-2002")], 'raiders':[(1000, "0-2002")], 'broncos':[(1000, "0-2002")], \
        'bengals':[(1000, "0-2002")], 'ravens':[(1000, "0-2002")], 'steelers':[(1000, "0-2002")], 'browns':[(1000, "0-2002")], \
        'texans':[(1000, "0-2002")], 'colts':[(1000, "0-2002")], 'titans':[(1000, "0-2002")], 'jaguars':[(1000, "0-2002")]}
team_names_to_elo_names = {"Denver Broncos":'broncos', "St. Louis Rams":'rams', "Buffalo Bills":'bills', "Los Angeles Rams":'rams',\
        "New York Jets":'jets', "Atlanta Falcons":'falcons', "New Orleans Saints":'saints', "Baltimore Ravens":'ravens',\
        "Cincinnati Bengals":'bengals', "Pittsburgh Steelers":'steelers', "Miami Dolphins":'dolphins', "New England Patriots":'patriots',\
        "Washington Commanders":'commies', "Washington Football Team":'commies', "Washington Redskins":'commies', "Los Angeles Chargers":'chargers',\
        "Las Vegas Raiders":'raiders', "Jacksonville Jaguars":'jaguars', "Oakland Raiders":'raiders', "Chicago Bears":'bears', "San Francisco 49ers":'niners',\
        "Carolina Panthers":'panthers', "Cleveland Browns":'browns', "Houston Texans":'texans', "Indianapolis Colts":'colts', \
        "Detroit Lions":'lions', "Philadelphia Eagles":'eagles', "Minnesota Vikings":'vikings', "Green Bay Packers":'packers',\
        "Tennessee Titans":'titans', "New York Giants":'giants', "Arizona Cardinals":'cardinals', "Kansas City Chiefs":'chiefs',\
        "Dallas Cowboys":'cowboys', "Tampa Bay Buccaneers":'buccaneers', "Seattle Seahawks":'seahawks', "San Diego Chargers":'chargers'}

ELO_K_FACTOR = 32

def get_reg_season(year):

    my_key = 'e888y7w5pvgs8cn5erhwhptm'

    conn = http.client.HTTPSConnection("api.sportradar.us")

    conn.request("GET", "/nfl/official/trial/v7/en/games/" + str(year) + "/REG/schedule.json?api_key=" + my_key)

    res = conn.getresponse()
    data = res.read()

    json_to_file = data.decode("utf-8")

    file = open('regular_season_' + str(year) + '.json', 'a')
    file.write(json_to_file)
    file.close()

def get_postseason(year):

    my_key = 'e888y7w5pvgs8cn5erhwhptm'

    conn = http.client.HTTPSConnection("api.sportradar.us")

    conn.request("GET", "/nfl/official/trial/v7/en/games/" + str(year) + "/PST/schedule.json?api_key=" + my_key)

    res = conn.getresponse()
    data = res.read()

    json_to_file = data.decode("utf-8")

    file = open('postseason_' + str(year) + '.json', 'a')
    file.write(json_to_file)
    file.close()

def get_expected_score(player_score, opponent_score):
    return 1 / (1 + (10**((opponent_score - player_score) / 400)))

# winner is either 'h' for home, 'a' for away, or 't' for tie

def calc_elo(home_team, away_team, winner, week_in_year):
    home_elo = elos_dict[home_team][len(elos_dict[home_team]) - 1][0]
    away_elo = elos_dict[away_team][len(elos_dict[away_team]) - 1][0]
    home_expected = get_expected_score(home_elo, away_elo)
    away_expected = get_expected_score(away_elo, home_elo)
    if winner == 'h':
        home_elo = (home_elo + (ELO_K_FACTOR * (1 - home_expected)), week_in_year)
        away_elo = (away_elo - (ELO_K_FACTOR * away_expected), week_in_year)
    elif winner == 'a':
        away_elo = (away_elo + (ELO_K_FACTOR * (1 - away_expected)), week_in_year)
        home_elo = (home_elo - (ELO_K_FACTOR * home_expected), week_in_year)
    elif winner == 't':
        home_elo = (home_elo + (ELO_K_FACTOR * (0.5 - home_expected)), week_in_year)
        away_elo = (away_elo + (ELO_K_FACTOR * (0.5 - away_expected)), week_in_year)
    elos_dict[home_team].append(home_elo)
    elos_dict[away_team].append(away_elo)


def get_elo_for_week(current_week, current_year):
    week_in_year = current_week['title'] + "-" + str(current_year)
    for game in current_week['games']:
        if 'scoring' not in game.keys():
            continue
        home_team = game['home']['name']
        if home_team not in team_names_to_elo_names.keys():
            continue
        home_team = team_names_to_elo_names[home_team]
        away_team = game['away']['name']
        away_team = team_names_to_elo_names[away_team]
        if game['scoring']['home_points'] > game['scoring']['away_points']:
            calc_elo(home_team, away_team, 'h', week_in_year)
        elif game['scoring']['home_points'] < game['scoring']['away_points']:
            # Away team won
            calc_elo(home_team, away_team, 'a', week_in_year)
        else:
            # Tie
            calc_elo(home_team, away_team, 't', week_in_year)
    fix_bye_week(week_in_year)

# How to deal with bye weeks-this is not an issue if it happens during the postseason as well
def fix_bye_week(week_in_year):
    max_length = 0
    for key in elos_dict:
        if len(elos_dict[key]) > max_length:
            max_length = len(elos_dict[key])
    for key in elos_dict:
        if len(elos_dict[key]) < max_length:
            elos_dict[key].append((elos_dict[key][len(elos_dict[key]) - 1][0], week_in_year))

def plot_team(team):
    scores = [x[0] for x in elos_dict[team]]
    plt.plot(scores, label=team)

# season is 'r' if regular or 'p' if postseason
def add_year_to_elo(year, season):
    year_string = str(year)
    if season == 'r':
        f = open('games\\regular_season\\regular_season_' + year_string + '.json')
    elif season == 'p':
        f = open('games\\postseason\\postseason_' + year_string + '.json')
    first_year = json.load(f)
    for week in first_year['weeks']:
        get_elo_for_week(week, year)
    f.close()

# title is the title of the graph
# teams is a list of every team being plotted

def plot_multiple_teams(teams, title):
    plt.title(title)
    plt.xlabel("Games Played Since Start of 2002 Season")
    plt.ylabel("Elo Rating")
    for squad in teams:
        plot_team(squad)
    plt.legend(loc="upper left")
    plt.show()

# NOTE: The Rams, Chargers, and Raiders moved and now go by different IDs
# NOTE: Also the Redskins/Football Team/Commanders changed names

if __name__ == "__main__":
    # Our dataset starts from the 2002 season. This is because the league
    # reached 32 teams in 2002 with the addition of the Houston Texans.
    for i in range(2002, 2023):
        add_year_to_elo(i, 'r')
        add_year_to_elo(i, 'p')
    title = sys.argv[1]
    teams_requested = []
    for j in range(2, len(sys.argv)):
        teams_requested.append(sys.argv[j])
    plot_multiple_teams(teams_requested, title)