from Compiler import Compiler


def main():
    compiler = Compiler()
    compiler.read()
    compiler.parse()
    compiler.visit()
    compiler.save_graph()


if __name__ == "__main__":
    main()
