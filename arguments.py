import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help='A string input', dest = 'string_input', type=str)
    parser.add_argument(help='An integer input', dest = 'int_input', type=int)
    parser.add_argument(help='A float input', dest = 'float_input', type=float)

    args = parser.parse_args()

    print(f'String input: {args.string_input}')
    print(f'Integer input: {args.int_input}')
    print(f'Float input: {args.float_input}')

if __name__ == '__main__':
    main()