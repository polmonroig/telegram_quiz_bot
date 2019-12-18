from Compiler import Compiler


def main():
    compiler = Compiler()
    compiler.read()
    compiler.parse()
    compiler.visit()




if __name__ == "__main__":
    main()
