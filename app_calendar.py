month_name = "April"
date = 1
days_name = ["Mo", "Tu", "Wd", "Th", "Fr", "Sa", "Su"]
month_temps = [
    # days -->
    # Mo    Tu    Wd    Th    Fr    Sa    Su
    [None, None, None, None, 7.0,  5.3,  12.2, ],
    [3.0,  7.7,  9.2,  15.8, 18.0, 11.3, 18.3, ],
    [11.3, 6.6,  6.1,  4.1,  12.0, 15.0, 18.3, ],
    [11.3, 12.6, 8.0,  4.1,  7.6,  11.8, 12.1, ],
    [15.9, 18.2, 3.3,  7.2,  8.1,  15.2, None, ],
]

month_temps_1d = []
for week_index in range(5):
    for day_index in range(7):
        if month_temps[week_index][day_index] != None:
            month_temps_1d.append(month_temps[week_index][day_index])

max_temp = max(month_temps_1d)
min_temp = min(month_temps_1d)

# HW 2.4*
avg_temp = sum(month_temps_1d) / len(month_temps_1d)

# HW 2.3*
def line_console():
    print("-" * 63)

def empty_last_cell():
    print("|     |")


################## Display the calendar ##################
# Header
line_console()
print(f"| {month_name:54}|     |")
line_console()

# Day names
for day_index in range(7):
    print(f"| {days_name[day_index]}    ", end="")
empty_last_cell()
line_console()

# Loop through the weeks
for week_index in range(5):
    # Temps for one week
    for day_index in range(7):
        if month_temps[week_index][day_index] == None:
            date_str = " " * 6
        else:
            date_str = date
            date +=1
        print(f"| {date_str:<6}", end = "")
    empty_last_cell()
    
    # HW 2.2
    for day_index in range(7):
        print(f"|       ", end="")
    print(f"|  {week_index+1}  |")
    
    for day_index in range(7):
        # HW 2.1
        # if month_temps[week_index][day_index] != None:
        #     temp = f"{month_temps[week_index][day_index]:6.1f}"
        # else:
        #     temp = " " * 6
        temp = f"{month_temps[week_index][day_index]:6.1f}" if month_temps[week_index][day_index] != None else " " * 6
        print(f"|{temp} ", end="")
    empty_last_cell()
    line_console()

################## Display the calendar ##################

print(f"Max temp for {month_name}: {max_temp}C")
print(f"Min temp for {month_name}: {min_temp}C")
print(f"AVG temp for {month_name}: {avg_temp:1.1f}C")