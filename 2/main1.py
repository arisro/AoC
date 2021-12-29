import sys
import typing as t

def read_stdin() -> t.Generator[str, None, None]:
    for line in sys.stdin:
        if 'q' == line.rstrip():
            break

        yield line

if __name__ == '__main__':
    # horizontal, depth
    position = [0, 0]

    moves = {
        'forward': lambda pos, change: [pos[0] + change, pos[1]],
        'down': lambda pos, change: [pos[0], pos[1] + change],
        'up': lambda pos, change: [pos[0], pos[1] - change],
    }

    for line in read_stdin():
        data = line.split()
        position = moves[data[0]](position, int(data[1]))

    print(f'Answer: {position[0] * position[1]}')