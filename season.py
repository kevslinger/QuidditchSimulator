import utils, constants
import numpy as np

def simulate_season(LEAGUE_TABLE):
    # PLAY BALL
    # Rules of the game: 
    # Scoring is the same as quidditch. 10 points for each quaffle, 150 points for each snitch.
    # The game will proceed until the snitch has been caught. 
    #   Each turn, the two teams of chasers will each get a chance for the quaffle. 
    # The chance a team wins the quaffle is (chaser / (chaser + opp beater)). So your chaser points divided by the sum of your chaser points and the opponent's beater points.
    #   In other words, if team A has 8 chaser points and team B has 4 beater points, team A has a 8/12 = 66% chance.
    # To score a goal, the chasers have to beat the keeper. the keeper has an Attribute % chance to make a save.
    #   If the team has a keeper attribute of 10, they'll have a 10% chance to make a save.
    # Finally, the two seekers will work independently. Each seeker will have a 1 + Attribute % chance to capture the snitch (the 1+ is to ensure the game definitively ends).
    for game in utils.create_double_round_robin(constants.TEAMS):
        SNITCH_CAUGHT = False
        TEAM_A = game[0]
        TEAM_B = game[1]
        SCORE = {
            TEAM_A: 0,
            TEAM_B: 0
        }  
        while not SNITCH_CAUGHT:
            # Check if Team A's Chasers beat Team B's Beaters
            team_a_quaffle = LEAGUE_TABLE[TEAM_A][constants.CHASER] > 0 and np.random.rand() <= LEAGUE_TABLE[TEAM_A][constants.CHASER] / (LEAGUE_TABLE[TEAM_A][constants.CHASER] + LEAGUE_TABLE[TEAM_B][constants.BEATER])
            # Check if Team B's Chasers beat Team A's Beaters
            team_b_quaffle = LEAGUE_TABLE[TEAM_B][constants.CHASER] > 0 and np.random.rand() <= LEAGUE_TABLE[TEAM_B][constants.CHASER] / (LEAGUE_TABLE[TEAM_B][constants.CHASER] + LEAGUE_TABLE[TEAM_A][constants.BEATER])
            # Check if Team A's Chasers beat Team B's Keeper
            if team_a_quaffle and np.random.rand() > (LEAGUE_TABLE[TEAM_B][constants.KEEPER] / constants.KEEPER_PROB):
                SCORE[TEAM_A] += 10
                LEAGUE_TABLE[TEAM_A][constants.POINTS_FOR] += 10
                LEAGUE_TABLE[TEAM_B][constants.POINTS_AGAINST] += 10
            # Check if Team B's Chasers beat Team A's Keeper
            if team_b_quaffle and np.random.rand() > (LEAGUE_TABLE[TEAM_A][constants.KEEPER] / constants.KEEPER_PROB):
                SCORE[TEAM_B] += 10
                LEAGUE_TABLE[TEAM_B][constants.POINTS_FOR] += 10
                LEAGUE_TABLE[TEAM_A][constants.POINTS_AGAINST] += 10
            # Finally, the Seeker
            snitch_prob = np.random.rand()
            if snitch_prob <= (LEAGUE_TABLE[TEAM_A][constants.SEEKER]+1) / constants.SEEKER_PROB:
                SCORE[TEAM_A] += 150
                LEAGUE_TABLE[TEAM_A][constants.POINTS_FOR] += 150
                LEAGUE_TABLE[TEAM_B][constants.POINTS_AGAINST] += 150
                LEAGUE_TABLE[TEAM_A][constants.SNITCHES_CAUGHT] += 1
                SNITCH_CAUGHT = True
            elif snitch_prob <= (LEAGUE_TABLE[TEAM_A][constants.SEEKER]+1+LEAGUE_TABLE[TEAM_B][constants.SEEKER]+1) / constants.SEEKER_PROB:
                SCORE[TEAM_B] += 150
                LEAGUE_TABLE[TEAM_B][constants.POINTS_FOR] += 150
                LEAGUE_TABLE[TEAM_A][constants.POINTS_AGAINST] += 150
                LEAGUE_TABLE[TEAM_B][constants.SNITCHES_CAUGHT] += 1
                SNITCH_CAUGHT = True
        # Update win/loss record for both teams at the end of the game.     
        if SCORE[TEAM_A] > SCORE[TEAM_B]:
            LEAGUE_TABLE[TEAM_A][constants.WINS] += 1
            LEAGUE_TABLE[TEAM_B][constants.LOSSES] += 1
        else:
            LEAGUE_TABLE[TEAM_B][constants.WINS] += 1
            LEAGUE_TABLE[TEAM_A][constants.LOSSES] += 1   
    #utils.print_league_table(LEAGUE_TABLE)
    return LEAGUE_TABLE