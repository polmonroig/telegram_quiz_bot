from BotTalker import BotTalker


def main():
    TOKEN = open('token.txt').read().strip()
    talker = BotTalker(TOKEN)
    talker.init()


if __name__ == "__main__":
    main()
