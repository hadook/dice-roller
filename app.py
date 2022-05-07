
class App:
    """This class represents the main application instance."""

    def __init__(self) -> None:
        self.running = True

    def run(self):
        print("\n--- Dice roller ---")
        
        while self.running:
            formula = input('\n> ')

            if formula == '/exit':
                self.running = False

            elif formula.startswith('/roll '):
                print('executing')

            else:
                print('invalid formula')


if __name__ == "__main__":
    App().run()
