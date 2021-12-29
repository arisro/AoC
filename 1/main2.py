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
    windows = []

    for sdepth in read_stdin():
        depth = int(sdepth)

        if len(windows) < 3:
            windows.append([])

        [w.append(depth) for w in windows]

        if len(windows[0]) == 3:
            win_depth = sum(windows.pop(0))
            if last_depth > -1 and win_depth > last_depth:
                increases += 1

            last_depth = win_depth

    print(f'Result: {increases}')