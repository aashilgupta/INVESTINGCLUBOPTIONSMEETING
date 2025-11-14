import random

START_BALANCE = 30000
ROUNDS = 10

def get_user_choice(balance):
    print(f"\nCurrent Balance: ${balance}")
    print("Choose ONE for this round:")
    print("A: 5-point spread (Win=$200, Loss=$300 per contract)")
    print("B: 10-point spread (Win=$140, Loss=$860 per contract)")
    print("C: Skip this round")
    choice = input("Your choice (A/B/C): ").strip().upper()

    if choice == "C":
        return choice, 0
    contracts = int(input("How many contracts? (1-10): "))

    # Check if you can afford the risk
    max_loss = 300 if choice == "A" else 860
    if contracts < 1 or contracts > 10 or balance < max_loss * contracts:
        print("Not enough balance for this risk or invalid contract number.")
        return "C", 0
    return choice, contracts

def play_game():
    balance = START_BALANCE
    for round_num in range(1, ROUNDS+1):
        print(f"\n--- Round {round_num} ---")
        choice, contracts = get_user_choice(balance)

        if choice == "C":
            print("Round skipped.")
            continue

        # Random win/loss (50% chance each)
        outcome = random.choice(["Win", "Loss"])
        if choice == "A":
            win, loss = 200, 300
        else:
            win, loss = 140, 860

        if outcome == "Win":
            gain = win * contracts
            balance += gain
            print(f"Result: WIN! You gained ${gain}.")
        else:
            cost = loss * contracts
            balance -= cost
            print(f"Result: LOSS. You lost ${cost}.")

        print(f"End of Round Balance: ${balance}")

        # End if out of money
        if balance <= 0:
            print("Bankrupt! Game over.")
            break

    print(f"\nFinal Balance: ${balance}")
    if balance > START_BALANCE:
        print("Great job! You finished with more than you started.")
    else:
        print("Try again to beat your starting balance.")

play_game()
