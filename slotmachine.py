import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3
COLS = 3


symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}


def deposit():
    while True:
        amount = input("How much would you like to desposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount is less than 0")
        else:
            print("Please enter a valid amount.")
    return amount

def get_no_of_lines():
    while True:
        lines = input("How many lines do you wanna bet on? (1 -" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("The number of lines is less than 1")
        else:
            print("Please enter a valid amount.")
    return lines

def get_bet():
    while True:
        bet = input("Enter your bet amount for each line. $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet amount should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid amount.")
    return bet

def the_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()

def check_winnings(columns, lines, bets, sym_values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = columns[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += sym_values[symbol] * bets
            winning_line.append(line + 1)
    return winnings, winning_line

def spin(balance):
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You dont have enough balance for that shit. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. The total amount is equal to: ${total_bet}.")
    slots = the_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"You have won ${winnings}.")
    print(f"You won on lines:", *winning_line)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        ans = input("Press enter to play (q to quit).")
        if ans == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}.")
    

main()