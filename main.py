"""
Copyright (C) 2020 Patrick Maloney

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
"""

import new_pd, tvt_pd
import nt1, nt2, nt3,nt4

# new_pd.start(<list of teams>, <Number of iterations>) to run the game
tvt = True
if tvt:
	tvt_pd.start([nt1, nt2, nt3, nt4], 100)
else:
	new_pd.start([nt1, nt2, nt3, nt4], 100)