from tkinter import *
from tkinter.ttk import *
import functions


class Gui:

    def run_gui(self):
        fc = functions.Functions()
        root = Tk()
        root.title("Calories count program")
        root.config(padx=100, pady=20)

        self.scroll_label = Label(width=17, font=("Times", "10", "bold"), text="Chose a product name")
        self.scroll_label.grid(column=0, row=2)

        self.product_value = StringVar()
        self.scroll = Combobox(root, state='readonly', textvariable=self.product_value)
        self.scroll.bind("<<ComboboxSelected>>", self.meal_number_get())
        self.scroll['values'] = (fc.name_chose())
        self.scroll.current(0)
        self.scroll.grid(column=0, row=3)

        self.button1 = Button(text="Confirm", command=lambda: [self.product_get(), self.product_gram, root.destroy()])
        self.button1.grid(column=2, row=3)

        self.entry_value = IntVar()
        self.gramature_entry_label = Label(width=25, font=("Times", "10", "bold"), text="Enter a gramature of product")
        self.gramature_entry_label.grid(column=1, row=2)
        self.entry = Entry(width=25, font=("Times", "10", "bold"), textvariable=self.entry_value)
        self.entry.grid(column=1, row=3)

        root.mainloop()

    def open_popup(self):
        root = Tk()
        root.title("Number of meals")
        root.config(padx=100, pady=100)

        self.open_label = Label(width=40, font=("Times", "15", "bold"), text="Welcome to calories counting program")
        self.open_label.grid(row=0, columnspan=2)

        self.open_label2 = Label(width=40, font=("Times", "15", "bold"), text="Chose number of meals and press confirm")
        self.open_label2.grid(row=1, columnspan=2)


        self.box_value = StringVar()
        self.meal_chose_scroll = Combobox(root, width=30, state='readonly', textvariable=self.box_value)
        self.meal_chose_scroll['values'] = (1, 2, 3, 4, 5, 6, 7, 8)
        self.meal_chose_scroll.bind("<<ComboboxSelected>>", self.meal_number_get())
        self.meal_chose_scroll.grid(column=0, row=3, columnspan=1)

        self.button1 = Button(text="Confirm", width=40, command=lambda: [self.meal_number_get(), root.destroy()])
        self.button1.grid(column=1, row=3)

        root.mainloop()

    def meal_number_get(self):
        self.meal_number = self.box_value.get()
        return self.meal_number

    def product_get(self):
        self.product_select = self.product_value.get()
        return self.product_select

    def product_gram(self):
        self.product_gram = self.entry_value.get()
        return self.product_gram

