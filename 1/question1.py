# take its mass, divide by three, round down, and subtract 2
import math

def part1():
    f = open("input.txt", "r")
    fuel = 0
    for i in f.readlines():
        fuel += math.floor(int(i.strip())/3)-2
    f.close()
    return fuel

def recursiveFuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    return fuel + recursiveFuel(fuel)

def part2():
    f = open("input.txt", "r")
    total = 0
    for i in f.readlines():
        total += recursiveFuel(int(i.strip()))
    f.close()
    return total



if __name__ == '__main__':
    print(part1())
    print(part2())