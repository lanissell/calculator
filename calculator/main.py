import sys
from BankCalculator import BankCalculator as bc

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python main.py <сумма кредита> <годовая ставка> <срок кредита>")
        print("Пример: python main.py 1000000 7.5 15")
        sys.exit(1)

    try:
        principal = float(sys.argv[1])
        annual_rate = float(sys.argv[2])
        years = int(sys.argv[3])

        monthly_payment = bc.calculate_monthly_payment(principal, annual_rate, years)

        print(f"\nЕжемесячный платеж: {monthly_payment:.2f} руб.")

    except ValueError:
        print("Ошибка: проверьте правильность введенных данных. Все значения должны быть числами.")
        sys.exit(1)