'''def join_name(names):
    string = ""
    for index, name in enumerate(names):
        if index > 0:
            string += ', '
        if index == len(names) - 1:
            string += "and "
        string += name
    return string

def introduce(title, names):
    message = f'{title}: {join_name(names)}'
    return message
frase = introduce("My family",['Renato', 'Duda', 'Rosileia'])
print(frase)
'''
import random

OPTIONS = ['Rock', 'Paper', 'Scissors']

class RockPaperScissorsSimulator:
    def __init__(self) -> None:
        self._human_choice = None
        self._computer_choice = None

    @staticmethod
    def print_draw():
        print("Draw!")

    def print_choices(self):
        print(f"You chose {self._human_choice}")
        print(f"Computer chose {self._computer_choice}")

    @staticmethod
    def print_option():
        print("\n".join(f"{i + 1} {option}" for i, option in enumerate(OPTIONS)))
    
    def get_computer_choice(self):
        self._computer_choice = random.choice(OPTIONS)

    def get_human_choice(self):
        choice = int(input("Please choose a number: "))
        self._human_choice = OPTIONS[choice - 1]

    def print_lose_or_win(self, frase_1, human_choice, frase_2, computer_choice):
        print(f"{frase_1}! {self._human_choice} {frase_2} {self._computer_choice}!")

    def win_or_lose(self,human_beats, human_loses):
        if self._computer_choice == human_loses:
            self.print_lose_or_win("Sorry", self._human_choice, "is beated by", self._computer_choice)
        elif self._computer_choice == human_beats:
            self.print_lose_or_win("Yes", self._human_choice, "beats", self._computer_choice)

    def print_result(self):
        if self._human_choice == self._computer_choice:
            self.print_draw()

        if self._human_choice == OPTIONS[0]:
            self.win_or_lose(OPTIONS[2], OPTIONS[1])
        elif self._human_choice == OPTIONS[1]:
            self.win_or_lose(OPTIONS[0], OPTIONS[2])
        elif self._human_choice == OPTIONS[2]:
            self.win_or_lose(OPTIONS[1], OPTIONS[0])

    def simulate(self):
        self.print_option()
        self.get_computer_choice()
        self.get_human_choice()
        self.print_choices()
        self.print_result()

jogo_1 = RockPaperScissorsSimulator()
jogo_1.simulate()
