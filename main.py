import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A":3,
    "B":4,
    "C":5,
    "D":7
}

symbol_value = {
    "A":6,
    "B":5,
    "C":4,
    "D":3
}

def check_winnigs(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[lines]
            if symbol != symbol_to_check:
                break
            else:
                winnigs += values[symbol] * bet
                winnings_lines.append(line + 1)
    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_value in symbols.items():
        for _ in range(symbol_value):
            all_symbols.append(symbol)
    
    table = []
    for _ in range(cols):
        colmns = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbol.remove(value)
            colmns.append(value)
        table.append(colmns)

    return table
            
def show_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) -1:
                print(col[row],"|",end=" ")
            else:
                print(col[row])
    

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        bet = input("What would you like to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")

    return bet


def spin(balance):
    lines = get_number_of_lines
    while True:
        bet = get_bet()
        lines = get_number_of_lines()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is {balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines}. Total bet is equal to: {total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    show_slot_machine(slots)
    winnigs, winning_lines = check_winnigs(slots, lines, bet, symbol_value)
    print(f"You won {winnigs}.")
    print(f"You won lines:", *winning_lines)
    return winnigs - total_bet
    
def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left win {balance}")
main()