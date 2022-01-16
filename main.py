import main_txt
import sys


LimitException=0
def printTape(tape, pointer):
    print("Stan tasmy: ", end="")
    for element in tape:
        print(f"{element} ", end="")
    print('\n', ' ' * (pointer * 2 + 10), '^')


def parseFile(filename):
    global LimitException #odwolanie do Limit Exception
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith("alfabet tasmowy:"):
                try:
                    alphabet = list(lines[i + 1].strip())
                except:
                    print('Problem ze wczytaniem alfabetu tasmowego, Prosze popraw plik')
            if line.startswith("alfabet wejsciowy:"):
                try:
                    input_alphabet = list(lines[i + 1].strip())
                except:
                    print('Problem ze wczytaniem alfabetu wejsciowego, Prosze popraw plik')
            if line.startswith("slowo wejsciowe:"):
                try:
                    input = list(lines[i + 1].strip())
                    if(len(input)>30):
                        print('slowo wejsciowe wieksze niz 32 znaki')
                        print('Popraw swoj plik')
                        LimitException+=1
                except:
                    print('Problem ze wczytaniem slowa wejsciowego, Prosze popraw plik')
            if line.startswith("stany:"):
                try:
                    states = lines[i + 1].strip().split()
                    if (len(states) > 50):
                        print('wiecej niz  50 stanow')
                        print('Popraw swoj plik')
                        LimitException += 1
                except:
                    print('Problem ze wczytaniem stanow, Prosze popraw plik')
            if line.startswith("stan poczatkowy:"):
                try:
                    begin_state = lines[i + 1].strip()
                except:
                    print('Problem ze wczytaniem stanu poczatkowego, Prosze popraw plik')
            if line.startswith("stany akceptujace:"):
                try:
                    accept_states = list(lines[i + 1].strip())
                except:
                    print('Problem ze wczytaniem stanu akceptujacego, Prosze popraw plik')
            if line.startswith("relacja przejscia:"):
                try:
                    relations = {}
                    for relation in lines[i + 1::]:
                        relation = relation.split()
                        relations[(relation[0], relation[1])] = relation[2::]
                except:
                    print('Problem ze wczytaniem stanu akceptujacego, Prosze popraw plik')
    return alphabet, input_alphabet, input, states, begin_state, accept_states, relations


alphabet, input_alphabet, init_input, states, begin_state, accept_states, relations = parseFile('file.txt')
if(LimitException>0): #IF to help detect bad value
    print('LimitException')
    print('Nacinij dowolny klawisz...')
    input()
    sys.exit()
tape = init_input + (['#'] * (32 - len(init_input)))
pointer = 0
state = begin_state
printTape(tape, pointer)
print("Aby przejsc do kolejnego kroku wcisnij enter, aby przejsc do konca obliczen wprowadz 's'")
skip = False
while state not in accept_states:
    if not skip:
        c = input()
        if c == 's':
            skip = True
    try:
        next_state, charToWrite, dir = relations[state, tape[pointer]]
        state = next_state
        tape[pointer] = charToWrite
    except:
        print('Nierozpoznana relacja przejscia, sprawdz swoj plik wejsciowy jescze raz')
        input()
        sys.exit()
    if dir == 'P':
        if pointer == len(tape) - 1:
            print("Nastepuje rozszerzenie tasmy w prawo")
            tape += ['#'] * 32
        pointer += 1
    elif dir == 'L':
        if pointer == 0:
            tape = ['#'] * 32 + tape
            print("Nastepuje rozszerzenie tasmy w lewo")
            pointer += 32
        pointer -= 1
    printTape(tape, pointer)

print("Slowo poczatkowe: ", end="")
for element in init_input:
    print(f"{element} ", end="")
print()
print("Slowo obliczone: ", end="")
for element in tape:
    print(f"{element} ", end="")
print()
#Jesli wszystko Ok wczytujemy funkcje i zapisujemy do pliku out.txt
main_txt.main_txts()