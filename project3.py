import grin
from grin import interpreter

def read_grin_program() -> iter:
    """Reads lines of input from the standard input until the end-of-program marker is encountered."""
    lines = []
    while True:
        line = input()
        if line == '.':
            break
        lines.append(line)
    return iter(lines)

def main():
    """The main entry point for the Grin interpreter."""
    try:
        program_lines = read_grin_program()
        tokens_per_line = grin.parse(program_lines)
        interpreter.interpret(tokens_per_line)
    except grin.GrinLexError as e:
        print(e)
    except grin.GrinParseError as e:
        print(e)
    except interpreter.GrinRuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()