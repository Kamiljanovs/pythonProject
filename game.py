from casino import CasinoGame
from rules import check_win_loss


def main():
    casino_game = CasinoGame()
    casino_game.start_game()

    while True:
        choice = input("Хотите ли вы сыграть еще? (да/нет): ")

        if choice.lower() == 'да':
            casino_game.make_bet()
        elif choice.lower() == 'нет':
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")

    result = check_win_loss(casino_game.initial_money, casino_game.current_money)
    print(f"Игра завершена. Вы {result}.")


if __name__ == "__main__":
    main()

