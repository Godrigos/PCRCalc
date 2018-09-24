#!/usr/bin/env python3

from json import load
from tkinter import *
from tkinter.ttk import *
from tkinter.font import nametofont
from PIL import ImageTk
from PIL import Image
from duration import duration


with open('./presets/cycle.json', 'r') as fc:
    cycle = load(fc)

with open('./presets/stock.json', 'r') as fs:
    stock = load(fs)


def callback(p):
    try:
        p == "" or float(p)
        return True
    except ValueError:
        return False


class Application:
    """Define GUI elements."""
    def __init__(self, master):
        self.default_font = nametofont("TkDefaultFont")
        self.default_font.configure(family="Helvetica", size=10)
        self.cb_font = Style()
        self.cb_font.configure('TCheckbutton', font=('Helvetica', 8))

        self.cb_val = StringVar(value="")
        self.fexten_val = DoubleVar(value=0)
        self.fexten_val2 = DoubleVar(value=0)
        self.id_val = DoubleVar(value=0)
        self.id_val2 = DoubleVar(value=0)
        self.d_val = DoubleVar(value=0)
        self.d_val2 = DoubleVar(value=0)
        self.anneal_val = DoubleVar(value=0)
        self.anneal_val2 = DoubleVar(value=0)
        self.exten_val = DoubleVar(value=0)
        self.exten_val2 = DoubleVar(value=0)
        self.cycle_val = DoubleVar(value=0)
        self.total_time = StringVar(value='0h 00m 00s')
        self.check_val = IntVar(value=0)

        self.cb_val.trace_add('write', self.locus_value)
        self.id_val.trace_add('write', self.locus_value)
        self.d_val.trace_add('write', self.locus_value)
        self.anneal_val.trace_add('write', self.locus_value)
        self.exten_val.trace_add('write', self.locus_value)
        self.cycle_val.trace_add('write', self.locus_value)
        self.fexten_val.trace_add('write', self.locus_value)

        vcmd = (master.register(callback))

        self.framel = Frame(master, width=375, height=480)
        self.framel.grid(row=0, column=0, sticky="news")
        self.framel.grid_propagate(0)
        self.framer = Frame(master, width=325, height=480)
        self.framer.grid(row=0, column=1, sticky="news")
        self.framer.grid_propagate(0)

        self.stock_lab = Label(self.framel, text="Stock Concentrations", font=("Helvetica", 10, "bold"))
        self.stock_lab.grid(row=1, column=0, columnspan=3)

        self.buffer_lab = Label(self.framel, text="Buffer:", width=8, anchor=W)
        self.buffer_lab.grid(row=2, column=0, pady=2)
        self.buffer_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.buffer_entry.insert(END, stock['buffer'])
        self.buffer_entry.grid(row=2, column=1, pady=2)
        self.buffer_unit = Label(self.framel, text='x', font=("Helvetica", 8))
        self.buffer_unit.grid(row=2, column=2, pady=2)

        self.dntps_lab = Label(self.framel, text="DNTPs:", width=8, anchor=W)
        self.dntps_lab.grid(row=3, column=0, pady=2)
        self.dntps_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.dntps_entry.insert(END, stock['dntps'])
        self.dntps_entry.grid(row=3, column=1, pady=2)
        self.dntps_unit = Label(self.framel, text='mM', font=("Helvetica", 8))
        self.dntps_unit.grid(row=3, column=2, pady=2)

        self.mgcl2_lab = Label(self.framel, text="MgCl₂:", width=8, anchor=W)
        self.mgcl2_lab.grid(row=4, column=0, pady=2)
        self.mgcl2_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.mgcl2_entry.insert(END, stock['mgcl2'])
        self.mgcl2_entry.grid(row=4, column=1, pady=2)
        self.mgcl2_unit = Label(self.framel, text='mM', font=("Helvetica", 8))
        self.mgcl2_unit.grid(row=4, column=2, pady=2)

        self.p1_lab = Label(self.framel, text="Primer 1:", width=8, anchor=W)
        self.p1_lab.grid(row=5, column=0, pady=2)
        self.p1_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.p1_entry.insert(END, stock['p1'])
        self.p1_entry.grid(row=5, column=1, pady=2)
        self.p1_unit = Label(self.framel, text='\u03bcM', font=("Helvetica", 8))
        self.p1_unit.grid(row=5, column=2, pady=2)

        self.p2_lab = Label(self.framel, text="Primer 2:", width=8, anchor=W)
        self.p2_lab.grid(row=6, column=0, pady=2)
        self.p2_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.p2_entry.insert(END, stock['p2'])
        self.p2_entry.grid(row=6, column=1, pady=2)
        self.p2_unit = Label(self.framel, text='\u03bcM', font=("Helvetica", 8))
        self.p2_unit.grid(row=6, column=2, pady=2)

        self.p3_lab = Label(self.framel, text="Primer 3:", width=8, anchor=W)
        self.p3_lab.grid(row=7, column=0, pady=2)
        self.p3_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.p3_entry.insert(END, stock['p3'])
        self.p3_entry.grid(row=7, column=1, pady=2)
        self.p3_unit = Label(self.framel, text='\u03bcM', font=("Helvetica", 8))
        self.p3_unit.grid(row=7, column=2, pady=2)

        self.p4_lab = Label(self.framel, text="Primer 4:", width=8, anchor=W)
        self.p4_lab.grid(row=8, column=0, pady=2)
        self.p4_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.p4_entry.insert(END, stock['p4'])
        self.p4_entry.grid(row=8, column=1, pady=2)
        self.p4_unit = Label(self.framel, text='\u03bcM', font=("Helvetica", 8))
        self.p4_unit.grid(row=8, column=2, pady=2)

        self.gly_lab = Label(self.framel, text="Glycerol:", width=8, anchor=W)
        self.gly_lab.grid(row=9, column=0, pady=2)
        self.gly_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.gly_entry.insert(END, stock['gly'])
        self.gly_entry.grid(row=9, column=1, pady=2)
        self.gly_unit = Label(self.framel, text='%', font=("Helvetica", 8))
        self.gly_unit.grid(row=9, column=2, pady=2)

        self.dmso_lab = Label(self.framel, text="DMSO:", width=8, anchor=W)
        self.dmso_lab.grid(row=10, column=0, pady=2)
        self.dmso_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.dmso_entry.insert(END, stock['dmso'])
        self.dmso_entry.grid(row=10, column=1, pady=2)
        self.dmso_unit = Label(self.framel, text='%', font=("Helvetica", 8))
        self.dmso_unit.grid(row=10, column=2, pady=2)

        self.taq_lab = Label(self.framel, text="Taq:", width=8, anchor=W)
        self.taq_lab.grid(row=11, column=0, pady=2)
        self.taq_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.taq_entry.insert(END, stock['taq'])
        self.taq_entry.grid(row=11, column=1, pady=2)
        self.taq_unit = Label(self.framel, text='U/\u03bcL', font=("Helvetica", 8), anchor=W)
        self.taq_unit.grid(row=11, column=2, pady=2)

        self.dnac_lab = Label(self.framel, text="DNA:", width=8, anchor=W)
        self.dnac_lab.grid(row=12, column=0, pady=2)
        self.dnac_entry = Entry(self.framel, width=10, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.dnac_entry.insert(END, stock['dna_c'])
        self.dnac_entry.grid(row=12, column=1, pady=2)
        self.dnac_unit = Label(self.framel, text='ng/\u03bcL', font=("Helvetica", 8), anchor=W)
        self.dnac_unit.grid(row=12, column=2, pady=2)

        self.separator = Separator(self.framel, orient=VERTICAL).grid(row=2, column=3, rowspan=11, sticky="ns",
                                                                      padx=5)

        self.mix_lab = Label(self.framel, text="PCR Mix", font=("Helvetica", 10, "bold"))
        self.mix_lab.grid(row=1, column=3, columnspan=3)
        self.mix_num_lab = Label(self.framel, text="Reactions:")
        self.mix_num_lab.grid(row=2, column=4)
        self.mix_num = Entry(self.framel, width=12, justify='right', validate='all', validatecommand=(vcmd, '%P'))
        self.mix_num.insert(END, 1)
        self.mix_num.grid(row=2, column=5)

        self.separator = Separator(self.framel, orient=VERTICAL).grid(row=1, column=6, rowspan=12, sticky="ns",
                                                                      padx=5)

        self.blank = Label(self.framer, text="")
        self.blank.grid(row=7, column=0, columnspan=7)

        self.select = Checkbutton(self.framer, text="Import from model", variable=self.check_val, command=self.cb_radio)
        self.select.grid(row=9, column=0, columnspan=7)

        self.lcb = Label(self.framer, text="Choose a Model:", width=17, anchor=W)
        self.lcb.grid(row=8, column=0)
        self.cb = Combobox(self.framer, textvariable=self.cb_val, values=[k for k in cycle.keys()])
        self.cb.configure(state=DISABLED, width=20)
        self.cb.grid(row=8, column=1, pady=2, columnspan=7)

        self.cycle_lab = Label(self.framer, text="PCR Cycle", font=("Helvetica", 10, "bold"))
        self.cycle_lab.grid(row=1, column=0, columnspan=8)

        self.init_denat_lab = Label(self.framer, text="Initial Denaturation:", width=17, anchor=W)
        self.init_denat_lab.grid(row=2, column=0, pady=2)
        self.init_denat_entry = Entry(self.framer, width=4, justify='right', validate='all', textvariable=self.id_val,
                                      validatecommand=(vcmd, '%P'))
        self.init_denat_entry.grid(row=2, column=1, pady=2)
        self.init_denat_time = Label(self.framer, text='s at', font=("Helvetica", 8))
        self.init_denat_time.grid(row=2, column=2, pady=2)
        self.init_denat_entry2 = Entry(self.framer, width=4, justify='right', validate='all', textvariable=self.id_val2,
                                       validatecommand=(vcmd, '%P'))
        self.init_denat_entry2.grid(row=2, column=3, pady=2)
        self.init_denat_temp = Label(self.framer, text='\u00b0C', font=("Helvetica", 8))
        self.init_denat_temp.grid(row=2, column=4, pady=2)

        self.denat_lab = Label(self.framer, text="Denaturation:", width=17, anchor=W)
        self.denat_lab.grid(row=3, column=0, pady=2)
        self.denat_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                 textvariable=self.d_val)
        self.denat_entry.grid(row=3, column=1, pady=2)
        self.denat_time = Label(self.framer, text='s at', font=("Helvetica", 8))
        self.denat_time.grid(row=3, column=2, pady=2)
        self.denat_entry2 = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.d_val2)
        self.denat_entry2.grid(row=3, column=3, pady=2)
        self.denat_temp = Label(self.framer, text='\u00b0C', font=("Helvetica", 8))
        self.denat_temp.grid(row=3, column=4, pady=2)

        self.anneal_lab = Label(self.framer, text="Annealing:", width=17, anchor=W)
        self.anneal_lab.grid(row=4, column=0, pady=2)
        self.anneal_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.anneal_val)
        self.anneal_entry.grid(row=4, column=1, pady=2)
        self.anneal_time = Label(self.framer, text='s at', font=("Helvetica", 8))
        self.anneal_time.grid(row=4, column=2, pady=2)
        self.anneal_entry2 = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                   textvariable=self.anneal_val2)
        self.anneal_entry2.grid(row=4, column=3, pady=2)
        self.anneal_temp = Label(self.framer, text='\u00b0C', font=("Helvetica", 8))
        self.anneal_temp.grid(row=4, column=4, pady=2)

        self.cycles_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.cycle_val)
        self.cycles_entry.grid(row=4, column=6)
        self.cycles_lab = Label(self.framer, text='x')
        self.cycles_lab.grid(row=4, column=7)

        self.exten_lab = Label(self.framer, text="Extension:", width=17, anchor=W)
        self.exten_lab.grid(row=5, column=0, pady=2)
        self.exten_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                 textvariable=self.exten_val)
        self.exten_entry.grid(row=5, column=1, pady=2)
        self.exten_time = Label(self.framer, text='s at', font=("Helvetica", 8))
        self.exten_time.grid(row=5, column=2, pady=2)
        self.exten_entry2 = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.exten_val2)
        self.exten_entry2.grid(row=5, column=3, pady=2)
        self.exten_temp = Label(self.framer, text='\u00b0C', font=("Helvetica", 8))
        self.exten_temp.grid(row=5, column=4, pady=2)

        img = Image.open("./images/brace.png")
        img = img.resize((20, 75), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.brackets = Label(self.framer, image=img)
        self.brackets.image = img
        self.brackets.grid(row=3, column=5, rowspan=3)

        self.fexten_lab = Label(self.framer, text="Final Extension:", width=17, anchor=W)
        self.fexten_lab.grid(row=6, column=0, pady=2)
        self.fexten_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.fexten_val)
        self.fexten_entry.grid(row=6, column=1, pady=2)
        self.fexten_time = Label(self.framer, text='m at', font=("Helvetica", 8))
        self.fexten_time.grid(row=6, column=2, pady=2)
        self.fexten_entry2 = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                   textvariable=self.fexten_val2)
        self.fexten_entry2.grid(row=6, column=3, pady=2)
        self.fexten_temp = Label(self.framer, text='\u00b0C', font=("Helvetica", 8))
        self.fexten_temp.grid(row=6, column=4, pady=2)

        self.duration_lab = Label(self.framer, text="Minimum Run Time:", width=17, anchor=W)
        self.duration_lab.grid(row=10, column=0, pady=2)
        self.duration = Label(self.framer, textvariable=self.total_time, width=17, anchor=W)
        self.duration.grid(row=10, column=1, columnspan=7)

    def locus_value(self, *args):
        if self.check_val.get() == 1:
            data = cycle[self.cb_val.get()]
            self.fexten_val.set(data['Final Extension']['m'])
            self.fexten_val2.set(data['Final Extension']['C'])
            self.id_val.set(data['Initial Denaturation']['s'])
            self.id_val2.set(data['Initial Denaturation']['C'])
            self.d_val.set(data['Denaturation']['s'])
            self.d_val2.set(data['Denaturation']['C'])
            self.anneal_val.set(data['Annealing']['s'])
            self.anneal_val2.set(data['Annealing']['C'])
            self.exten_val.set(data['Extension']['s'])
            self.exten_val2.set(data['Extension']['C'])
            self.cycle_val.set(data['Number of Cycles'])
            self.total_time.set(duration(self))
        else:
            self.id_val.set(self.init_denat_entry.get())
            self.d_val.set(self.denat_entry.get())
            self.anneal_val.set(self.anneal_entry.get())
            self.exten_val.set(self.exten_entry.get())
            self.cycle_val.set(self.cycles_entry.get())
            self.fexten_val.set(self.fexten_entry.get())
            self.total_time.set(duration(self))
        for arg in args:
            del arg

    def cb_radio(self):
        """
        Verify the Checkbutton variable values and handles server_url entry state accordingly.
            """
        if self.check_val.get() == 0:
            self.cb.configure(state=DISABLED)
        else:
            self.cb.configure(state="readonly")


class Cycle:
    locus = {
        "Initial Denaturation": {"s": 0, "C": 0},
        "Denaturation": {"s": 0, "C": 0},
        "Annealing": {"s": 0, "C": 0},
        "Extension": {"s": 0, "C": 0},
        "Number of Cycles": 0,
        "Final Extension": {"m": 0, "C": 0},
        "Hold": {"s": "Forever", "C": 4}
    }
    """Define the reaction cycle: number, temperatures, time and methods."""
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
