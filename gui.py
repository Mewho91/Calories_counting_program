from tkinter import *
from tkinter.ttk import *
import functions


class Gui:
    def __init__(self):
        self.y = None
        self.meal_count = 0
        self.product = None
        self.gram = 0
        self.box_value = None
        self.product_value = None
        self.entry_value = None
        self.finished = False

    def first_window(self):
        root = Tk()
        root.title("Number of meals")


        my_img = PhotoImage(file="warzywa.png")

        canvas = Canvas(root, width=600, height=380)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(10, 0, image=my_img, anchor="nw")
        canvas.create_text(280, 100, text="Welcome to calories counting program",fill="white", font=("Times", "23", "bold"))
        canvas.create_text(280, 220, text="Chose number of meals and press confirm",fill="white", font=("Times", "20", "bold"))
        self.box_value = StringVar()
        meal_chose_scroll = Combobox(root, width=20, font=("Times", "15"), state='readonly', textvariable=self.box_value)
        meal_chose_scroll['values'] = (1, 2, 3, 4, 5, 6, 7, 8)
        meal_chose_scroll.current(0)
        meal_chose_scroll.pack()
        button1 = Button(root, width=30,  text="Confirm", command=lambda: [self.meal_number_get(), root.destroy()])
        button_canvas = canvas.create_window(350, 300, height=50, anchor="nw", window=button1)
        canvas_combos = canvas.create_window(50, 300,height=50, anchor="nw", window=meal_chose_scroll)

        root.mainloop()

    def meal_number_get(self):
        self.meal_count = int(self.box_value.get())

    def secound_window(self):
        fc = functions.Functions()
        root = Tk()
        root.title("Calories count program")

        my_img = PhotoImage(file="drugie okno program.png")
        canvas = Canvas(root, width=470, height=650)
        canvas.pack()
        canvas.create_image(10, 0, image=my_img, anchor="nw")
        canvas.create_text(200, 40, text="Chose a product name", fill="white",
                           font=("Times", "23", "bold"))

        self.product_value = StringVar()
        scroll = Combobox(root,font=("Times", "15", "bold"), state='readonly', textvariable=self.product_value)
        scroll['values'] = (fc.name_chose())
        scroll.current(0)
        scroll_canvas = canvas.create_window(40, 100, height=50, width=250, anchor="nw", window=scroll)

        self.entry_value = IntVar()
        entry = Entry(width=25, font=("Times", "25", "bold"), background="red", textvariable=self.entry_value)
        canvas_entry = canvas.create_window(40, 300, height=50, width=250, anchor="nw", window=entry)
        canvas_entry_label = canvas.create_text(240, 240, fill="white", font=("Times", "23", "bold"),
                                                text="Enter a gramature of product")

        button1 = Button(text="Confirm", width=50, command=lambda: [self.product_get(), self.product_gram(), root.destroy()])
        canvas_button1 = canvas.create_window(40, 400, height=50, anchor="nw", window=button1)
        root.mainloop()

    def product_get(self):
        self.product = self.product_value.get()

    def product_gram(self):
        self.gram = int(self.entry_value.get())

    def third_window(self, x):
        root = Tk()
        root.title("Next meal ?")

        my_img = PhotoImage(file="trzecie okno.png")
        canvas = Canvas(root, width=520, height=350)
        canvas.pack()
        canvas.create_image(0, 0, image=my_img, anchor="nw")

        canvas.create_text(250,30,text=f"You added {self.product} : {self.gram} grams", font=("Times", "20", "bold"))
        canvas.create_text(250,200,text=x, font=("Times", "15", "bold"))

        button_next_meal = Button(root, text="Go to next meal", command=lambda: [self.next(), root.destroy()])
        canvas_button_next_meal = canvas.create_window(100, 300, height=50, anchor="nw", window=button_next_meal)
        button_this_meal = Button(root, text="Add product to this meal", command=lambda: [self.this(), root.destroy()])
        canvas_button_this_meal = canvas.create_window(300, 300, height=50, anchor="nw", window=button_this_meal)

        root.mainloop()

    def next_meal(self, x):
        root = Tk()
        root.title("Next meal ?")
        root.config(padx=100, pady=20)

        label = Label(text=f"You added {self.product} : {self.gram} grams", font=("Times", "25", "bold"))
        label.grid(column=0, row=2)

        button_next_meal = Button(root, text="Next meal", command=lambda: [self.next(), root.destroy()])
        button_next_meal.grid(column=0, row=1)

        button_this_meal = Button(root, text="Add to this meal", command=lambda: [self.this(), root.destroy()])
        button_this_meal.grid(column=1, row=1)

        label = Label(text=x)
        label.grid(column=0, rowspan=1)

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

        save_button = Button(text="Restart program", command=lambda: [self.restart_program(), result_window.destroy()])
        save_button.grid(column=2, row=12)

        result_button = Button(text="Close program", command=lambda: [self.close_program(), result_window.destroy()])
        result_button.grid(column=1, row=12)

        result_window.mainloop()

    def sum_of_all(self, cal, prot, carb, fat):
        sum_cal = sum(cal)
        sum_prot = sum(prot)
        sum_carb = sum(carb)
        sum_fat = sum(fat)

        return f"Summary calories : {sum_cal}, proteins :  {sum_prot}, carbs : {sum_carb}, fat: {sum_fat}"

    def prods(self, prod_input, gram_input, meal):
        return f"Meal {meal + 1} - Product : {prod_input}, grams : {gram_input}"

    def dict_prods(self, prod_input, gram_input):
        dictio = f"({prod_input, gram_input}"
        return dictio

    def what_u_added_to_meal(self, d):
        values = []
        for a in d:
            values.append(f"In {a} you added ")
            for b in d[a]:
                values.append(f"{b[0]} {b[1]} grams")
        return values

    def return_list_added(self, l):
        val = []
        for i in l:
            val.append(i)
        new_val = ("".join(val))
        if len(new_val) > 1:
            return f"Your meal contains:\n"\
                   f"{new_val}\n"

    def restart_program(self):
        self.y = 0
        return self.y

    def close_program(self):
        self.y = 1
        return self.y
