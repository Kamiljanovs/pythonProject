import random
import configparser


class CasinoGame:
    def __init__(self):
        self.initial_money = self.load_initial_money()
        self.current_money = self.initial_money
        self.slots = list(range(1, 11))

    def load_initial_money(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        return int(config['Game']['MY_MONEY'])

    def make_bet(self):
        bet_amount = int(input(f"У вас {self.current_money}$, введите ставку: "))
        selected_slot = int(input("Выберите слот (от 1 до 10): "))

        winning_slot = random.choice(self.slots)
        if selected_slot == winning_slot:
            self.current_money += 2 * bet_amount
            print(f"Поздравляем! Вы выиграли. Ваш текущий баланс: {self.current_money}$")
        else:
            self.current_money -= bet_amount
            print(f"Увы, вы проиграли. Ваш текущий баланс: {self.current_money}$")

    def start_game(self):
        print("Добро пожаловать в игру Казино!")
        print(f"У вас в начале игры {self.initial_money}$.")