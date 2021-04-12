letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

possible__letter_combinations = list()

for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                alphabet_string = letter1 + letter2 + letter3 + letter4
                possible__letter_combinations.append(alphabet_string)
                
pin_combinations = list()

for pin in range(0, 10000):
    possible_pin = str(pin).zfill(4)
    pin_combinations.append(possible_pin)

possible_passwords = list()

for combo in possible__letter_combinations:
    for pin in pin_combinations:
        in_all_pass = "SKY-"
        hypen = "-"
        individual_passwords = in_all_pass + combo.upper() + hypen + pin
        possible_passwords.append(individual_passwords)



print(f"\nPossible Pins: {len(pin_combinations)}")
print(pin_combinations[0:50])
print(f"\nPossible Letter Combos: {len(possible__letter_combinations)}")
print(f"\n\nPossible Passwords: {len(possible_passwords)}")