#!/usr/bin/env python3

from json import load
from tkinter import *
from tkinter.ttk import *
from tkinter.font import nametofont

with open('./presets/cycle.json', 'r') as fc:
    cycle = load(fc)

with open('./presets/stock.json', 'r') as fs:
    stock = load(fs)


class Application:

    def __init__(self, master):
        master = master
        self.default_font = nametofont("TkDefaultFont")
        self.default_font.configure(family="Helvetica", size=10)

        self.frame = Frame(width=720, height=480)
        self.frame.place(relx=0, rely=0)

        self.lom = Label(master, text="Select:")
        self.lom.grid(row=1, column=0)
        self.om = Combobox(master, values=[k for k in cycle.keys()])
        self.om.configure(width=10, state="readonly")
        self.om.grid(row=1, column=1)


class Cycle:
    """Define the reaction cycle: number, temperatures, time and methods."""
    locus = cycle['ITS']

    def __init__(self, init_denat=locus['Initial Denaturation']['s'], denat=locus['Denaturation']['s'],
                 anneal=locus['Annealing']['s'], exten=locus['Extension']['s'], cycle_num=locus['Number of Cycles'],
                 final_exten=locus['Final Extension']['m'], hold=locus['Hold']['s']):
        self.initial_denaturation = init_denat  # seconds and Celsius
        self.denaturation = denat  # seconds and Celsius
        self.annealing = anneal  # seconds and Celsius
        self.extension = exten  # seconds and Celsius
        self.cycles_number = cycle_num  # integer
        self.final_extension = final_exten*60  # minutes (converted to seconds) and Celsius
        self.hold = hold  # infinite at 4 C

    def duration(self):
        """Sum and return the minimum total time expected for PCR cycle."""
        total_sec = (self.initial_denaturation +
                     self.cycles_number * (self.denaturation +
                                           self.annealing +
                                           self.extension) +
                     self.final_extension)
        total_min = total_sec // 60
        total_hours = total_min // 60
        total_time = (str(total_hours) + 'h ' + "%02d" % (total_min % 60) + 'm ' + "%02d" % (total_sec % 60) + 's')
        return total_time


class Stock:
    """Define stock concentration of reagents to be used with PCR reaction."""
    def __init__(self, buffer=stock['buffer'], dntps=stock['dntps'], mgcl2=stock['mgcl2'], p1=stock['p1'],
                 p2=stock['p2'], p3=stock['p3'], p4=stock['p4'], gly=stock['gly'], dmso=stock['dmso'], taq=stock['taq'],
                 dna_c=stock['dna_c']):
        """Initialize stock values of PCR reagents."""
        self.buffer = buffer  # x (times)
        self.dntps = dntps    # mM - nmol/uL
        self.mgcl2 = mgcl2    # mM - nmol/uL
        self.primer1 = p1     # uM - pmol/uL
        self.primer2 = p2     # uM - pmol/uL
        self.primer3 = p3     # uM - pmol/uL
        self.primer4 = p4     # uM - pmol/uL
        self.glycerol = gly   # % (v/v)
        self.dmso = dmso      # % (v/v)
        self.taq = taq        # U/uL (units)
        self.dna_concentration = dna_c  # ng/uL


class Reaction:
    """Define the reaction reagents, quantities and methods."""
    def __init__(self, buffer=1, dntps=0.2, mgcl2=1.5, p1=0.2, p2=0.2, p3=0, p4=0, h2o=5, taq=0.05, dna_m=5, react_n=1,
                 gly=0, dmso=0, vol=12.5):
        """Initialize reagents and parameters of a standard PCR reaction."""
        self.buffer = buffer  # x (times)
        self.dntps = dntps    # mM - nmol/uL
        self.mgcl2 = mgcl2    # mM - nmol/uL
        self.primer1 = p1     # uM - pmol/uL
        self.primer2 = p2     # uM - pmol/uL
        self.primer3 = p3     # uM - pmol/uL
        self.primer4 = p4     # uM - pmol/uL
        self.h2o = h2o  # uL
        self.glycerol = gly  # % (v/v)
        self.dmso = dmso  # % (v/v)
        self.taq = taq  # U/reaction (units)
        self.dna_mass = dna_m  # ng
        self.dna_add = (self.dna_mass / Stock().dna_concentration)  # uL
        self.volume = vol  # uL
        self.reaction_number = react_n  # integer

    def mix(self):
        """Calculate reagent mix volumes."""
        self.buffer = ((self.buffer * self.volume) / Stock().buffer)
        self.dntps = ((self.dntps * self.volume) / Stock().dntps)
        self.mgcl2 = ((self.mgcl2 * self.volume) / Stock().mgcl2)
        self.primer1 = ((self.primer1 * self.volume) / Stock().primer1)
        self.primer2 = ((self.primer2 * self.volume) / Stock().primer2)
        self.primer3 = ((self.primer3 * self.volume) / Stock().primer3)
        self.primer4 = ((self.primer4 * self.volume) / Stock().primer4)
        self.taq = ((self.taq / Stock().taq) * self.volume)
        self.glycerol = (self.volume * (self.glycerol / 100))
        self.dmso = (self.volume * (self.dmso / 100))
        self.h2o = (self.volume - self.buffer - self.dntps - self.mgcl2 - self.primer1 - self.primer2 - self.primer3 -
                    self.primer4 - self.taq - self.dna_add - self.glycerol - self.dmso)
        mix_volume = (self.buffer + self.dntps + self.mgcl2 + self.primer1 + self.primer2 + self.primer3 +
                      self.primer4 + self.taq + self.glycerol + self.dmso + self.h2o)

        mix = {'Buffer': self.buffer, 'DNTPs': self.dntps, 'MgCl₂': self.mgcl2, 'Primer 1': self.primer1,
               'Primer 2': self.primer2, 'Primer 3': self.primer3, 'Primer 4': self.primer4, 'Taq': self.taq,
               'Glycerol': self.glycerol, 'DMSO': self.dmso, 'H₂O': self.h2o, 'Mix Total': mix_volume}

        for value in mix:
            mix[value] *= self.reaction_number

        for key, value in mix.items():
            print(key + ": " + str(value) + " uL")
        print("Each sample DNA: " + str(self.dna_add) + " uL")
