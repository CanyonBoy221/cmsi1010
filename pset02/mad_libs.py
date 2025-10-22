# ----------------------------------------------------------------------
# This is the file mad_libs.py
#
# The intent is to give you practice writing a complete, interactive
# Python program using a lot of Python data types, especially lists,
# sets, and dictionaries.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!
#
# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.
#
# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.
#
# Here are some constraints:
#
#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.
# ----------------------------------------------------------------------
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
