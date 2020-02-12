# PrisonersDilemma

## Team Scripts

- There must be at least 3 teams
- The scripts must follow the layout defined here

```python
name = <Team Name>
plan = <Name of Plan>


def action(iteration,opponent_history):
  ''' This is where the execution of your plan will go. '''
  return <a, c, or b> # this must return an 'a', 'b', or 'c' for admit, betray, or collude, respectively 

```

## Requirements

- [RandCrack](https://pypi.org/project/randcrack/) is not required
- [art](https://pypi.org/project/art/) is required

## Copyright and License

Copyright (C) 2020 Patrick Maloney

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
