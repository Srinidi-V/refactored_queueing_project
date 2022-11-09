from _tkinter import TclError
from tkinter import *
from tkinter.messagebox import *
from Plots import *
from Stochastic import *
from Deterministic import *


class Windows:
    def __init__(self, master):
        self.val1 = "Average Customers in System"
        self.val2 = "Average Customers in Queue"
        self.val3 = "Average Time Spent in System"
        self.val4 = "Average Time Waiting in Line"
        self.val5 = "Server Utilization"
        
        # --- Frames --- #
        label_frame1 = LabelFrame(master, text="Models", font=('Ubuntu', 10), fg="#0033ff")
        label_frame1.grid(row=0, column=0, pady=10, padx=10, rowspan=2)

        label_frame2 = LabelFrame(master, text="Inputs", font=('Ubuntu', 10), fg="#0033ff")
        label_frame2.grid(row=0, column=1, pady=10, padx=10)

        label_frame3 = LabelFrame(master, text="", font=('Ubuntu', 10), fg="#0033ff")
        label_frame3.grid(row=1, column=1, pady=10, padx=10)

        frame1 = Frame(label_frame2)
        frame1.grid(row=0, column=0, pady=5, padx=5, sticky=W)

        frame2 = Frame(label_frame2)
        frame2.grid(row=0, column=1, pady=5, padx=5, sticky=W)

        frame5 = Frame(label_frame3)
        frame5.grid(row=0, column=0, pady=5, padx=10)

        frame6 = Frame(label_frame3)
        frame6.grid(row=0, column=1, pady=5, padx=10)

        # --- Images --- #
        try:
            self.quit_img = PhotoImage(file="../images/button_quit.png")
            self.calculate_img = PhotoImage(file="../images/button_calculate.png")

            self.sys_size_img = PhotoImage(file="../images/e_in_s.png")
            self.q_time_img = PhotoImage(file="../images/w_in_q.png")
            self.total_time_img = PhotoImage(file="../images/w_in_s.png")
            self.departure_img = PhotoImage(file="../images/d_t.png")
            self.arrival_t_img = PhotoImage(file="../images/a_t.png")
            self.balking_cus_img = PhotoImage(file="../images/b_c.png")

            self.dd1k_img = PhotoImage(file="../images/button_d-d-k.png")
            self.mm1_img = PhotoImage(file="../images/button_m-m-1.png")
            self.mm1k_img = PhotoImage(file="../images/button_m-m-k.png")
            self.mmc_img = PhotoImage(file="../images/button_m-m-c.png")
            self.mmck_img = PhotoImage(file="../images/button_m-m-c-k.png")
        
        except TclError:
            self.quit_img = PhotoImage(file="./images/button_quit.png")
            self.calculate_img = PhotoImage(file="./images/button_calculate.png")

            self.sys_size_img = PhotoImage(file="./images/e_in_s.png")
            self.q_time_img = PhotoImage(file="./images/w_in_q.png")
            self.total_time_img = PhotoImage(file="./images/w_in_s.png")
            self.departure_img = PhotoImage(file="./images/d_t.png")
            self.arrival_t_img = PhotoImage(file="./images/a_t.png")
            self.balking_cus_img = PhotoImage(file="./images/b_c.png")

            self.dd1k_img = PhotoImage(file="./images/button_d-d-k.png")
            self.mm1_img = PhotoImage(file="./images/button_m-m-1.png")
            self.mm1k_img = PhotoImage(file="./images/button_m-m-k.png")
            self.mmc_img = PhotoImage(file="./images/button_m-m-c.png")
            self.mmck_img = PhotoImage(file="./images/button_m-m-c-k.png")

        # --- Buttons --- #
        self.quit = Button(frame5, image=self.quit_img, command=self.exit_program, borderwidth=0)
        self.quit.grid(row=0, column=0, sticky=W, pady=3, padx=16)

        self.calculate = Button(frame6, image=self.calculate_img, command=self.radio_event, borderwidth=0)
        self.calculate.grid(row=0, column=0, sticky=W, pady=3, padx=16)

        # --- Radio Buttons --- #
        self.rad_values = IntVar()

        self.dd1k = Radiobutton(label_frame1, image=self.dd1k_img, value=1, variable=self.rad_values, borderwidth=0, command=self.rad_dd1k)
        self.dd1k.grid(row=0, column=0, sticky=W, pady=5, padx=10)

        self.mm1 = Radiobutton(label_frame1, image=self.mm1_img, value=2, variable=self.rad_values, borderwidth=0, command=self.rad_mm1)
        self.mm1.grid(row=1, column=0, sticky=W, pady=0, padx=10)

        self.mm1k = Radiobutton(label_frame1, image=self.mm1k_img, value=3, variable=self.rad_values, borderwidth=0, command=self.rad_mm1k)
        self.mm1k.grid(row=2, column=0, sticky=W, pady=5, padx=10)

        self.mmc = Radiobutton(label_frame1, image=self.mmc_img, value=4, variable=self.rad_values, borderwidth=0, command=self.rad_mmc)
        self.mmc.grid(row=3, column=0, sticky=W, pady=0, padx=10)

        self.mmck = Radiobutton(label_frame1, image=self.mmck_img, value=5, variable=self.rad_values, borderwidth=0, command=self.rad_mmck)
        self.mmck.grid(row=4, column=0, sticky=W, pady=5, padx=10)

        # --- Labels --- #
        self.__lambda = Label(frame1, text="Arrival rate(λ):", font=('Ubuntu', 16))
        self.__lambda.grid(row=0, column=0, sticky=W, pady=0, padx=5)

        self.__mu = Label(frame1, text="Service rate(μ):", font=('Ubuntu', 16))
        self.__mu.grid(row=1, column=0, sticky=W, pady=5, padx=5)

        self.__k = Label(frame1, text="Queue Capacity(K):", font=('Ubuntu', 16))
        self.__k.grid(row=2, column=0, sticky=W, pady=0, padx=5)

        self.__c = Label(frame1, text="Servers(C):", font=('Ubuntu', 16))
        self.__c.grid(row=3, column=0, sticky=W, pady=5, padx=5)

        self.__M = Label(frame1, text="Initial Customers(M):", font=('Ubuntu', 16))
        self.__M.grid(row=4, column=0, sticky=W, pady=0, padx=5)

        # --- Entries --- #
        self.__elambda = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__elambda.grid(row=0, column=1, sticky=W, pady=5, padx=5)

        self.__emu = Entry(frame2, bd=2, font=('Ubuntu', 10), justify=LEFT)
        self.__emu.grid(row=1, column=1, sticky=W, pady=5, padx=5)

        self.__ek = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__ek.grid(row=2, column=1, sticky=W, pady=5, padx=5)

        self.__ec = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__ec.grid(row=3, column=1, sticky=W, pady=5, padx=5)

        self.__em = Entry(frame2, bd=2, font=('Ubuntu', 10))
        self.__em.grid(row=4, column=1, sticky=W, pady=5, padx=5)

    @staticmethod
    def exit_program():
        if askquestion(title='Quit?', message='Do you really want to quit?') == 'yes':
            exit()

    def rad_dd1k(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="normal")
        self.__ec.configure(state="disabled")
        self.__em.configure(state="normal", text="0")

    def rad_mm1(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="disabled")
        self.__ec.configure(state="disabled")
        self.__em.configure(state="disabled", text="0")

    def rad_mm1k(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="normal")
        self.__ec.configure(state="disabled")
        self.__em.configure(state="disabled", text="0")

    def rad_mmc(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="disabled")
        self.__ec.configure(state="normal")
        self.__em.configure(state="disabled", text="0")

    def rad_mmck(self):
        self.__elambda.configure(state="normal")
        self.__emu.configure(state="normal")
        self.__ek.configure(state="normal")
        self.__ec.configure(state="normal")
        self.__em.configure(state="disabled", text="0")

    def radio_event(self):
        radio_selected = self.rad_values.get()
