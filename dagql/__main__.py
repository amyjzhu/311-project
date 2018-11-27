from .lexer import Lexer
from .parser import Parser
from .compiler import Compiler
import sys

def main():
    compiler = Compiler()
    while True:
        try:
            text = input("DAGQL> ")
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        parser = Parser(lexer.lex())
        statements = parser.parse() # = Interpreter(parser)
        #resolver = Resolver(compiler)
        #resolver.resolve(statements)
        result = compiler.compile(statements)
        #print([hex(r) for r in result])

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        assert(len(sys.argv) == 2)
        text = open(sys.argv[1]).read() #TODO: make more general, so file can be located anywhere
        statements = Parser(Lexer(text).lex()).parse()
        compiler = Compiler()
        result = compiler.compile(statements)
        print(result)
        #print([hex(r) for r in result])
        #sys.stdout = open("source.yb", "wb")
        # for h in [hex(r) for r in result+[HALT]:
        #    print r
        # f = open(sys.argv[1].rstrip("ysl") + "yb", "wb")
