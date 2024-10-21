import sys
from antlr4 import *
from compiladorLexer import compiladorLexer
from compiladorParser import compiladorParser

from CustomListener import CustomListener
from CustomErrorListener import CustomErrorListener
from CustomVisitor import CustomVisitor


def main(argv):
    archivo = "./input/programa.txt"
    if len(argv) > 1:
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladorParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    listener = CustomListener()
    parser.addParseListener(listener)

    tree = parser.programa()
    # print(tree.toStringTree(recog=parser))

    # walker = CustomVisitor()
    # walker.visitPrograma(tree)


if __name__ == "__main__":
    main(sys.argv)
