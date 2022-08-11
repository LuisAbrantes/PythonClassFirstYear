studants_heights = input("Input a list of studant heights ").split()
for n in range(0, len(studants_heights)):
    studants_heights[n] = int(studants_heights[n])
print(studants_heights)

total_height = 0
for heights in studants_heights:
    total_height += height
print(total_height)

number_of_studants = 0
for studant in studants_heights:
    number_of_studants += 1
print(number_of_studants)

average_height = round(total_height / number_of_studants)
print(average_height)