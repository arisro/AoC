import sys
import typing as t

def read_stdin() -> t.Generator[str, None, None]:
    for line in sys.stdin:
        if 'q' == line.rstrip():
            break

        yield line.rstrip()

if __name__ == '__main__':
    bit_counts: t.List[t.List[int]] = []

    for line in read_stdin():
        data = list(map(int, list(line)))

        if len(bit_counts) == 0:
            [bit_counts.append([0, 0]) for _ in range(len(data))]

        for i, bit in enumerate(data):
            bit_counts[i][bit] += 1

    gamma_rate_str = ''
    epsilon_date_str = ''
    for pos in bit_counts:
        gamma_rate_str += '0' if pos[0] > pos[1] else '1'
        epsilon_date_str += '1' if pos[0] > pos[1] else '0'

    print(f'Answer: {int(gamma_rate_str, 2) * int(epsilon_date_str, 2)}')