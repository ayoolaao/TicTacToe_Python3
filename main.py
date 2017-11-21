import random


class TicTacToe:
    def __init__(self):
        self.status = ""
        self.count = 0
        self.icon = ""
        self.cell = ""
        self.storage_db = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

    def board(self):
        print("The board looks like this: \n")
        print("{} | {} | {}\n---------\n{} | {} | {}\n---------\n{} | {} | {}\n\n".format(self.storage_db["1"],
                                                                                          self.storage_db["2"],
                                                                                          self.storage_db["3"],
                                                                                          self.storage_db["4"],
                                                                                          self.storage_db["5"],
                                                                                          self.storage_db["6"],
                                                                                          self.storage_db["7"],
                                                                                          self.storage_db["8"],
                                                                                          self.storage_db["9"]))

    def set_icon(self):
        if self.count % 2 == 0:
            self.icon = "O"
        else:
            self.icon = "X"

    def get_icon(self):
        return self.icon

    def set_cell(self):
        if self.icon == "X":
            self.cell = input("What cell number d you want (1- 9)? ")
        else:
            self.random_play()

    def set_storage_db(self):
        while True:
            self.set_cell()
            if self.storage_db[self.cell] == " ":
                self.storage_db[self.cell] = self.icon
                return
            else:
                pass
                # print("Cell already taken")
                # return False

    def get_storage_db(self):
        return self.storage_db

    def random_play(self):
        self.cell = str(random.randint(1, 9))

    def set_status(self):
        if self.storage_db["1"] == self.storage_db["2"] == self.storage_db["3"]:
            self.status = self.storage_db["1"]
        elif self.storage_db["4"] == self.storage_db["5"] == self.storage_db["6"]:
            self.status = self.storage_db["4"]
        elif self.storage_db["7"] == self.storage_db["8"] == self.storage_db["9"]:
            self.status = self.storage_db["7"]
        elif self.storage_db["1"] == self.storage_db["4"] == self.storage_db["7"]:
            self.status = self.storage_db["1"]
        elif self.storage_db["2"] == self.storage_db["5"] == self.storage_db["8"]:
            self.status = self.storage_db["2"]
        elif self.storage_db["3"] == self.storage_db["6"] == self.storage_db["9"]:
            self.status = self.storage_db["3"]
        elif self.storage_db["1"] == self.storage_db["5"] == self.storage_db["9"]:
            self.status = self.storage_db["1"]
        elif self.storage_db["3"] == self.storage_db["5"] == self.storage_db["7"]:
            self.status = self.storage_db["3"]
        else:
            self.status = ""

    def get_status(self):
        return self.status


def instructions():
    print("Welcome to Tic Tac Toe\n")
    print("Use the following cell numbers to make your move: \n")
    print("The board looks like this: \n")

    print("1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n\n")


if __name__ == '__main__':
    instructions()
    game1 = TicTacToe()
    begin = input("Are you ready to play? (Y or N): ").upper()

    if begin == "Y" or begin == "YES":
        while True:
            game1.set_icon()
            game1.set_storage_db()
            game1.board()
            game1.set_status()
            game1.count += 1

            if game1.get_status() == "X":
                print("You Won!!\n")
                break

            elif game1.get_status() == "O":
                print("You Lost the game\n")
                break

            elif game1.count == 9:
                print("Game is a TIE\n")
                break

            else:
                pass

    else:
        print("Goodbye")
