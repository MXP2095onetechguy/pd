from stratmov import Strategy, Move

class PrisonersDilemma:
    def __init__(self, strategy1: Strategy, strategy2: Strategy):
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.last_move1 = None
        self.last_move2 = None

    def play_round(self, current_round):
        self.strategy1.feed(self.last_move2, current_round=current_round)
        self.strategy2.feed(self.last_move1, current_round=current_round)

        move1 = self.strategy1.decide_move()
        move2 = self.strategy2.decide_move()

        self.last_move1 = move1
        self.last_move2 = move2

        if move1 == Move.COOPERATE and move2 == Move.COOPERATE:
            return (3, 3)
        elif move1 == Move.BETRAY and move2 == Move.COOPERATE:
            return (5, 0)
        elif move1 == Move.COOPERATE and move2 == Move.BETRAY:
            return (0, 5)
        elif move1 == Move.BETRAY and move2 == Move.BETRAY:
            return (1, 1)
        else:
            raise ValueError("Invalid moves")

    def run_game(self, rounds):
        total_payoff1 = 0
        total_payoff2 = 0

        for round_number in range(rounds):
            payoff1, payoff2 = self.play_round(current_round=round_number + 1)

            total_payoff1 += payoff1
            total_payoff2 += payoff2

        return total_payoff1, total_payoff2
