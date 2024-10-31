from datetime import datetime

class SpookyGreeting:
    def __init__(self):
        self.today = datetime.now().date()

    def greet(self):
        if self.today.month == 10 and self.today.day == 31:
            print("🎃 Happy Halloween! 🎃")
        else:
            print("It's not Halloween yet, but stay spooky! 👻")

if __name__ == "__main__":
    greeting = SpookyGreeting()
    greeting.greet()
