#    Heritage for the future visual novel, game based off of hftf community
#    Copyright (C) <2018>  <Devboys>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

label start:
    call prologue from _call_prologue
    call chapter1 from _call_chapter1
    call chapter2 from _call_chapter2
    return

label splashscreen:

    $ renpy.movie_cutscene('jahintro.mpeg')
    hide movie_cutscene
    return
