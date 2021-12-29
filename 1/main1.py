import sys
import typing as t

def read_stdin() -> t.Generator[str, None, None]:
    for line in sys.stdin:
        if 'q' == line.rstrip():
            break

        yield line

if __name__ == '__main__':
    increases = 0
    last_depth = -1

    for depth in read_stdin():
        if last_depth > -1 and int(depth) > last_depth:
            increases += 1

        last_depth = int(depth)

    print(f'Answer: {increases}')