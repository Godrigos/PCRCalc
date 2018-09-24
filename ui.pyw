#!/usr/bin/env python3

"""
This file is part of PCRCalc.

PCRCalc is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PCRCalc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PCRCalc.  If not, see <https://www.gnu.org/licenses/>.

Copyright 2018 Rodrigo Aluizio
"""

from tkinter import *
from ttkthemes import ThemedStyle
from PCR import Application


root = Tk()
root.geometry('700x480')
root.resizable(width=False, height=False)
root.title("PCR Calculator")
style = ThemedStyle(root)
style.set_theme("clearlooks") # Windows version should use "vista" for a more native experience
Application(root)
root.mainloop()
