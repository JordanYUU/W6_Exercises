# Finding Substrings with .find()

sched1 = "Garbage pickup is Wednesday"
sched2 = "Recycling pickup is Wednesday"
sched3 = "Yard waste pickup is Friday"

# print(sched2.upper().rfind('RECYCLING'))
# print(sched2.rfind('pickup'))
# print(sched2.find('Wednesday'))
# print(sched2.rfind('Wednesday'))




# Formatting strings using format()

# inv_gar = 26.39
# inv_recy = 8.02
# inv_yw = 14.12

# total_bill = "Your total waste management bill is : {total:.2f}"
# breakdown = "Total includes harbage {0}, recycling {1}, and yard waste {14}"

# print(total_bill.format(total = inv_gar + inv_recy + inv_yw))
# print(breakdown)

# print(f'''Your total waste management bill is: 
#       ${format(inv_gar + inv_recy + inv_yw, ".2f")}''')




# Replace Method

# print(f'''Schedule change! This week, due to the holiday:
#       {sched1.replace("Wednesday", "Thirsday")}
#       {sched2.replace("Wednesday", "Thursday")}
#       {sched3.replace("Wednesday", "Thursday")}''')




# Range function

# test_range = range(1, 31, 7)
# for x in test_range:
#     print(x)