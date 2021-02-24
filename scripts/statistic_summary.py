import sys
sys.path.append('../')
import season
import utils
import constants
import pandas as pd
from tqdm import tqdm


NUM_SIMS = int(1e6)
best_wins = dict()
for position in constants.POSITIONS:
    best_wins[position] = 0

for sim in tqdm(range(NUM_SIMS)):
    df = pd.DataFrame.from_dict(season.simulate_season(utils.create_teams()))
    df = df.transpose()

    #print(df)
    # TODO: if teams are tied for first, need to include both.
    best_teams = df[df[constants.WINS] == df[constants.WINS].max()].index
    best_chasers = df[df[constants.CHASER] == df[constants.CHASER].max()].index
    best_beaters = df[df[constants.BEATER] == df[constants.BEATER].max()].index
    best_keepers = df[df[constants.KEEPER] == df[constants.KEEPER].max()].index
    best_seekers = df[df[constants.SEEKER] == df[constants.SEEKER].max()].index

    #print(best_teams)
    #print(best_chasers)
    #print(best_beaters)
    #print(best_keepers)
    #print(best_seekers)
    for best_team in best_teams.values:
        for best_chaser in best_chasers:
            if best_team == best_chaser:
                best_wins[constants.CHASER] += 1
        for best_beater in best_beaters:
            if best_team == best_beater:
                best_wins[constants.BEATER] += 1
        for best_keepers in best_keepers:
            if best_team == best_keepers:
                best_wins[constants.KEEPER] += 1
        for best_seeker in best_seekers:
            if best_team == best_seeker:
                #print(f"Best Seeker team won with {df.loc[constants.WINS].max()} wins")
                best_wins[constants.SEEKER] += 1
    if not sim % 10000:
        print(f"Num Wins after {sim} iterations:")
        for position in constants.POSITIONS:
            print(f"{position}: {best_wins[position]} ({100*round(best_wins[position] / (sim+1), 2)}%)")
print(f"Number wins after {NUM_SIMS} simulated seasons")
for position in constants.POSITIONS:
    print(f"{position}: {best_wins[position]} ({round(best_wins[position]/NUM_SIMS, 2)}")