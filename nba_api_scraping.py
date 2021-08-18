import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Import recruits
recruits_all = pd.read_csv('/Users/joerussell/Desktop/DATASCIENCE/PROJECTS/ESPNrecruits/recruiting_classes.csv')

# In this analysis, we only want recruits in older classes so they all have NBA experience
recruits = recruits_all[recruits_all.Class <= 2017]


# Import NBA players
from nba_api.stats.static import players
player_dict = players.get_players()

recruit_names = recruits.Name.tolist()
nba_players = [player for player in player_dict if player['full_name'] in recruit_names]
nba_player_ids = [player['id'] for player in nba_players]
nba_df = pd.DataFrame(nba_players)

# Drop players who share names to avoid mixing up stats
nba_df.drop_duplicates(subset=['full_name'], inplace=True)

# Import career stats
from nba_api.stats.endpoints import PlayerCareerStats

MIN = []
GP = []
PTS = []
REB = []
AST = []
STL = []
BLK = []
TOV = []
FGM = []
FGA = []
FG3M = []
FG3A = []

stats_list = [MIN, GP, PTS, REB, AST, STL, BLK, TOV, FGM, FGA, FG3M, FG3A]
stats_cols = ['MIN', 'GP', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FGM', 'FGA', 'FG3M', 'FG3A']

# Get stats for each player in our list (takes about 8 minutes)
stats = []
for player in nba_player_ids:
    stats.append(PlayerCareerStats(player_id=player).get_data_frames()[0])
    time.sleep(0.7)
    
stats_df = pd.concat(stats).reset_index(drop=True)

# Fill stat lists with player data (zeros for non-NBA recruits) and insert into dataframe
recruit_names = recruits.Name.tolist()
nba_names = nba_df.full_name.tolist()

for i in range(12):
    for recruit in recruit_names:
        if recruit in nba_names:
            player_id = nba_df[nba_df.full_name == recruit].id
            total = stats_df[stats_df.PLAYER_ID == int(player_id)][stats_cols[i]].sum()
            stats_list[i].append(total)
        else:
            stats_list[i].append(0)
    recruits[stats_cols[i]] = stats_list[i]

recruits.to_csv("nba_recruits.csv")


