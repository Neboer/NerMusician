from typing import List

from note import Note, Last


def parse(input_stream: str) -> List[Note]:
    pitch = 0
    head = 0
    notes: List[Note] = []
    while head < len(input_stream):
        prev_symbol = input_stream[head - 1] if head > 1 else None
        current_symbol = input_stream[head]

        p = head + 1  # 1) 2//1 )2//1（ 2
        while p < len(input_stream) and input_stream[p] in ')]':
            p += 1
        if p == len(input_stream):  # 扫描到了队尾，说明没有下个有意义的符号了
            next_meaningful_symbol = None
        else:
            next_meaningful_symbol = input_stream[p]
        if current_symbol in "1234567":
            notes.append(Note(int(current_symbol), prev_symbol == '#', pitch, Last.from_suffix(next_meaningful_symbol)))
        elif current_symbol in '(]':
            pitch += 1
        elif current_symbol in ')[':
            pitch -= 1
        head += 1
    return notes


if __name__ == '__main__':
    input_string = '''2#12(23#12)6 #467 6 #4\n3#45#435#47(#12)(#1)#5#67(#1)\n4#4(23#12)6 #467 6 #4\n3#4567(#123#45#43#12)7'''
    print(''.join([str(x) for x in parse(input_string)]))
