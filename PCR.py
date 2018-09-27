#!/usr/bin/env python3

from json import load
from tkinter import *
from tkinter.ttk import *
from tkinter.font import nametofont
from PIL import ImageTk
from PIL import Image
from duration import duration
from sys import exit
from mix import mix


with open('./presets/cycle.json', 'r') as fc:
    cycle = load(fc)

with open('./presets/stock.json', 'r') as fs:
    stock = load(fs)


def callback_float(p):
    """Allow only float values in entries"""
    try:
        p == "" or float(p)
        return True
    except ValueError:
        return False


def callback_int(p):
    """Allow only float values in entries"""
    try:
        p == "" or int(p)
        return True
    except ValueError:
        return False


class Application:
    """Define GUI elements."""
    def __init__(self, master):
        self.default_font = nametofont("TkDefaultFont")
        self.default_font.configure(family="Arial", size=10)
        Style().configure('TCheckbutton', font=('Arial', 8))

        # Define stock variables and initial values
        self.buffer_val = DoubleVar(value=stock['buffer'])
        self.dntps_val = DoubleVar(value=stock['dntps'])
        self.mgcl2_val = DoubleVar(value=stock['mgcl2'])
        self.p1_val = DoubleVar(value=stock['primer1'])
        self.p2_val = DoubleVar(value=stock['primer2'])
        self.p3_val = DoubleVar(value=stock['primer3'])
        self.p4_val = DoubleVar(value=stock['primer4'])
        self.gly_val = DoubleVar(value=stock['gly'])
        self.dmso_val = DoubleVar(value=stock['dmso'])
        self.taq_val = DoubleVar(value=stock['taq'])
        self.dnac_val = DoubleVar(value=stock['dna_c'])

        # Define PRC cycle variables and initial values
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
        self.check_val_stock = IntVar(value=0)
        self.check_val_pcr = IntVar(value=1)

        # Define reaction variables and initial values
        self.buffer_react = DoubleVar(value=1)                      # x (times)
        self.dntps_react = DoubleVar(value=0.2)                     # mM - nmol/uL
        self.mgcl2_react = DoubleVar(value=1.5)                     # mM - nmol/uL
        self.primer1_react = DoubleVar(value=0.2)                   # uM - pmol/uL
        self.primer2_react = DoubleVar(value=0.2)                   # uM - pmol/uL
        self.primer3_react = DoubleVar(value=0)                     # uM - pmol/uL
        self.primer4_react = DoubleVar(value=0)                     # uM - pmol/uL
        self.glycerol_react = DoubleVar(value=0)                    # % (v/v)
        self.dmso_react = DoubleVar(value=0)                        # % (v/v)
        self.taq_react = DoubleVar(value=0.05)                      # U/reaction (units)
        self.dna_mass = DoubleVar(value=5)                          # ng
        self.dna_add = DoubleVar(value=(self.dna_mass.get() /
                                        self.dnac_val.get()))       # uL
        self.volume = DoubleVar(value=12.5)                         # uL
        self.reaction_number = IntVar(value=1)

        # Trace PCR cycle values changes
        self.cb_val.trace_add('write', self.locus_value)
        self.id_val.trace_add('write', self.locus_value)
        self.d_val.trace_add('write', self.locus_value)
        self.anneal_val.trace_add('write', self.locus_value)
        self.exten_val.trace_add('write', self.locus_value)
        self.cycle_val.trace_add('write', self.locus_value)
        self.fexten_val.trace_add('write', self.locus_value)

        vcmd = (master.register(callback_float))
        vcmdi = (master.register(callback_int))

        self.framel = Frame(master, width=375, height=330)
        self.framel.grid(row=0, column=0, sticky="news")
        self.framel.grid_propagate(0)
        self.framer = Frame(master, width=310, height=330)
        self.framer.grid(row=0, column=1, sticky="news")
        self.framer.grid_propagate(0)

        self.stock_lab = Label(self.framel, text="Stock Concentrations", font=("Arial", 10, "bold"))
        self.stock_lab.grid(row=1, column=0, columnspan=3)

        self.buffer_lab = Label(self.framel, text="Buffer:", width=8, anchor=W)
        self.buffer_lab.grid(row=2, column=0, pady=2)
        self.buffer_entry = Entry(self.framel, width=10, justify='right', textvariable=self.buffer_val, validate='all',
                                  validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.buffer_entry.grid(row=2, column=1, pady=2)
        self.buffer_unit = Label(self.framel, text='x', font=("Arial", 8), width=6, anchor=W)
        self.buffer_unit.grid(row=2, column=2, pady=2)

        self.dntps_lab = Label(self.framel, text="DNTPs:", width=8, anchor=W)
        self.dntps_lab.grid(row=3, column=0, pady=2)
        self.dntps_entry = Entry(self.framel, width=10, justify='right', textvariable=self.dntps_val, validate='all',
                                 validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.dntps_entry.grid(row=3, column=1, pady=2)
        self.dntps_unit = Label(self.framel, text='nmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.dntps_unit.grid(row=3, column=2, pady=2)

        self.mgcl2_lab = Label(self.framel, text="MgCl₂:", width=8, anchor=W)
        self.mgcl2_lab.grid(row=4, column=0, pady=2)
        self.mgcl2_entry = Entry(self.framel, width=10, justify='right', textvariable=self.mgcl2_val, validate='all',
                                 validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.mgcl2_entry.grid(row=4, column=1, pady=2)
        self.mgcl2_unit = Label(self.framel, text='nmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.mgcl2_unit.grid(row=4, column=2, pady=2)

        self.p1_lab = Label(self.framel, text="Primer 1:", width=8, anchor=W)
        self.p1_lab.grid(row=5, column=0, pady=2)
        self.p1_entry = Entry(self.framel, width=10, justify='right', textvariable=self.p1_val, validate='all',
                              validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.p1_entry.grid(row=5, column=1, pady=2)
        self.p1_unit = Label(self.framel, text='pmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.p1_unit.grid(row=5, column=2, pady=2)

        self.p2_lab = Label(self.framel, text="Primer 2:", width=8, anchor=W)
        self.p2_lab.grid(row=6, column=0, pady=2)
        self.p2_entry = Entry(self.framel, width=10, justify='right', textvariable=self.p2_val, validate='all',
                              validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.p2_entry.grid(row=6, column=1, pady=2)
        self.p2_unit = Label(self.framel, text='pmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.p2_unit.grid(row=6, column=2, pady=2)

        self.p3_lab = Label(self.framel, text="Primer 3:", width=8, anchor=W)
        self.p3_lab.grid(row=7, column=0, pady=2)
        self.p3_entry = Entry(self.framel, width=10, justify='right', textvariable=self.p3_val, validate='all',
                              validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.p3_entry.grid(row=7, column=1, pady=2)
        self.p3_unit = Label(self.framel, text='pmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.p3_unit.grid(row=7, column=2, pady=2)

        self.p4_lab = Label(self.framel, text="Primer 4:", width=8, anchor=W)
        self.p4_lab.grid(row=8, column=0, pady=2)
        self.p4_entry = Entry(self.framel, width=10, justify='right', textvariable=self.p4_val, validate='all',
                              validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.p4_entry.grid(row=8, column=1, pady=2)
        self.p4_unit = Label(self.framel, text='pmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.p4_unit.grid(row=8, column=2, pady=2)

        self.gly_lab = Label(self.framel, text="Glycerol:", width=8, anchor=W)
        self.gly_lab.grid(row=9, column=0, pady=2)
        self.gly_entry = Entry(self.framel, width=10, justify='right', textvariable=self.gly_val, validate='all',
                               validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.gly_entry.grid(row=9, column=1, pady=2)
        self.gly_unit = Label(self.framel, text='%', font=("Arial", 8), width=6, anchor=W)
        self.gly_unit.grid(row=9, column=2, pady=2)

        self.dmso_lab = Label(self.framel, text="DMSO:", width=8, anchor=W)
        self.dmso_lab.grid(row=10, column=0, pady=2)
        self.dmso_entry = Entry(self.framel, width=10, justify='right', textvariable=self.dmso_val, validate='all',
                                validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.dmso_entry.grid(row=10, column=1, pady=2)
        self.dmso_unit = Label(self.framel, text='%', font=("Arial", 8), width=6, anchor=W)
        self.dmso_unit.grid(row=10, column=2, pady=2)

        self.taq_lab = Label(self.framel, text="Taq:", width=8, anchor=W)
        self.taq_lab.grid(row=11, column=0, pady=2)
        self.taq_entry = Entry(self.framel, width=10, justify='right', textvariable=self.taq_val, validate='all',
                               validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.taq_entry.grid(row=11, column=1, pady=2)
        self.taq_unit = Label(self.framel, text='U/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.taq_unit.grid(row=11, column=2, pady=2)

        self.dnac_lab = Label(self.framel, text="DNA:", width=8, anchor=W)
        self.dnac_lab.grid(row=12, column=0, pady=2)
        self.dnac_entry = Entry(self.framel, width=10, justify='right', textvariable=self.dnac_val, validate='all',
                                validatecommand=(vcmd, '%P'), state=DISABLED, font=("Arial", 10))
        self.dnac_entry.grid(row=12, column=1, pady=2)
        self.dnac_unit = Label(self.framel, text='ng/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.dnac_unit.grid(row=12, column=2, pady=2)

        self.cbs = Checkbutton(self.framel, text="Edit stock values", variable=self.check_val_stock,
                               command=self.stock_radio)
        self.cbs.grid(row=13, column=0, columnspan=3)

        self.separator = Separator(self.framel, orient=VERTICAL).grid(row=2, column=3, rowspan=12, sticky="ns",
                                                                      padx=10, pady=0)

        self.pcr_lab = Label(self.framel, text="PCR Concentrations", font=("Arial", 10, "bold"))
        self.pcr_lab.grid(row=1, column=4, columnspan=3)

        self.buffer_react_lab = Label(self.framel, text="Buffer:", width=8, anchor=W)
        self.buffer_react_lab.grid(row=2, column=4)
        self.buffer_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.buffer_react,
                                        validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.buffer_react_entry.grid(row=2, column=5)
        self.buffer_react_unit = Label(self.framel, text="x", font=("Arial", 8), width=6, anchor=W)
        self.buffer_react_unit.grid(row=2, column=6)

        self.dntps_react_lab = Label(self.framel, text="DNTPs:", width=8, anchor=W)
        self.dntps_react_lab.grid(row=3, column=4)
        self.dntps_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.dntps_react,
                                       validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.dntps_react_entry.grid(row=3, column=5)
        self.dntps_react_unit = Label(self.framel, text='nmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.dntps_react_unit.grid(row=3, column=6)

        self.mgcl2_react_lab = Label(self.framel, text="MgCl₂:", width=8, anchor=W)
        self.mgcl2_react_lab.grid(row=4, column=4)
        self.mgcl2_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.mgcl2_react,
                                       validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.mgcl2_react_entry.grid(row=4, column=5)
        self.mgcl2_react_unit = Label(self.framel, text='nmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.mgcl2_react_unit.grid(row=4, column=6)

        self.p1_react_lab = Label(self.framel, text="Primer 1:", width=8, anchor=W)
        self.p1_react_lab.grid(row=5, column=4)
        self.p1_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.primer1_react,
                                    validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.p1_react_entry.grid(row=5, column=5)
        self.p1_react_unit = Label(self.framel, text='pmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.p1_react_unit.grid(row=5, column=6)

        self.p2_react_lab = Label(self.framel, text="Primer 2:", width=8, anchor=W)
        self.p2_react_lab.grid(row=6, column=4)
        self.p2_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.primer2_react,
                                    validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.p2_react_entry.grid(row=6, column=5)
        self.p2_react_unit = Label(self.framel, text='pmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.p2_react_unit.grid(row=6, column=6)

        self.p3_react_lab = Label(self.framel, text="Primer 3:", width=8, anchor=W)
        self.p3_react_lab.grid(row=7, column=4)
        self.p3_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.primer3_react,
                                    validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.p3_react_entry.grid(row=7, column=5)
        self.p3_react_unit = Label(self.framel, text='pmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.p3_react_unit.grid(row=7, column=6)

        self.p4_react_lab = Label(self.framel, text="Primer 4:", width=8, anchor=W)
        self.p4_react_lab.grid(row=8, column=4)
        self.p4_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.primer4_react,
                                    validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.p4_react_entry.grid(row=8, column=5)
        self.p4_react_unit = Label(self.framel, text='pmol/\u03bcL', font=("Arial", 8), width=6, anchor=W)
        self.p4_react_unit.grid(row=8, column=6)

        self.gly_react_lab = Label(self.framel, text="Glycerol:", width=8, anchor=W)
        self.gly_react_lab.grid(row=9, column=4)
        self.gly_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.glycerol_react,
                                     validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.gly_react_entry.grid(row=9, column=5)
        self.gly_react_unit = Label(self.framel, text='%', font=("Arial", 8), width=6, anchor=W)
        self.gly_react_unit.grid(row=9, column=6)

        self.dmso_react_lab = Label(self.framel, text="DMSO:", width=8, anchor=W)
        self.dmso_react_lab.grid(row=10, column=4)
        self.dmso_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.dmso_react,
                                      validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.dmso_react_entry.grid(row=10, column=5)
        self.dmso_react_unit = Label(self.framel, text='%', font=("Arial", 8), width=6, anchor=W)
        self.dmso_react_unit.grid(row=10, column=6)

        self.taq_react_lab = Label(self.framel, text="Taq:", width=8, anchor=W)
        self.taq_react_lab.grid(row=11, column=4)
        self.taq_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.taq_react,
                                     validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.taq_react_entry.grid(row=11, column=5)
        self.taq_react_unit = Label(self.framel, text='U', font=("Arial", 8), width=6, anchor=W)
        self.taq_react_unit.grid(row=11, column=6)

        self.dna_react_lab = Label(self.framel, text="DNA:", width=8, anchor=W)
        self.dna_react_lab.grid(row=12, column=4)
        self.dna_react_entry = Entry(self.framel, width=7, justify='right', textvariable=self.dna_mass,
                                     validate='all', validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.dna_react_entry.grid(row=12, column=5)
        self.dna_react_unit = Label(self.framel, text='ng', font=("Arial", 8), width=6, anchor=W)
        self.dna_react_unit.grid(row=12, column=6)

        self.cbpcr = Checkbutton(self.framel, text="Edit PCR values", variable=self.check_val_pcr,
                                 command=self.pcr_radio)
        self.cbpcr.grid(row=13, column=4, columnspan=3)

        self.separator1 = Separator(self.framel, orient=VERTICAL).grid(row=1, column=7, rowspan=13, sticky="ns",
                                                                       padx=10, pady=0)

        self.blank = Label(self.framer, text="")
        self.blank.grid(row=7, column=0, columnspan=8)

        self.select = Checkbutton(self.framer, text="Import from model", variable=self.check_val, command=self.cb_radio)
        self.select.grid(row=9, column=0, columnspan=7)

        self.lcb = Label(self.framer, text="Choose a Model:", width=17, anchor=W)
        self.lcb.grid(row=8, column=0)
        self.cb = Combobox(self.framer, textvariable=self.cb_val, values=[k for k in cycle.keys()],
                           font=('Arial', 8))
        self.cb.configure(state=DISABLED, width=25)
        self.cb.grid(row=8, column=1, pady=2, columnspan=7)

        self.cycle_lab = Label(self.framer, text="PCR Cycle", font=("Arial", 10, "bold"))
        self.cycle_lab.grid(row=1, column=0, columnspan=8)

        self.init_denat_lab = Label(self.framer, text="Initial Denaturation:", width=17, anchor=W)
        self.init_denat_lab.grid(row=2, column=0, pady=2)
        self.init_denat_entry = Entry(self.framer, width=4, justify='right', validate='all', textvariable=self.id_val,
                                      validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.init_denat_entry.grid(row=2, column=1, pady=2)
        self.init_denat_time = Label(self.framer, text='s at', font=("Arial", 8))
        self.init_denat_time.grid(row=2, column=2, pady=2)
        self.init_denat_entry2 = Entry(self.framer, width=4, justify='right', validate='all', textvariable=self.id_val2,
                                       validatecommand=(vcmd, '%P'), font=("Arial", 10))
        self.init_denat_entry2.grid(row=2, column=3, pady=2)
        self.init_denat_temp = Label(self.framer, text='\u00b0C', font=("Arial", 8))
        self.init_denat_temp.grid(row=2, column=4, pady=2)

        self.denat_lab = Label(self.framer, text="Denaturation:", width=17, anchor=W)
        self.denat_lab.grid(row=3, column=0, pady=2)
        self.denat_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                 textvariable=self.d_val, font=("Arial", 10))
        self.denat_entry.grid(row=3, column=1, pady=2)
        self.denat_time = Label(self.framer, text='s at', font=("Arial", 8))
        self.denat_time.grid(row=3, column=2, pady=2)
        self.denat_entry2 = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.d_val2, font=("Arial", 10))
        self.denat_entry2.grid(row=3, column=3, pady=2)
        self.denat_temp = Label(self.framer, text='\u00b0C', font=("Arial", 8))
        self.denat_temp.grid(row=3, column=4, pady=2)

        self.anneal_lab = Label(self.framer, text="Annealing:", width=17, anchor=W)
        self.anneal_lab.grid(row=4, column=0, pady=2)
        self.anneal_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.anneal_val, font=("Arial", 10))
        self.anneal_entry.grid(row=4, column=1, pady=2)
        self.anneal_time = Label(self.framer, text='s at', font=("Arial", 8))
        self.anneal_time.grid(row=4, column=2, pady=2)
        self.anneal_entry2 = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                   textvariable=self.anneal_val2, font=("Arial", 10))
        self.anneal_entry2.grid(row=4, column=3, pady=2)
        self.anneal_temp = Label(self.framer, text='\u00b0C', font=("Arial", 8))
        self.anneal_temp.grid(row=4, column=4, pady=2)

        self.cycles_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.cycle_val, font=("Arial", 10))
        self.cycles_entry.grid(row=4, column=6)
        self.cycles_lab = Label(self.framer, text='x')
        self.cycles_lab.grid(row=4, column=7)

        self.exten_lab = Label(self.framer, text="Extension:", width=17, anchor=W)
        self.exten_lab.grid(row=5, column=0, pady=2)
        self.exten_entry = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                 textvariable=self.exten_val, font=("Arial", 10))
        self.exten_entry.grid(row=5, column=1, pady=2)
        self.exten_time = Label(self.framer, text='s at', font=("Arial", 8))
        self.exten_time.grid(row=5, column=2, pady=2)
        self.exten_entry2 = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                  textvariable=self.exten_val2, font=("Arial", 10))
        self.exten_entry2.grid(row=5, column=3, pady=2)
        self.exten_temp = Label(self.framer, text='\u00b0C', font=("Arial", 8))
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
                                  textvariable=self.fexten_val, font=("Arial", 10))
        self.fexten_entry.grid(row=6, column=1, pady=2)
        self.fexten_time = Label(self.framer, text='m at', font=("Arial", 8))
        self.fexten_time.grid(row=6, column=2, pady=2)
        self.fexten_entry2 = Entry(self.framer, width=4, justify='right', validate='all', validatecommand=(vcmd, '%P'),
                                   textvariable=self.fexten_val2, font=("Arial", 10))
        self.fexten_entry2.grid(row=6, column=3, pady=2)
        self.fexten_temp = Label(self.framer, text='\u00b0C', font=("Arial", 8))
        self.fexten_temp.grid(row=6, column=4, pady=2)

        self.duration_lab = Label(self.framer, text="Minimum Run Time:", width=17, anchor=W)
        self.duration_lab.grid(row=10, column=0, pady=2)
        self.duration = Label(self.framer, textvariable=self.total_time, width=17, anchor=W)
        self.duration.grid(row=10, column=1, columnspan=7)

        self.separator2 = Separator(self.framer, orient=HORIZONTAL).grid(row=11, column=0, columnspan=8, padx=0,
                                                                         pady=2, sticky="ew")

        self.react_num_lab = Label(self.framer, text="PCR Reactions Number:", width=22, anchor=W)
        self.react_num_lab.grid(row=13, column=0, columnspan=2)
        self.react_num_entry = Entry(self.framer, width=15, justify='right', validate='all',
                                     validatecommand=(vcmdi, '%P'), textvariable=self.reaction_number,
                                     font=("Arial", 10))
        self.react_num_entry.grid(row=13, column=2, columnspan=5, pady=(1, 5))

        self.react_vol_lab = Label(self.framer, text="Reaction Volume:", width=22, anchor=W)
        self.react_vol_lab.grid(row=12, column=0, columnspan=2)
        self.react_vol_entry = Entry(self.framer, width=15, justify='right', validate='all',
                                     validatecommand=(vcmd, '%P'), textvariable=self.volume, font=("Arial", 10))
        self.react_vol_entry.grid(row=12, column=2, columnspan=5)
        self.react_vol_unit = Label(self.framer, text='\u03bcL', font=("Arial", 8), width=2, anchor=W)
        self.react_vol_unit.grid(row=12, column=7)

        self.button = Button(self.framer, text="View Mix", command=lambda: mix(self))
        self.button.grid(row=14, column=0, columnspan=2)

        self.exit = Button(self.framer, text="Close", command=exit)
        self.exit.grid(row=14, column=2, columnspan=5)

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
        Verify the Checkbutton variable values and handles combobox entry state accordingly.
        """
        if self.check_val.get() == 0:
            self.cb.configure(state=DISABLED)
        else:
            self.cb.configure(state="readonly")

    def stock_radio(self):
        """
        Verify the Checkbutton variable values and handles stock entries accordingly.
        """
        if self.check_val_stock.get() == 0:
            self.buffer_entry.configure(state=DISABLED)
            self.dntps_entry.configure(state=DISABLED)
            self.mgcl2_entry.configure(state=DISABLED)
            self.p1_entry.configure(state=DISABLED)
            self.p2_entry.configure(state=DISABLED)
            self.p3_entry.configure(state=DISABLED)
            self.p4_entry.configure(state=DISABLED)
            self.gly_entry.configure(state=DISABLED)
            self.dmso_entry.configure(state=DISABLED)
            self.taq_entry.configure(state=DISABLED)
            self.dnac_entry.configure(state=DISABLED)
        else:
            self.buffer_entry.configure(state=NORMAL)
            self.dntps_entry.configure(state=NORMAL)
            self.mgcl2_entry.configure(state=NORMAL)
            self.p1_entry.configure(state=NORMAL)
            self.p2_entry.configure(state=NORMAL)
            self.p3_entry.configure(state=NORMAL)
            self.p4_entry.configure(state=NORMAL)
            self.gly_entry.configure(state=NORMAL)
            self.dmso_entry.configure(state=NORMAL)
            self.taq_entry.configure(state=NORMAL)
            self.dnac_entry.configure(state=NORMAL)

    def pcr_radio(self):
        """
        Verify the Checkbutton variable values and handles stock entries accordingly.
        """
        if self.check_val_pcr.get() == 0:
            self.buffer_react_entry.configure(state=DISABLED)
            self.dntps_react_entry.configure(state=DISABLED)
            self.mgcl2_react_entry.configure(state=DISABLED)
            self.p1_react_entry.configure(state=DISABLED)
            self.p2_react_entry.configure(state=DISABLED)
            self.p3_react_entry.configure(state=DISABLED)
            self.p4_react_entry.configure(state=DISABLED)
            self.gly_react_entry.configure(state=DISABLED)
            self.dmso_react_entry.configure(state=DISABLED)
            self.taq_react_entry.configure(state=DISABLED)
            self.dna_react_entry.configure(state=DISABLED)
        else:
            self.buffer_react_entry.configure(state=NORMAL)
            self.dntps_react_entry.configure(state=NORMAL)
            self.mgcl2_react_entry.configure(state=NORMAL)
            self.p1_react_entry.configure(state=NORMAL)
            self.p2_react_entry.configure(state=NORMAL)
            self.p3_react_entry.configure(state=NORMAL)
            self.p4_react_entry.configure(state=NORMAL)
            self.gly_react_entry.configure(state=NORMAL)
            self.dmso_react_entry.configure(state=NORMAL)
            self.taq_react_entry.configure(state=NORMAL)
            self.dna_react_entry.configure(state=NORMAL)
