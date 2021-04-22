def main():

    print("The future value calculator \n")

    monthly_investment = float(input("Enter your monthly investment: "))
    yearly_interest = float(input("Enter yearly interest rate: "))
    years = int(input("Enter number of years: "))

    def calculate_future_value(monthly_investment, yearly_interest, years=20):
        monthly_interest_rate = yearly_interest/12/100
        months = years * 12

        future_value = 0.0
        for i in range(0, months):
            future_value += monthly_investment
            monthly_interest = future_value * monthly_interest_rate
            future_value += monthly_interest
        return future_value

    future_value = calculate_future_value(monthly_investment, yearly_interest, years)
    print("Future value: ", round(future_value, 2))



if __name__=="__main__":
    main()