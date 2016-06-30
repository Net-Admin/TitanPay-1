import tkinter
import tkinter.messagebox
from source.accounting import payer


class ProcessPayroll:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.timeLabel = tkinter.Label(self.middle_frame, text='Enter Date in MM/DD/YYYY Format')
        self.startLabel = tkinter.Label(self.middle_frame, text = 'Start Date')
        self.start_entry = tkinter.Entry(self.middle_frame, width=10)
        self.endLabel = tkinter.Label(self.middle_frame, text="End Date")
        self.end_entry = tkinter.Entry(self.middle_frame, width=10)

        self.timeLabel.pack()
        self.startLabel.pack(side='left')
        self.start_entry.pack(side='left')
        self.endLabel.pack(side='left')
        self.end_entry.pack(side='left')

        self.enact_button = tkinter.Button(self.bottom_frame, text="Process Payroll", command=self.processChoice)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.enact_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def processChoice(self):
        if self.start_entry.get() == '' or self.end_entry.get() == '':
            self.errorMessage()
        elif len(self.start_entry.get().split('/')) != 3 or len(self.end_entry.get().split('/')) != 3:
            self.errorMessage()
        else:
            starter = self.start_entry.get().split('/')
            ender = self.end_entry.get().split('/')
            for x in range(len(ender)):
                starter[x] = int(starter[x])
                ender[x] = int(ender[x])
            s = payer.dictionaryMaker(starter, ender)
            tkinter.messagebox.showinfo('Payroll Processed', s)

    def errorMessage(self):
        tkinter.messagebox.showinfo('Error', 'Check your date inputs. There is an error.')

