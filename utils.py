import constants
import numpy as np
#import pandas as pd


def create_teams() -> dict:
    """Assign attribute values to each team in the league
    
    :param teams: (list) the list of teams in the league
    :return team_attributes (dict): the dictionary containing each team and their attributes (Chase, Beater, Keeper, Seeker)
    :return standings (dict): Each team's win-loss score
    """
    # Each team will have a total of 20 attribute points out of a max of 40.
    # The lowest for each attribute is 0 and the max is 10. 
    team_attributes = dict()
    for team in constants.TEAMS:
        team_attributes[team] = dict()
        for position_stat in constants.POSITIONS + constants.STATS:
            team_attributes[team][position_stat] = 0
        for _ in range(constants.MAX_SKILL_POINTS):
            # Make sure we don't go over the max for one position
            position_idx = np.random.randint(0, 4)
            while team_attributes[team][constants.POSITIONS[position_idx]] >= constants.MAX_SKILL:
                position_idx = np.random.randint(0, 4)
            team_attributes[team][constants.POSITIONS[position_idx]] += 1
    
    return team_attributes


def create_double_round_robin(teams) -> list:
    """Create a double round robin with all the teams in the league
    :param teams: (list) the list of teams
    :return (list) the list of lists which contains each game to be played
    """
    round_robin = []
    for team1 in teams:
        for team2 in teams:
            if team1 == team2:
                continue
            round_robin.append([team1, team2])
    return round_robin


def update_standings(game, standings, score, team_a_snitch):
    # win/loss
    if score[game[0]] > score[game[1]]:
        standings[game[0]][constants.WINS] += 1
        standings[game[1]][constants.LOSSES] += 1
    else:
        standings[game[0]][constants.LOSSES] += 1
        standings[game[1]][constants.WINS] += 1
    # score
    standings[game[0]][constants.POINTS_FOR] += score[game[0]]
    standings[game[0]][constants.POINTS_AGAINST] += score[game[1]]
    standings[game[1]][constants.POINTS_FOR] += score[game[1]]
    standings[game[1]][constants.POINTS_AGAINST] += score[game[0]]
    # snitch
    if team_a_snitch:
        standings[game[0]][constants.SNITCHES_CAUGHT] += 1
    else:
        standings[game[1]][constants.SNITCHES_CAUGHT] += 1
        




def print_league_attributes(league):
    """Print out each team and their point values in tabular format"""
    output_str = ""
    for team in league:
        output_str += f"{team}: " + '\t'
        for position in league[team]:
            output_str += f"{position}: {league[team][position]} "
        output_str += "\n"
    print(output_str)


def print_score(score):
    """Print the score between the two teams"""
    output_str = ""
    for team in score:
        output_str += f"{team}: " + '\t' + f"{score[team]}\n"
    print(output_str)


def print_league_table(league_table):
    """Print out each team and their standings in tabular format"""
    output_str = "Team Name\t\t" + '\t'.join(constants.STATS + constants.POSITIONS) + '\n'
    for team in constants.TEAMS:
        output_str += f"{team}: "
        for position_or_stat in constants.POSITIONS + constants.STATS:
            output_str += '\t' + f"{league_table[team][position_or_stat]}"
        output_str += "\n"
    print(output_str)

def empty_standings():
    standings = dict()
    for team in constants.TEAMS:
        standings[team] = dict()
        for stat in constants.STATS:
            standings[team][stat] = 0
    return standings

def empty_attributes():
    attributes = dict()
    for team in constants.TEAMS:
        attributes[team] = dict()
        for position in constants.POSITIONS:
            attributes[team][position] = 0
    return attributes



