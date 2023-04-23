from flask import Flask, render_template
from pytz import timezone
from flask import request
from datetime import datetime
from datetime import timedelta
from itertools import cycle, islice

import random
import statsapi
import requests
import itertools
import time
import pytz

app = Flask(__name__)

teamIDs = {
  "NYY": 147,
  "NYM": 121,
  "ATL": 144,
  "SF": 137,
  "OAK": 133,
  "LAA": 108,
  "CLE": 114,
  "LAD": 119,
  "SEA": 136,
  "CIN": 113,
  "WAS": 120,
  "PIT": 134,
  "MIL": 158,
  "STL": 138,
  "CHI": 112,
  "PHI": 143,
  "TOR": 141,
  "BOS": 111,
  "CWS": 145,
  "TB": 139,
  "BAL": 110,
  "DET": 116,
  "ARI": 109,
  "COL": 115,
  "SD": 135,
  "MIN": 142,
  "TEX": 140,
  "HOU": 117,
  "MIA": 146,
  "KC": 118,
}

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/result")
def result():
  
  team = request.args.get('team')
  team = team.upper()
  gameday = request.args.get('gamedate')

  currentday = datetime.now()
  days_before = currentday - timedelta(days=20)
  
  currentday_str = currentday.strftime("%Y-%m-%d")
  days_before_str = days_before.strftime("%Y-%m-%d")

  single_game_sched = statsapi.schedule(start_date=gameday, end_date=gameday, team=teamIDs[team])

  if not single_game_sched:
    return render_template("answer.html", pitcher={"sp": "no one.", "gameday": "Looks like your team is not playing on the date you provided.", "score": "Try checking your dates and try again."})
  
  if single_game_sched[0]['home_id'] == teamIDs[team]:
      result = "home"
  elif single_game_sched[0]['away_id'] == teamIDs[team]:
      result = "away"

  if single_game_sched[0][f"{result}_probable_pitcher"] != '':
     return render_template("answer.html", pitcher={"sp": single_game_sched[0][f"{result}_probable_pitcher"], "gameday": gameday, "score": f"{single_game_sched[0]['away_name']} @ {single_game_sched[0]['home_name']}"})

  sched = statsapi.schedule(start_date=days_before_str,end_date=currentday_str,team=teamIDs[team])
  
  pitcher_list = []
  game_list = sorted(sched, key = lambda game: game["game_date"] and game["status"] != 'Cancelled' and game['status'] != 'Postponed')
  game_list.reverse()

  for game in game_list[0:5]:
    if game['home_id'] == teamIDs[team]:
      result = "home"
    elif game['away_id'] == teamIDs[team]:
      result = "away"
    print(game['game_date'])
    pitcher_list.append(game[f"{result}_probable_pitcher"])
  pitcher_list.reverse()

  print(pitcher_list)
  
  gamesched = statsapi.schedule(start_date=currentday_str, end_date=gameday, team=teamIDs[team])

  pitcher_cycle = cycle(pitcher_list)  
  rotation = [pitcher_list[4], pitcher_list[0], pitcher_list[1], pitcher_list[2], pitcher_list[3]]
  starting_last = islice(pitcher_cycle,4, None)
  
  for game in gamesched:
    if game["status"] != "Final":
      current_pitcher = next(starting_last)
      print(current_pitcher + " pitching on " + game['game_date'])
    else: 
      pass
  final_result = current_pitcher

  return render_template("answer.html", pitcher={"sp": final_result, "gameday": gameday, "score": f"{game['away_name']} @ {game['home_name']}", "rotation": rotation})

if __name__ == "__main__": 
	app.run(
		host='0.0.0.0',
		port=random.randint(2000 , 9000))