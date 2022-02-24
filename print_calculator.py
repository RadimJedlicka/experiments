def print_calculator(*args, **kwargs):
    pole = '+---'
    length = kwargs['line_length']
    radek = f'{length * pole}+'

    for _ in args:
        print(radek)
        print(f"| {' | '.join(args[:length])} |")
        args = args[length:]

        if len(args) <= length:
            print(radek)
            print(f"| {' | '.join(args[:length])} |".center(len(radek)))
            print(f"{pole * len(args)}+".center((len(radek))))
            break


print_calculator('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '/', '*', line_length=3)
