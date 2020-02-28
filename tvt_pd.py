"""
Copyright (C) 2020 Patrick Maloney

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
"""

import nt1, nt2, nt3, nt4
from importlib import reload
from time import sleep
from uuid import uuid4

teams = [nt1, nt2, nt3, nt4]


def start(teams, rounds):
    '''This starts the program'''
    names = []
    init_str = ''
    for team in teams:
        reload(team)
        init_str += f'reloaded {team}\n'
        print('reloaded', team)
        if not hasattr(team, 'plan'):
            init_str += f'{team} is missing attribute: plan\n'
            setattr(team, 'plan', 'missing assignment')
            print(f'{team} is missing attribute: plan')
        if not hasattr(team, 'name'):
            rename = uuid4()
            init_str += f'\n\nWARNING:\nMissing team name in module {team}\nReplacing name with UUID:\n{rename}\n\n'
            print(
                f'\n\nWARNING:\nMissing team name in module {team}\nReplacing name with UUID:\n{rename}\n\n'
            )
            setattr(team, 'name', rename)
        setattr(team, 'score', 0)
        if team.name in names:
            rename = uuid4()
            init_str += f'\n\nWARNING:\nInvalid team name in module {team}: {team.name}\nReplacing name with UUID:\n{rename}\n\nPlease avoid duplicate names\n\n'
            print(
                f'\n\nWARNING:\nInvalid team name in module {team}: {team.name}\nReplacing name with UUID:\n{rename}\n\nPlease avoid duplicate names\n\n'
            )
            setattr(team, 'name', rename)
        names.append(team.name)
    sleep(5)
    init_str += f'There are {len(teams)} team(s)\nAnd those teams and their plans are: \n\n'
    print(
        f'There are {len(teams)} team(s)\nAnd those teams and their plans are: \n\n'
    )
    for team in teams:
        init_str += f'{team.name}: {team.plan}'
        print(f'{team.name}: {team.plan}')
    init_str += '\n\n'
    print('\n\n')
    sleep(5)
    with open('init.txt', 'w') as outfile:
        outfile.writelines(init_str)
        outfile.close()
    run_iters(teams, rounds)


def run_iters(teams, rounds):
    score_sheet = {
        'ab': -500,
        'aa': -250,
        'ac': -100,
        'bb': -250,
        'ba': 500,
        'bc': 250,
        'cb': -250,
        'ca': 100,
        'cc': 0
    }
    scores = {}
    '''This is where the iterations will be executed'''
    for team in teams:
        opponents = [opp for opp in teams if opp != team]
        scores[team] = {}
        for opponent in opponents:
            opponent_history = ''
            team_history = ''
            for round in range(rounds):
              team_error = False
              opp_error = False
              team_choice = team.action(round, opponent_history)
              opponent_choice = opponent.action(round, team_history)
              scorer = team_choice + opponent_choice
              team_history += team_choice
              opponent_history += opponent_choice
              if team_choice not in ('a', 'c', 'b'):
                print('team error')
                team_error = True
                team.score += -250
              if opponent_choice not in ('a', 'c', 'b'):
                print('opp error')
                opp_error = True
                team.score += 250
              if not team_error:
                if not opp_error:
                    team.score += score_sheet[scorer]
            scores[team][opponent] = team.score
            setattr(team, 'score', 0)
    score_report(teams, scores)


# TODO: Redo score_report
# score_report needs to be redone because it is not optimized for Team vs teams
# Changes will need to be made to run_iters for proper score reportage
def score_report(teams, scores):
    '''This will make and print the score report'''
    sr_str = ''
    for team in teams:
      sr_str += f'{team.name} from module {team}\n----\n\n'
    sr_str += '\n\n'
    for team in teams:
      sr_str += f'{team.name}\n'
      sr_str += '-----'*4
      opps = [opp for opp in teams if opp != team]
      for opp in opps:
        sr_str += f'\n{team.name} - {opp.name}:\n'
        sr_str += f'{scores[team][opp]}\n'
      sr_str += '-----'*4
      sr_str += '\n\n'
    with open('report.txt','w') as outfile:
      outfile.writelines(sr_str)
    print("Copyright (C) 2020 Patrick Maloney\n")
