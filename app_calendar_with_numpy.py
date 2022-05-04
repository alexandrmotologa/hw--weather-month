from matplotlib import pyplot
import numpy as np
from os import system

month_name = "April"
date = 1
days_name = ["Mo", "Tu", "Wd", "Th", "Fr", "Sa", "Su"]
month_temps = np.array([
    # days -->
    # Mo    Tu    Wd    Th    Fr    Sa    Su
    [np.nan, np.nan, np.nan, np.nan, 7.0,  5.3,  12.2, ],
    [3.0,  7.7,  9.2,  15.8, 18.0, 11.3, 18.3, ],
    [11.3, 6.6,  6.1,  4.1,  12.0, 15.0, 18.3, ],
    [11.3, 12.6, 8.0,  4.1,  7.6,  11.8, 12.1, ],
    [15.9, 18.2, 3.3,  7.2,  8.1,  15.2, np.nan, ],
])

month_temps_c = month_temps[~np.isnan(month_temps)]
max_temp = month_temps_c.max()
min_temp = month_temps_c.min()
avg_temp = month_temps_c.sum() / month_temps_c.size

def line_console():
    print("-" * 63)

def empty_last_cell():
    print("|     |")

################## Display the calendar ##################
# Header
system("cls")
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
        if np.isnan(month_temps[week_index][day_index]):
            date_str = " " * 6
        else:
            date_str = date
            date += 1
        print(f"| {date_str:<6}", end="")
    empty_last_cell()

    for day_index in range(7):
        print(f"|       ", end="")
    print(f"|  {week_index+1}  |")

    for day_index in range(7):
        temp = f"{month_temps[week_index][day_index]:6.1f}" if ~np.isnan(
            month_temps[week_index][day_index]) else " " * 6
        print(f"|{temp} ", end="")
    empty_last_cell()
    line_console()

################## Display the calendar ##################

print(f"Max temp for {month_name}: {max_temp}C")
print(f"Min temp for {month_name}: {min_temp}C")
print(f"AVG temp for {month_name}: {avg_temp:1.1f}C")

pyplot.plot(range(1, month_temps_c.size+1, 1), month_temps_c)
pyplot.show()