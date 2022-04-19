days = ["Mo", "Tu", "Wd", "Th", "Fr", "Sa", "Su"]

april_temps = [
    # days -->
    # Mo    Tu    Wd    Th    Fr    Sa    Su
    [ None, None, None, None, 7.0,  5.3,  2.2, ],
    [ 3.0,  7.7,  9.2,  15.8, 18.0, 11.3, 18.3, ],
    [ 11.3, 6.6,  6.1,  4.1,  12.0, 15.0, 18.3, ],
    [ 11.3, 12.6, 8.0,  4.1,  7.6,  11.8, 12.1, ],
    [ 15.9, 18.2, 3.3,  7.2,  8.1,  15.2, 16.9, ],
]

while True:
    print()
    option = input("Temperature for a day(type d) or a week(type w)? ")
    
    if option == "d":
        week = int(input("Type a week from April: "))-1
        if week >=0 and week <=4:
            day = int(input("Type a day from April: "))-1
            if day >= 0 and day <= 6:
                if april_temps[week] != None and april_temps[week][day] != None:
                    print(f"Today's temperature {april_temps[week][day]:3.3}C")
                else:
                    print("Wrong week or day...")
            else:
                print("Wrong week or day...")
        else:
            print("Wrong week or day...")
            
    if option == "w":
        week = int(input("Type a week from April: "))-1
        if week >= 0 and week <= 4:
            if april_temps[week] != None:
                days_of_week = april_temps[week]
                for day_index in range(7):
                    if april_temps[week][day_index] != None:
                        print(
                            f"Temperature for {days[day_index]}: {april_temps[week][day_index]:3.3}C")
                    else:
                        print(f"Temperature for {days[day_index]}: isn't disponible")
            else:
                print("Wrong week or day...")
        else:
            print("Wrong week or day...")