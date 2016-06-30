from source.accounting.processpayroll import ProcessPayroll
import tkinter
import tkinter.messagebox

class Menu:
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

        self.enact_button = tkinter.Button(self.bottom_frame, text="Implement Task", command=self.picker)

        self.enact_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def picker(self):
        if self.radio_var.get() == 6:
            payroll = ProcessPayroll()

menu = Menu()