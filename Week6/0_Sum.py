class ZeroSumGame:
    def __init__(self, start):
        self.start = start
        self.current = start
        self.players = ['agent', 'opponent']
        self.player = 'agent'  
        self.memo = {}

    def actions(self, state):
        if state % 2 == 0:
            return ['divide', 'subtract']
        else:
            return ['subtract']

    def successor(self, state, action):
        if action == 'divide':
            return state // 2
        elif action == 'subtract':
            return state - 1

    def isEnd(self, state):
        return state == 0

    def utility(self, state):
        if self.isEnd(state):
            return 1 if self.player == 'opponent' else -1
        return 0

    def get_best_move(self, state):
        if state in self.memo:
            return self.memo[state]

        possible_actions = self.actions(state)
        for action in possible_actions:
            next_state = self.successor(state, action)
            if self.isEnd(next_state):
                self.memo[state] = action
                return action

        # Default to 'subtract' if no better choice is found.
        self.memo[state] = 'subtract'
        return 'subtract'

    def play(self):
        while not self.isEnd(self.current):
            print(f'Current number is {self.current}')

            if self.player == 'agent':
                action = self.get_best_move(self.current)
                print(f'Agent chooses action: {action}')
            else:
                print(f'Possible actions are {self.actions(self.current)}')
                action = input('Enter action (divide or subtract): ')

            # Update the current state and switch players
            self.current = self.successor(self.current, action)
            self.player = self.players[(self.players.index(self.player) + 1) % 2]

        # When the game ends, print the result
        winner = 'agent' if self.player == 'agent' else 'opponent'
        print(f'Game over. {winner} wins!')


if __name__ == '__main__':
    start = int(input('Enter start number: '))
    game = ZeroSumGame(start)
    game.play()
