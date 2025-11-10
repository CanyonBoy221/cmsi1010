from cards import deal, poker_classification


def main():
    while True:
        user_input = input(
            "Enter the number of players(2-10): ").strip().lower()

        if user_input in ["bye", "exit"]:
            break

        try:
            num_players = int(user_input)
            if num_players < 2 or num_players > 10:
                print("Number of players must be between 2 and 10")
                continue

            hands = deal(num_players, 5)

            for hand in hands:
                cards_str = " ".join(str(card) for card in sorted(
                    hand, key=lambda c: (c.rank, c.suit)))
                classification = poker_classification(hand)
                print(f"{cards_str} is a {classification}")

        except ValueError:
            print("Please enter a valid number")
            continue


if __name__ == "__main__":
    main()
