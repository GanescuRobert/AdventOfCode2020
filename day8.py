
import re


def day8():
    regex = r'(jmp|nop|acc) ([-+]\d+)'
    instructions = []
    jmp_list = []
    nop_list = []
    with open('day8input.txt') as file:
        for data in file:
            values = re.search(regex, data)
            ins = values.group(1)
            arg = values.group(2)

            instructions.append([ins, arg])

            if ins == 'jmp':
                pos = len(instructions)-1
                jmp_list.append(pos)
            if ins == 'nop':
                pos = len(instructions)-1
                nop_list.append(pos)

    notFoundAns = True
    while notFoundAns:
        accumulator = 0
        vis = []
        position = 0
        condition = True
        work = True
        while work:
            if len(instructions) <= position:
                print(accumulator)
                notFoundAns = False
                break
            if position in vis:
                print(accumulator) # ! Comment this for part 2
                work = False
                notFoundAns = False  # ! Comment this for part 2
            else:
                vis.append(position)
                ins, arg = instructions[position]

                # ! Uncomment this for part 2
                """if condition and position in nop_list:
                    ins='jmp'
                    nop_list.remove(position)
                    condition=False
                elif condition and position in jmp_list:
                    ins='nop'
                    jmp_list.remove(position)
                    condition=False"""

                arg = int(arg)
                if ins == 'nop':
                    position += 1
                    continue
                elif ins == 'acc':
                    position += 1
                    accumulator += arg
                elif ins == 'jmp':
                    position += arg
                    continue


day8()
