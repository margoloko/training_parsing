import sys
import argparse


MURZIK = '=^..^=______/'


if __name__ == '__main__':
    # Инициализация парсера аргументов с описанием.
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    parser.add_argument('name', help='Name')
    parser.add_argument('-s', '--surname', help='Familia')
    parser.add_argument('-c', '--city', help='gorod', choices=['Chekhov', 'Dublin', 'Minsk', 'Simbirsk'],)
    parser.add_argument('-m', '--murzik', help='send_kot', action='store_true')
    # Извлечение аргументов командной строки в переменную args.
    args = parser.parse_args() 
    parts = []
    parts.append(f'hello, {args.name}')
    if args.surname is not None:
        parts.append(args.surname)
    if args.city is not None:
        parts.append(f'from {args.city}')
    if args.murzik is not None:
        parts.append(MURZIK)
    print(*parts)