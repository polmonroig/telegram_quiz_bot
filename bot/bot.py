from BotTalker import BotTalker
import pickle



def main():
    TOKEN = open('token.txt').read().strip()
    talker = BotTalker(TOKEN)
    talker.add_commands()
    talker.init()



if __name__ == "__main__":
    main()