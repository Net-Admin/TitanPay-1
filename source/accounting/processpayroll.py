import tkinter
import tkinter.messagebox
from source.accounting.makepayment import MakePayment

class ProcessPayroll:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Make IntVar
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # Objects
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Create Employee', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='View Time Cards', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='View Pay Rate or Salary', variable=self.radio_var, value=3)
        self.rb4 = tkinter.Radiobutton(self.top_frame, text='View Sales', variable=self.radio_var, value=4)
        self.rb5 = tkinter.Radiobutton(self.top_frame, text='Change Payment Method', variable=self.radio_var, value=5)
        self.rb6 = tkinter.Radiobutton(self.top_frame, text='Process Payroll', variable=self.radio_var, value=6)

        # Pack Buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()
        self.rb6.pack()

        # Buttons
        self.enact_button = tkinter.Button(self.bottom_frame, text="Implement Task", command=self.picker)

        #Pack Buttons
        self.enact_button.pack(side = 'left')

        #Frame Packing
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Start Main Look
        tkinter.mainloop()

    def picker(self):
        if self.radio_var.get() == 6:
            self.payroll()

    def payroll(self):
        #Main Window
        self.main_window = tkinter.Tk()

        #Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Set Up time windows
        self.timeLabel = tkinter.Label(self.middle_frame, text='Enter Date in MM/DD/YYYY Format')
        self.startLabel = tkinter.Label(self.middle_frame, text = 'Start Date')
        self.start_entry = tkinter.Entry(self.middle_frame, width=10)
        self.endLabel = tkinter.Label(self.middle_frame, text = "End Date")
        self.end_entry = tkinter.Entry(self.middle_frame, width = 10)

        #Pack Time
        self.timeLabel.pack()
        self.startLabel.pack(side = 'left')
        self.start_entry.pack(side = 'left')
        self.endLabel.pack(side = 'left')
        self.end_entry.pack(side = 'left')

        #Buttons
        self.enact_button = tkinter.Button(self.bottom_frame, text = "Process Payroll", command = self.processChoice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)

        #Pack Buttons
        self.enact_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        #Frame Packing
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        #Start Main Loop
        tkinter.mainloop()

    def processChoice(self):
        if self.start_entry.get() == '' or self.end_entry.get() == '':
            self.errorMessage()
        elif len(self.start_entry.get().split('/')) != 3 or len(self.end_entry.get().split('/')) != 3:
            self.errorMessage()
            pass
        else:
            starter = self.start_entry.get().split('/')
            ender = self.end_entry.get().split('/')
            for x in range (2):
                starter[x] = int(starter[x])
                ender[x] = int(ender[x])
            payer = MakePayment(starter, ender)
            payer.pay()
            s = payer.makeThePayment()
            tkinter.messagebox.showinfo('Payroll Processed', s)

    def errorMessage(self):
        tkinter.messagebox.showinfo('Error', 'Check your date inputs. There is an error.')

processpayroll = ProcessPayroll()
