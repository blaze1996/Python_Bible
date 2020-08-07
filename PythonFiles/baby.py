from random import choice
from typing import List

question = ["Why is my cat green?: ", "Why are marshmellos squishy?: ", "Why have we not abolished the Patriot Act?: "]

question = choice(question)
answer = input(question).lower()

while answer!= "just because":
    answer = input("why?: ").strip().lower()

print("Oh... okay")