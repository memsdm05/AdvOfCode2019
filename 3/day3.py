# BOUNDS
# HiX  HiY   LoX  LoY
# 4423 2553 -6695 4423

def importWires():
    f = open("day3_input.txt", "r")
    newStuff = []
    for i in f.readlines():
        newStuff.append(i.strip())
    f.close()
    return newStuff

def part1():
    wires = importWires()
    st = 0
    a = []
    b = []
    for w in wires:
        st += 1
        wire = w.split(",")
        for mv in wire:
            x = 0
            y = 0
            drc = mv[0]
            dst = int(mv[1:])
            for i in range(dst):
                if drc == "R":
                    x += 1
                elif drc == "L":
                    x -= 1
                elif drc == "U":
                    y -= 1
                elif drc == "D":
                    y += 1

                if st == 2:
                    b.append((x, y))
                else:
                    a.append((x, y))

    shit = 0
    for coord in b:
        if coord in a:
            shit += 1
            print(coord)

    print(len(a), flush=True)
    print(shit)




if __name__ == '__main__':
    part1()
