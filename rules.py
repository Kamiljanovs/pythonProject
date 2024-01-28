def check_win_loss(initial_money, current_money):
    if current_money > initial_money:
        return "вы в выигрыше"
    elif current_money < initial_money:
        return "вы в проигрыше"
    else:
        return "вы остались при своих"
