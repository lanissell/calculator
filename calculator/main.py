from BankCalculator import BankCalculator as bc

if __name__ == "__main__":

    print("Калькулятор ежемесячного платежа по ипотечному кредиту")
    principal = float(input("Введите сумму кредита (в рублях): "))
    annual_rate = float(input("Введите годовую процентную ставку (в %): "))
    years = int(input("Введите срок кредита (в годах): "))

    monthly_payment = bc.calculate_monthly_payment(principal, annual_rate, years)

    print(f"\nЕжемесячный платеж: {monthly_payment:.2f} руб.")