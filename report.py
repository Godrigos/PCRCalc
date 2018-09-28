from tkinter.filedialog import asksaveasfilename
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors


def y(self):
    x = 6.4
    if self.final_mix['Primer 3'] != 0:
        x += 0.4
    if self.final_mix['Primer 4'] != 0:
        x += 0.4
    if self.final_mix['Glycerol'] != 0:
        x += 0.4
    if self.final_mix['DMSO'] != 0:
        x += 0.4
    return x


def report(self):
    try:
        file = asksaveasfilename(parent=self.window, defaultextension=".pdf", initialdir=Path.home(),
                                 filetypes=[("PDF files", "*.pdf")], title="Select a directory and enter a filename")

        width, height = (5 * cm, y(self) * cm)
        c = canvas.Canvas(file,  pagesize=(width, height))
        c.setTitle("PCRCalc Output")
        textmix = c.beginText()
        textmix.setFont("Helvetica", 10)
        textmix.setTextOrigin(10, (height-15))

        textmix.textLine(f"{self.react_num_entry.get()} reactions of {self.react_vol_entry.get()} \u03bcL need:")
        textmix.textLine("")
        textmix.textLine(f"Buffer:      {round(self.final_mix['Buffer'], 3)} \u03bcL")
        textmix.textLine(f"DNTPs:    {round(self.final_mix['DNTPs'], 3)} \u03bcL")
        textmix.textOut("MgCl")
        apply_scripting(textmix, "2", -2)
        textmix.textLine(f":      {round(self.final_mix['MgCl2'], 3)} \u03bcL")
        textmix.textLine(f"Primer 1:  {round(self.final_mix['Primer 1'], 3)} \u03bcL")
        textmix.textLine(f"Primer 2:  {round(self.final_mix['Primer 2'], 3)} \u03bcL")
        if self.final_mix['Primer 3'] != 0:
            textmix.textLine(f"Primer 3:  {round(self.final_mix['Primer 3'], 3)} \u03bcL")
        if self.final_mix['Primer 4'] != 0:
            textmix.textLine(f"Primer 4:  {round(self.final_mix['Primer 4'], 3)} \u03bcL")
        textmix.textLine(f"Taq:         {round(self.final_mix['Taq'], 3)} \u03bcL")
        if self.final_mix['Glycerol'] != 0:
            textmix.textLine(f"Glycerol:  {round(self.final_mix['Glycerol'], 3)} \u03bcL")
        if self.final_mix['DMSO'] != 0:
            textmix.textLine(f"DMSO:     {round(self.final_mix['DMSO'], 3)} \u03bcL")
        textmix.textOut('H')
        apply_scripting(textmix, "2", -2)
        textmix.textLine(f"O:         {round(self.final_mix['H2O'], 3)} \u03bcL")
        textmix.textLine("")
        textmix.textLine(f"Mix Total: {round(self.final_mix['Mix Total'], 3)} \u03bcL")
        textmix.textLine("")
        textmix.setFillColor(colors.red)
        textmix.textLine(f"Add {round(self.dna_add, 3)} \u03bcL of stock DNA")
        textmix.textLine("to each reaction!")
        textmix.setFillColor(colors.black)

        c.drawText(textmix)
        c.save()
    except AttributeError:
        pass


def apply_scripting(textmix, text, rise):
    textmix.setFont("Helvetica", 6)
    textmix.setRise(rise)
    textmix.textOut(text)
    textmix.setFont("Helvetica", 10)
    textmix.setRise(0)
