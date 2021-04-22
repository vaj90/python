# Allow the user to enter some inputs
weeklyHour = float(input("Enter your weekly number of hours: "));
ratePerHour = float(input("Enter your rate per hour: "));
# Initialize workedPay = 0
workedPay = 0
if (weeklyHour > 0) and (weeklyHour <= 60):
    # Calculate the overtime by subtracting the weeklyHour in 40
    overtimeHour = weeklyHour - 40
    # if weeklyHour is more than 40 hr then will calculate the overtime
    if weeklyHour > 40:
        # calculate the overTimeHour then get the value of the paid overtime
        overtimePay = overtimeHour * 1.5
        # calculate the workedPay with overtimePay
        workedPay = (40 * ratePerHour) + overtimePay
    else:
        # calculate the workedPay
        workedPay = weeklyHour * ratePerHour
    # Print the calculation
    print("WeeklyHour:",weeklyHour ,"\nratePerHour:", ratePerHour, "\nOvertime:",overtimeHour ,"\nratePerHour:", workedPay)
