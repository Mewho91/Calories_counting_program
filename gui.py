import tkinter
from tkinter import *
from tkinter.ttk import *
import functions


class Gui:
    def __init__(self):
        self.meal_count = 0
        self.product = None
        self.gram = 0
        self.box_value = None
        self.product_value = None
        self.entry_value = None
        self.finished = False


    def open_popup(self):
        root = Tk()
        root.title("Number of meals")
        root.config(padx=100, pady=100)

        open_label = Label(width=40, font=("Times", "15", "bold"), text="Welcome to calories counting program")
        open_label.grid(row=0, columnspan=2)
        open_label2 = Label(width=40, font=("Times", "15", "bold"), text="Chose number of meals and press confirm")
        open_label2.grid(row=1, columnspan=2)

        self.box_value = StringVar()
        meal_chose_scroll = Combobox(root, width=30, state='readonly', textvariable=self.box_value)
        meal_chose_scroll['values'] = (1, 2, 3, 4, 5, 6, 7, 8)
        meal_chose_scroll.grid(column=0, row=3, columnspan=1)

        button1 = Button(text="Confirm", width=40, command=lambda: [self.meal_number_get(), root.destroy()])
        button1.grid(column=1, row=3)

        root.mainloop()

    def meal_number_get(self):
        self.meal_count = int(self.box_value.get())

    def run_gui(self):

        fc = functions.Functions()
        root = Tk()
        root.title("Calories count program")
        root.config(padx=100, pady=20)

        scroll_label = Label(width=17, font=("Times", "10", "bold"), text="Chose a product name")
        scroll_label.grid(column=0, row=2)

        self.product_value = StringVar()
        scroll = Combobox(root, state='readonly', textvariable=self.product_value)
        scroll['values'] = (fc.name_chose())
        scroll.current(0)
        scroll.grid(column=0, row=3)

        button1 = Button(text="Confirm", command=lambda: [self.product_get(), self.product_gram()])
        button1.grid(column=2, row=3)
        button2 = Button(text="Finish", command=lambda: [root.destroy()])
        button2.grid(column=2, row=4)

        self.entry_value = IntVar()
        gramature_entry_label = Label(width=25, font=("Times", "10", "bold"), text="Enter a gramature of product")
        gramature_entry_label.grid(column=1, row=2)
        entry = Entry(width=25, font=("Times", "10", "bold"), textvariable=self.entry_value)
        entry.grid(column=1, row=3)

        root.mainloop()

    #
    # def add_label(self, name):
    #     new_label = Label(text=name)
    #     new_label.grid(column=0, row=5)

    def product_get(self):
        self.product = self.product_value.get()

    def product_gram(self):
        self.gram = int(self.entry_value.get())

    def next_meal(self):
        root = Tk()
        root.title("Next meal ?")
        root.config(padx=100, pady=20)

        button_next_meal = Button(text="Next meal", command=lambda: [self.next(), root.destroy()])
        button_next_meal.grid(column=0, row=1)

        button_this_meal = Button(text="Add to this meal", command=lambda: [self.this(), root.destroy()])
        button_this_meal.grid(column=1, row=1)

        root.mainloop()

    def next(self):
        self.finished = True

    def this(self):
        self.finished = False

    def results(self, r, sums):
        result_window = Tk()
        result_window.title("Results")
        result_window.config(padx=100, pady=20)
        for item in r:
            new_label = Label(text=item)
            new_label.grid(column=1, row=r.index(item) + 1)

        result_label = Label(text=sums)
        result_label.grid(column=1, row=9)

        result_button = Button(text="Continue", command=lambda: [result_window.destroy()])
        result_button.grid(column=1, row=12)

        result_window.mainloop()

    def sum_of_all(self, cal, prot, carb, fat):
        sum_cal = sum(cal)
        sum_prot = sum(prot)
        sum_carb = sum(carb)
        sum_fat = sum(fat)

        return f"Sum of calories : {sum_cal}, sum of proteins :  {sum_prot}, sum of carbs : {sum_carb}, sum of fat: {sum_fat}"
