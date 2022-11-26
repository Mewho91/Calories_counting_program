dict = {
    'Meal 1': [('Jabłko', 222), ('Banan', 222), ('Odżywka Białkowa', 333)],
    'Meal 2': [('Orzechy Włoskie', 333), ('Płatki Owsiane', 333)],
    'Meal 3': [('Banan', 333)]
}
values = []
for a in dict:
    # print(f"In {a} you added ")
    values.append(f"In {a} you added ")
    for b in dict[a]:
        # print(b[0])
        # print(f"{b[0]} {b[1]}grams")
        values.append(f"{b[0]} {b[1]} grams")

print(values)

