import random
templates = [
    {
        "text": "The :adjective :noun jumped over the :adjective :noun.",
        "author": "Alice"
    },
    {
        "text": "Once upon a time, a :adjective :animal lived in a :place.",
        "author": "Bob"
    },
    {
        "text": "My favorite food is :food because it is so :adjective.",
        "author": "Charlie"
    },
    {
        "text": "The :color :vehicle drove down the :adjective road.",
        "author": "Diana"
    },
    {
        "text": "In the :season, I love to :verb with my :noun.",
        "author": "Eve"
    },
    {
        "text": "The :adjective :profession works at the :place every day.",
        "author": "Frank"
    },
    {
        "text": "A :adjective :creature lives in the depths of the :body_of_water.",
        "author": "Grace"
    },
    {
        "text": "The :adjective :instrument makes beautiful music.",
        "author": "Hank"
    },
    {
        "text": "During the :event, everyone wears a :adjective costume.",
        "author": "Ivy"
    },
    {
        "text": "The :adjective :fruit fell from the tree and landed on my :body_part.",
        "author": "Jack"
    }
]
yes_answers = {"yes", "y", "sí", "si", "s", "oui",
               "o", "yeah", "yep", "sure", "absolutely"}


def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if 1 <= len(user_input) <= 30:
            return user_input
        else:
            print("Input must be between 1 and 30 characters long. Please try again.")


def play_mad_libs():
    print("Welcome to the Mad Libs game!")
    while True:
        template = random.choice(templates)
        text = template["text"]
        author = template["author"]
        words_to_fill = {}
        parts = text.split()
        for part in parts:
            if part.startswith(":"):
                key = part[1:]
                if key not in words_to_fill:
                    user_word = get_user_input(f"Please enter a {key}: ")
                    words_to_fill[key] = user_word
        completed_text = text
        for key, user_word in words_to_fill.items():
            completed_text = completed_text.replace(f":{key}", user_word)
        print("\nHere is your completed Mad Libs story:")
        print(completed_text)
        print(f"\n-- Story by {author}\n")
        play_again = input(
            "Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in yes_answers:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_mad_libs()
