from util.parser import Parser


"""This class represents the main application instance."""
class App:

    # initializes the app
    def __init__(self) -> None:
        self.running = True

    # runs app in a loop, asking for user input and evaluating it
    def run(self):
        print("\n--- Dice roller ---")

        while self.running:
            exp = input('\n> ')

            if exp.startswith('/exit'):
                self.running = False

            elif exp.startswith('/roll '):
                p = Parser(exp)
                if p.result is not None:
                    print(p)
                else:
                    print('Invalid command.')

            else:
                print('Invalid command.')


if __name__ == "__main__":
    App().run()

