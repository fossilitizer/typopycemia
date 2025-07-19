from argparse import ArgumentParser
from random import shuffle
from pathlib import Path
from string import ascii_letters

def shuffle_buffer(buffer: list[str], doubles: bool=False, bifrucate: bool=False) -> list[str]:
    # Preserve double letter proximity, 
    # but allow them to move around as a pair
    if doubles:
        paired_buffer = []
        last = None
        for c in buffer:
            if c == last:
                paired_buffer.append(paired_buffer.pop()*2)
                last = None
                continue
            paired_buffer.append(c)
            last = c
        buffer = paired_buffer

    fl = buffer[0]
    ll = buffer[-1]
    ml = buffer[1:-1]
    if bifrucate:
        ml1 = ml[:len(ml)//2]
        ml2 = ml[len(ml)//2:]
        shuffle(ml1)
        shuffle(ml2)
        ml = ml1 + ml2
    else:
        shuffle(ml)
    return [fl, *ml, ll]

def encode(text: str | Path, doubles: bool=False, bifrucate: bool=False) -> str:
    if Path(text).exists():
        text = Path(text).read_text()
    chars = []
    buffer = []
    for char in text:
        # Register characters to buffer
        # Only execute the shuffle when a non-ascii 
        # character is found
        if char in ascii_letters:
            buffer.append(char)
            continue

        # Only shuffle words with > 3 charaters
        if len(buffer) > 3:
            buffer = shuffle_buffer(buffer, doubles, bifrucate)
        
        # Add the shuffled buffer and the new charater 
        # to the output
        chars.extend(buffer)
        chars.append(char)
        buffer.clear()
    
    # Add remaining buffer contents
    if buffer:
        buffer = shuffle_buffer(buffer, doubles, bifrucate)
        chars.extend(buffer)

    # Join and return the charater list
    return ''.join(chars)

def main():
    parser = ArgumentParser(
        prog='Typopycemia',
        usage='Inucrtode topys like nveer brfoee',
        description=
        (
            'Input string is split on non-ascii letters and each run has all middle letters shuffled '
            '(e.g. Hello, World! -> Hlelo, Wrlod!)'
        ),
    )

    parser.add_argument('input', 
                        help='Filename or string to typoglycemiafy')
    parser.add_argument('-d', '--doubles', action='store_true', 
                        help='Preserve double letters like "ee" and "ll"')
    parser.add_argument('-b', '--bifrucate', action='store_true', 
                        help='Dont send letters to the other side of the word "adhominem" -> a+?[dhom]? + ?[ine]?+m each part shuffled then joined')
    args = parser.parse_args()
    print(encode(args.input, args.doubles, args.bifrucate))

if __name__ == "__main__":
    main()