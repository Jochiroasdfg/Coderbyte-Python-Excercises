# dictionary for card values
values = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 10,
    "queen": 10,
    "king": 10,
    "ace": 11}


def BlackjackHighest(strArr):
    # Total value of cards in hand
    total = 0
    new_total = 0
    highest_card = ""
    highest_value = 0

    for value in strArr:
        total += values[value]
    #print(total)

    if "ace" in strArr and total <= 21:
        highest_card = strArr.index("ace")
        if total < 21:
            print(f"below {strArr[highest_card]}")
        elif total == 21:
            print("blackjack " + strArr[highest_card])

    elif "ace" in strArr and total >= 22:
        values["ace"] = 1
        for value in strArr:
            new_total += values[value]
        #print(new_total)

        for card in strArr:
            if values[card] > highest_value:
                highest_value = values[card]
                highest_card = strArr.index(card)

        if new_total < 21:
            print(f"below {strArr[highest_card]}")
        elif new_total > 21:
            print(f"above {strArr[highest_card]}")

    elif total < 21:
        if "jack" in strArr:
            highest_card = strArr.index("jack")
            print(f"below {strArr[highest_card]}")
        elif "queen" in strArr:
            highest_card = strArr.index("queen")
            print(f"below {strArr[highest_card]}")
        elif "king" in strArr:
            highest_card = strArr.index("king")
            print(f"below {strArr[highest_card]}")
        elif "jack" not in strArr and "queen" not in strArr and "king" not in strArr:
            for card in strArr:
                if values[card] > highest_value:
                    highest_value = values[card]
                    highest_card = strArr.index(card)
            print(f"below {strArr[highest_card]}")

    elif total > 21:
        if "jack" in strArr:
            highest_card = strArr.index("jack")
            print(f"above {strArr[highest_card]}")
        elif "queen" in strArr:
            highest_card = strArr.index("queen")
            print(f"above {strArr[highest_card]}")
        elif "king" in strArr:
            highest_card = strArr.index("king")
            print(f"above {strArr[highest_card]}")
        elif "jack" not in strArr and "queen" not in strArr and "king" not in strArr:
            for card in strArr:
                if values[card] > highest_value:
                    highest_value = values[card]
                    highest_card = strArr.index(card)
            print(f"above {strArr[highest_card]}")

    elif total == 21:
        if "jack" in strArr:
            highest_card = strArr.index("jack")
            print(f"blackjack {strArr[highest_card]}")
        elif "queen" in strArr:
            highest_card = strArr.index("queen")
            print(f"blackjack {strArr[highest_card]}")
        elif "king" in strArr:
            highest_card = strArr.index("king")
            print(f"blackjack {strArr[highest_card]}")
        elif "jack" not in strArr and "queen" not in strArr and "king" not in strArr:
            for card in strArr:
                if values[card] > highest_value:
                    highest_value = values[card]
                    highest_card = strArr.index(card)
            print(f"blackjack {strArr[highest_card]}")


BlackjackHighest(["four","ace","ten"])
