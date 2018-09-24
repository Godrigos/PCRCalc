def duration(self, *args):
    """Sum and return the minimum total time expected for PCR cycle."""
    try:
        init = int(self.init_denat_entry.get())
    except ValueError:
        init = 0
    try:
        cycles = int(self.cycles_entry.get())
    except ValueError:
        cycles = 0
    try:
        denat = int(self.denat_entry.get())
    except ValueError:
        denat = 0
    try:
        anneal = int(self.anneal_entry.get())
    except ValueError:
        anneal = 0
    try:
        exten = int(self.exten_entry.get())
    except ValueError:
        exten = 0
    try:
        final = int(self.fexten_entry.get()) * 60
    except ValueError:
        final = 0

    total_sec = init + (cycles * (denat + anneal + exten)) + final
    total_min = total_sec // 60
    total_hours = total_min // 60
    total_time = (str(total_hours) + 'h ' + "%02d" % (total_min % 60) + 'm ' + "%02d" % (total_sec % 60) + 's')
    for arg in args:
        del arg
    return total_time
