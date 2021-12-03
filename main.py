def main():
    print("Starting...")

    oxygenBinary = ""
    scrubBinary = ""

    with open('input.txt') as f:
        lines = f.readlines()        
        index = 0

        while len(lines) > 1:
            oneCounts = oneCountsAtIndex(lines, index)

            toRemove = "0" if oneCounts >= len(lines) / 2 else "1"
            lines = [x for x in lines if x[index] != toRemove]
            index += 1

        oxygenBinary = lines[0]


    with open('input.txt') as f:
        index = 0
        lines = f.readlines()

        while len(lines) > 1:
            oneCounts = oneCountsAtIndex(lines, index)

            toRemove = "1" if oneCounts >= len(lines) / 2 else "0"
            lines = [x for x in lines if x[index] != toRemove]
            index += 1

        scrubBinary = lines[0]

    oxygen = int(oxygenBinary, 2)
    scrub = int(scrubBinary, 2)
    print(oxygen * scrub)

def oneCountsAtIndex(lines, index):
    oneCountsAtIndex = 0
    for line in lines:                
        bit = line[index]
        if bit == "1":
            oneCountsAtIndex += 1
    return oneCountsAtIndex

if __name__ == "__main__":
    main()
