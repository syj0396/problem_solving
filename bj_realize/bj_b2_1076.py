colors = ["black", "brown", "red", "orange", "yellow", "green",
        "blue", "violet", "grey", "white"]

first_color = input()
second_color = input()
third_color = input()

j_1 = colors.index(first_color)
j_2 = colors.index(second_color)
j_3 = colors.index(third_color)

value = j_1 * 10 + j_2 + 10**j_3
print(value)