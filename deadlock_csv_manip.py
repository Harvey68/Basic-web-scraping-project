import pandas as pd
import csv
df = pd.read_csv(r'D:\CODING\baisc_web-scrapping_project\deadlock_data1.csv')

games_played = df.sort_values('Games played', ascending=False)

print(games_played)


    