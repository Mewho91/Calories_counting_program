d = {
    'Meal 1': {'Cal': 164, 'prot': 31, 'carb': 0, 'fat': 3},
    'Meal 2': {'Cal': 164, 'prot': 31, 'carb': 0, 'fat': 3}
}

# Numery posilkow
dk = d.keys()
dv = d.values()
for keys in dk:
    print(keys)
    for val in dv:
        print(val["Cal"])
# Cal
# dv = d.values()
# for val in dv:
#     print(val["Cal"])
# #Prot
# dv = d.values()
# for val in dv:
#     print(val["prot"])
# # carb
# dv = d.values()
# for val in dv:
#     print(val["carb"])
# # fat
# dv = d.values()
# for val in dv:
#     print(val["fat"])