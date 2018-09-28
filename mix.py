from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk
from PIL import Image
from report import report
from tkinter.messagebox import showwarning


def mix(self):
    """Calculate reagent mix volumes."""
    buffer = ((float(self.buffer_react_entry.get()) * float(self.react_vol_entry.get())) /
              float(self.buffer_entry.get()))
    dntps = ((float(self.dntps_react_entry.get()) * float(self.react_vol_entry.get())) / float(self.dntps_entry.get()))
    mgcl2 = ((float(self.mgcl2_react_entry.get()) * float(self.react_vol_entry.get())) / float(self.mgcl2_entry.get()))
    primer1 = ((float(self.p1_react_entry.get()) * float(self.react_vol_entry.get())) / float(self.p1_entry.get()))
    primer2 = ((float(self.p2_react_entry.get()) * float(self.react_vol_entry.get())) / float(self.p2_entry.get()))
    primer3 = ((float(self.p3_react_entry.get()) * float(self.react_vol_entry.get())) / float(self.p3_entry.get()))
    primer4 = ((float(self.p4_react_entry.get()) * float(self.react_vol_entry.get())) / float(self.p4_entry.get()))
    taq = ((float(self.taq_react_entry.get()) / float(self.taq_entry.get())) * float(self.react_vol_entry.get()))
    glycerol = (float(self.react_vol_entry.get()) * (float(self.gly_react_entry.get()) / float(self.gly_entry.get())))
    dmso = (float(self.react_vol_entry.get()) * (float(self.dmso_react_entry.get()) / float(self.dmso_entry.get())))
    self.dna_add = (float(self.dna_mass.get()) / float(self.dnac_entry.get()))
    h2o = (float(self.react_vol_entry.get()) - buffer - dntps - mgcl2 - primer1 - primer2 - primer3 - primer4 - taq -
           self.dna_add - glycerol - dmso)
    mix_volume = (buffer + dntps + mgcl2 + primer1 + primer2 + primer3 + primer4 + taq + glycerol + dmso + h2o)

    if h2o < 0:
        showwarning("Wrong values!", "Your PCR concentrations have values that are not possible to acheive in the mix!")
    else:
        self.final_mix = {'Buffer': buffer, 'DNTPs': dntps, 'MgCl2': mgcl2, 'Primer 1': primer1, 'Primer 2': primer2,
                          'Primer 3': primer3, 'Primer 4': primer4, 'Taq': taq, 'Glycerol': glycerol, 'DMSO': dmso,
                          'H2O': h2o, 'Mix Total': mix_volume}

        for value in self.final_mix:
            self.final_mix[value] *= float(self.react_num_entry.get())

        self.window = Toplevel(master=None)
        self.window.resizable(width=False, height=False)
        self.window.title("PCR Mix")

        frame = Frame(self.window)
        frame.grid(row=0, column=0, sticky="news")
        frame.grid_propagate(1)

        mix_lab = Label(frame, text=f"{self.react_num_entry.get()} reactions need:")
        mix_lab.grid(row=0, column=0, columnspan=3)

        buf_lab = Label(frame, text="Buffer:", width=8, anchor=W)
        buf_lab.grid(row=1, column=0)
        buf_lab_val = Label(frame, text=f" {round(self.final_mix['Buffer'], 3)} ", width=6, anchor=E)
        buf_lab_val.grid(row=1, column=1)
        buf_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        buf_lab_unit.grid(row=1, column=2)

        dntps_lab = Label(frame, text="DNTPs:", width=8, anchor=W)
        dntps_lab.grid(row=2, column=0)
        dntps_lab_val = Label(frame, text=f" {round(self.final_mix['DNTPs'], 3)} ", width=6, anchor=E)
        dntps_lab_val.grid(row=2, column=1)
        dntps_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        dntps_lab_unit.grid(row=2, column=2)

        mgcl2_lab = Label(frame, text="MgCl₂:", width=8, anchor=W)
        mgcl2_lab.grid(row=3, column=0)
        mgcl2_lab_val = Label(frame, text=f" {round(self.final_mix['MgCl2'], 3)} ", width=6, anchor=E)
        mgcl2_lab_val.grid(row=3, column=1)
        mgcl2_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        mgcl2_lab_unit.grid(row=3, column=2)

        p1_lab = Label(frame, text="Primer 1:", width=8, anchor=W)
        p1_lab.grid(row=4, column=0)
        p1_lab_val = Label(frame, text=f" {round(self.final_mix['Primer 1'], 3)} ", width=6, anchor=E)
        p1_lab_val.grid(row=4, column=1)
        p1_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        p1_lab_unit.grid(row=4, column=2)

        p2_lab = Label(frame, text="Primer 2:", width=8, anchor=W)
        p2_lab.grid(row=5, column=0)
        p2_lab_val = Label(frame, text=f" {round(self.final_mix['Primer 2'], 3)} ", width=6, anchor=E)
        p2_lab_val.grid(row=5, column=1)
        p2_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        p2_lab_unit.grid(row=5, column=2)

        p3_lab = Label(frame, text="Primer 3:", width=8, anchor=W)
        p3_lab.grid(row=6, column=0)
        p3_lab_val = Label(frame, text=f" {round(self.final_mix['Primer 3'], 3)} ", width=6, anchor=E)
        p3_lab_val.grid(row=6, column=1)
        p3_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        p3_lab_unit.grid(row=6, column=2)

        p4_lab = Label(frame, text="Primer 4:", width=8, anchor=W)
        p4_lab.grid(row=7, column=0)
        p4_lab_val = Label(frame, text=f" {round(self.final_mix['Primer 4'], 3)} ", width=6, anchor=E)
        p4_lab_val.grid(row=7, column=1)
        p4_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        p4_lab_unit.grid(row=7, column=2)

        taq_lab = Label(frame, text="Taq:", width=8, anchor=W)
        taq_lab.grid(row=8, column=0)
        taq_lab_val = Label(frame, text=f" {round(self.final_mix['Taq'], 3)} ", width=6, anchor=E)
        taq_lab_val.grid(row=8, column=1)
        taq_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        taq_lab_unit.grid(row=8, column=2)

        gly_lab = Label(frame, text="Glycerol:", width=8, anchor=W)
        gly_lab.grid(row=9, column=0)
        gly_lab_val = Label(frame, text=f" {round(self.final_mix['Glycerol'], 3)} ", width=6, anchor=E)
        gly_lab_val.grid(row=9, column=1)
        gly_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        gly_lab_unit.grid(row=9, column=2)

        dmso_lab = Label(frame, text="DMSO:", width=8, anchor=W)
        dmso_lab.grid(row=10, column=0)
        dmso_lab_val = Label(frame, text=f" {round(self.final_mix['DMSO'], 3)} ", width=6, anchor=E)
        dmso_lab_val.grid(row=10, column=1)
        dmso_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        dmso_lab_unit.grid(row=10, column=2)

        h2o_lab = Label(frame, text="H₂O:", width=8, anchor=W)
        h2o_lab.grid(row=11, column=0)
        h2o_lab_val = Label(frame, text=f" {round(self.final_mix['H2O'], 3)} ", width=6, anchor=E)
        h2o_lab_val.grid(row=11, column=1)
        h2o_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        h2o_lab_unit.grid(row=11, column=2)

        total_lab = Label(frame, text="Mix Total:", width=8, anchor=W)
        total_lab.grid(row=12, column=0)
        total_lab_val = Label(frame, text=f" {round(self.final_mix['Mix Total'], 3)} ", width=6, anchor=E)
        total_lab_val.grid(row=12, column=1)
        total_lab_unit = Label(frame, text='\u03bcL', width=2, anchor=W)
        total_lab_unit.grid(row=12, column=2)

        dna_lab = Label(frame, text=f"Add {round(self.dna_add, 3)} \u03bcL of stock DNA to each reaction!",
                        justify=CENTER, anchor=CENTER, wraplength=140, foreground='red')
        dna_lab.grid(row=13, column=0, rowspan=2, columnspan=3)

        Separator(frame, orient=VERTICAL).grid(row=0, column=3, rowspan=15, sticky="ns", padx=10, pady=0)

        if self.duration['text'] == '0h 00m 00s':
            Label(frame, text="You have not defined a PCR Cycle!", justify=CENTER, anchor=CENTER,
                  wraplength=140).grid(row=0, column=4, rowspan=15, columnspan=3)
        else:
            Label(frame, text=f"Initial Denaturation: {self.init_denat_entry.get()} s at {self.init_denat_entry2.get()}"
                              f" \u00b0C", width=30, anchor=W).grid(row=1, column=4, columnspan=4)
            Label(frame, text=f"Denaturation: {self.denat_entry.get()} s at {self.denat_entry2.get()}"
                              f" \u00b0C", width=23, anchor=W).grid(row=2, column=4, columnspan=2)
            Label(frame, text=f"Annealing: {self.anneal_entry.get()} s at {self.anneal_entry2.get()}"
                              f" \u00b0C", width=23, anchor=W).grid(row=3, column=4, columnspan=2)
            Label(frame, text=f"Extension: {self.exten_entry.get()} s at {self.exten_entry2.get()}"
                              f" \u00b0C", width=23, anchor=W).grid(row=4, column=4, columnspan=2)
            Label(frame, text=f"{self.cycles_entry.get()}").grid(row=3, column=7)
            Label(frame, text=f"Final Extension: {self.fexten_entry.get()} m at {self.fexten_entry2.get()}"
                              f" \u00b0C", width=30, anchor=W).grid(row=5, column=4, columnspan=4)
            Label(frame, text="Hold: Forever at 4 \u00b0C", width=30, anchor=W).grid(row=6, column=4, columnspan=4)

            img = Image.open("./images/brace.png")
            img = img.resize((20, 70), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            brackets = Label(frame, image=img)
            brackets.image = img
            brackets.grid(row=2, column=6, rowspan=3)

            Label(frame, text=f"Minimum Run Time: {self.duration['text']}").grid(row=10, column=4, columnspan=4)

        save = Button(frame, text="Save", command=lambda: report(self))
        save.grid(row=15, column=0, columnspan=3, pady=(5, 5))
        close = Button(frame, text="Close", command=self.window.destroy)
        close.grid(row=15, column=4, columnspan=3, pady=(5, 5))
