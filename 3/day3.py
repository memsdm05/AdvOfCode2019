# BOUNDS
# HiX  HiY   LoX  LoY
# 4423 2553 -6695 4423

def buildMap(w, h):
    arr = [[0 for x in range(w)] for y in range(h)]
    return arr

def importWires():
    f = open("day3_input.txt", "r")
    newStuff = []
    for i in f.readlines():
        newStuff.append(i.strip())
    f.close()
    return newStuff

def part1():
    wires = importWires()
    wMap = buildMap(500, 500)
    stuff = 0
    midX = len(wMap)//2
    midY = len(wMap)//2
    for w in wires:
        stuff += 1
        wire = w.split(",")
        x = midX
        y = midY
        for mv in wire:
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
                wMap[y][x] = stuff
    for row in wMap:
        print(row)




if __name__ == '__main__':
    part1()
