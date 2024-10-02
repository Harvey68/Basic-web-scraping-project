from bs4 import BeautifulSoup
import requests
import csv
import re
from datetime import datetime
import os

url ="https://tracklock.gg/players"
page =requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

rank_data = soup.find_all(class_="font-medium text-white hidden md:table-cell")
player_data = soup.find_all(class_="font-medium text-blue-400 hover:text-blue-300 text-sm md:text-base")
elo_data = soup.find_all(class_="font-semibold text-orange-400 hidden md:table-cell")
hero_data = soup.find_all(class_="text-xs md:text-sm whitespace-nowrap overflow-hidden text-ellipsis max-w-[60px] md:max-w-none")
games_played_data = soup.find_all(class_="text-[9px] md:text-xs text-gray-400 whitespace-nowrap")
row_count = soup.find_all("tr")

games_played_parent = soup.find_all("div", class_="flex items-center gap-1 md:gap-2 min-w-[100px] md:min-w-0")

data_list =[]
count = 0
# check if hames played and heros played contains the info by using find() from the parent class
#create an if statment to add set data to N/A if classes im looking for arent there
for i in range(len(rank_data)):
    rank = rank_data[i].text
    player = player_data[i].text
    elo = elo_data[i].text

    next_element = games_played_parent[i].next_element
    class_next = next_element.get("class")
    if class_next == ['text-gray-400']:
        hero = "N/A"
        games_played = "N/A"
        count +=1
    else:
        hero =  hero_data[i-count].text
        games_played = re.sub(r'[\(\)]|games',"",games_played_data[i-count].text)
    leaderboard_data ={
        "Rank": rank,
        "Player": player,
        "Elo": elo,
        "Hero": hero,
        "Games Played": games_played,
    }
    data_list.append(leaderboard_data,)




directory = r"D:\CODING\baisc_web-scrapping_project\Leaderboard_csv_txt"
time = datetime.now().strftime("%b%d_%y")
csv_file = f"Deadlock_Leaderboard_{time}.csv"
filepath = os.path.join(directory,csv_file)
with open(filepath, mode="w", newline="",encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data_list[0].keys())
    writer.writeheader()
    writer.writerows(data_list)