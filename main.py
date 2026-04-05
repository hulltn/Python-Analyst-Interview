import random
import time

symbols = ["🍒", "🍋", "🍊", "⭐", "💎"]

def spin():
    return [random.choice(symbols) for _ in range(3)]

def show_spin():
    for _ in range(5):
        print("🎰 Spinning...", end="\r")
        time.sleep(0.2)

def check_win(result, bet):
    if result[0] == result[1] == result[2]:
        if result[0] == "💎":
            return bet * 10
        return bet * 5
    elif len(set(result)) == 2:
        return bet * 2
    return 0

def main():
    print("🎰 Welcome to Python Slots!")

    balance = int(input("Enter starting balance: $"))

    while balance > 0:
        print(f"\n💰 Balance: ${balance}")

        try:
            bet = int(input("Enter your bet (0 to quit): "))
        except ValueError:
            print("❌ Invalid input")
            continue

        if bet == 0:
            break

        if bet > balance:
            print("❌ Not enough money!")
            continue

        balance -= bet

        show_spin()
        result = spin()

        print(" | ".join(result))

        winnings = check_win(result, bet)

        if winnings > 0:
            print(f"🎉 You won ${winnings}!")
            balance += winnings
        else:
            print("😢 You lost!")

    print("💀 Game over!")

if __name__ == "__main__":
    main()

