from gui import GUI
from algorithm_bot import Bot


def main():
    bot = Bot()
    gui = GUI()

    gui.add_bot(bot)



if __name__ == "__main__":
    main()