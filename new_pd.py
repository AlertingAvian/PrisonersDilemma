"""
Copyright (C) 2020 Patrick Maloney

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
"""

import nt1, nt2, nt3, nt4
import random
from importlib import reload
from art import *
from time import sleep

teams = [nt1,nt2,nt3,nt4]

def start(teams,rounds):
  '''This starts the program'''

  for team in teams:
    reload(team)
    print('reloaded',team)
    for req_var in ['name','plan']:
      if not hasattr(team, req_var):
        setattr(team, req_var, 'missing assignment')
        print(f'{team} is missing attribute: {req_var}')
    setattr(team, 'player_history', '')
    setattr(team, 'score', 0)


  print()
  print()
  print(f'There are {len(teams)} team(s)\nAnd those teams and their plans are: ')
  for team in teams:
    print(f'{team.name}: {team.plan}')
  print()
  print()
  run_iters(teams,rounds)

def make_choice():
  '''This is where the opponents choice is made'''
  return random.choice(['a','c','b'])

def run_iters(teams,rounds):
  opponent_history = ''
  score_sheet = {'ab':-500, 'aa':-250, 'ac':-100, 'bb':-250, 'ba':500, 'bc':250, 'cb':-250, 'ca':100, 'cc':0}
  '''This is where the iterations will be executed'''
  for i in range(rounds):
    for team in teams:
      # make choices
      team_choice = team.action(i, opponent_history).lower()
      opponent_choice = make_choice()
      # record choices
      team.player_history += (team_choice)
      opponent_history += (opponent_choice)
      choices = team_choice + opponent_choice
      team.score += score_sheet[choices]
      print(choices)
  score_report(teams)
  
def score_report(teams):
  '''This will make and print the score report'''
  for i in range(10):
    print()
  team_scores = {}
  line = '-' * 50
  logo = text2art("Score Report","isometric3")
  print(logo)
  print(line*3+'----------')
  sleep(2)
  for team in teams:
    team_scores[team] = team.score
  top_3 = sorted(team_scores.items(), key=lambda kv: kv[1], reverse=True)
  ta = text2art("In Third Place","a_zooloo")
  third_place = text2art(f'{top_3[2][0].name} with {top_3[2][1]} points',"bigfig")
  sa = text2art("In Second Place", "a_zooloo")
  second_place = text2art(f'{top_3[1][0].name} with {top_3[1][1]} points',"bigfig")
  fa = text2art("In First Place", "a_zooloo")
  first_place = text2art(f'{top_3[0][0].name} with {top_3[0][1]} points',"bigfig")
  print()
  print(ta)
  sleep(3)
  print(third_place)
  sleep(2)
  print()
  print(sa)
  sleep(4)
  print(second_place)
  sleep(2)
  print()
  print(fa)
  sleep(5)
  print(first_place)
  sleep(10)
  for i in range(40):
    print()
    sleep(.25)  
  print('Final Score Report:')
  for team in teams:
    sleep(.5)
    print(f'{team.name} scored {team.score} points')
  print()
  sleep(1)
  print("Copyright (C) 2020 Patrick Maloney")
