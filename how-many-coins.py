
existing_coins = 0
print("You have " + str(existing_coins) + " coins.")
yes_or_no = input('Do you want a coin? ')

while yes_or_no == "yes":
    existing_coins += 1
    print("You have " + str((existing_coins)) + " coins.")
    break

else:
    print("You have " + str(existing_coins) + " coins. Bye.")

    

