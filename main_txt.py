import sys
def main_txts():
    def printTape(tape,pointer):
        print("Stan tasmy: ", end = "")
        for element in tape:
            print(f"{element} ", end= "")
        print('\n', ' ' * (pointer*2 + 10), '^')

    def parseFile(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith("alfabet tasmowy:"):
                    alphabet = list(lines[i+1].strip())
                if line.startswith("alfabet wejsciowy:"):
                    input_alphabet = list(lines[i+1].strip())
                if line.startswith("slowo wejsciowe:"):
                    input = list(lines[i+1].strip())
                if line.startswith("stany:"):
                    states = lines[i+1].strip().split()
                if line.startswith("stan poczatkowy:"):
                    begin_state = lines[i+1].strip()
                if line.startswith("stany akceptujace:"):
                    accept_states = list(lines[i+1].strip())
                if line.startswith("relacja przejscia:"):
                    relations = {}
                    for relation in lines[i+1::]:
                        relation = relation.split()
                        relations[(relation[0], relation[1])] = relation[2::]
        return alphabet, input_alphabet, input, states, begin_state, accept_states, relations

    sys.stdout = open("out.txt", "w")
    alphabet, input_alphabet, init_input, states, begin_state, accept_states, relations = parseFile('in.txt')
    tape = init_input + (['#'] * (32 - len(init_input)))
    pointer = 0
    state = begin_state
    printTape(tape,pointer)
    while state not in accept_states:
        next_state, charToWrite, dir = relations[state, tape[pointer]]
        state = next_state
        tape[pointer] = charToWrite
        if dir == 'P':
            if pointer == len(tape) - 1:
                print("Nastepuje rozszerzenie tasmy w prawo")
                tape += ['#'] * 32
            pointer += 1
        elif dir == 'L':
            if pointer == 0:
                tape = ['#'] * 32 + tape
                print("Nastepuje rozszerzenie tasmy w lewo")
                pointer+=32
            pointer -=1
        printTape(tape,pointer)
    print("Slowo poczatkowe: ", end = "")
    for element in init_input:
        print(f"{element} ", end = "")
    print()
    print("Slowo obliczone: ", end = "")
    for element in tape:
        print(f"{element} ", end = "")
    print()
    sys.stdout.close()