from tkinter import *
from tkinter.ttk import *
import functions


class Gui:


    def run_gui(self):
        fc = functions.Functions()
        root = Tk()
        root.title("Calories count program")
        root.config(padx=100, pady=20)

        # meal_chose_label = Label(width=17, font=("Times", "10", "bold"), text="Chose number of meals")
        # meal_chose_label.grid(column=0, row=0)
        #
        # meal_chose_scroll = Combobox(root)
        # meal_chose_scroll['values'] = (1, 2, 3, 4, 5, 6, 7, 8)
        # meal_chose_scroll.grid(column=0, row=1)

        scroll_label = Label(width=17, font=("Times", "10", "bold"), text="Chose a product name")
        scroll_label.grid(column=0, row=2)

        scroll = Combobox(root, state='readonly')
        scroll['values'] = (fc.name_chose())
        scroll.current(0)
        scroll.grid(column=0, row=3)

        gramature_entry_label = Label(width=25, font=("Times", "10", "bold"), text="Enter a gramature of product")
        gramature_entry_label.grid(column=1, row=2)
        entry = Entry(width=25, font=("Times", "10", "bold"))
        entry.grid(column=1, row=3)
        root.mainloop()

    def open_popup(self):
        root = Tk()
        self.meal_chosed = 0
        root.title("Number of meals")
        root.config(padx=100, pady=20)

        meal_chose_label = Label(width=17, font=("Times", "10", "bold"), text="Chose number of meals")
        meal_chose_label.grid(column=0, row=0)

        meal_chose_scroll = Combobox(root, state='readonly')
        meal_chose_scroll['values'] = (1, 2, 3, 4, 5, 6, 7, 8)
        meal_chose_scroll.grid(column=0, row=1)

        button = Button(text="Confirm", command=root.destroy)
        button.grid(column=1, row=1)
        root.mainloop()
