import sqlite3
import pandas as pd

cnx = sqlite3.connect('./exo/fil_rouge/foot/database.sqlite')

df_team = pd.read_sql_query("SELECT * FROM Team_Attributes", cnx)

print(df_team[["date", "buildUpPlaySpeed","buildUpPlayDribbling", "buildUpPlayDribblingClass", "buildUpPlayPassing",
               "chanceCreationPassing", "chanceCreationCrossing", "chanceCreationShooting", "defencePressure", "defenceAggression", "defenceTeamWidth"]])