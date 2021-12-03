def main():
    print("Starting...")
    index = 0

    with open('input.txt') as f:
        lines = f.readlines()
        oxygenLines = lines

        while len(oxygenLines) > 1:
            oneCountsAtIndex = 0

            for line in oxygenLines:                
                bit = line[index]
                if bit == "1":
                    oneCountsAtIndex += 1

            toRemove = "1" if oneCountsAtIndex >= len(oxygenLines) / 2 else "0"
            oxygenLines = filter(lambda l: l[index] == toRemove, oxygenLines)
            index += 1

    index = 0

    with open('input.txt') as f:
        lines = f.readlines()
        scrubberLines = lines

        while len(scrubberLines) > 1:
            oneCountsAtIndex = 0

            for line in scrubberLines:                
                bit = line[index]
                if bit == "1":
                    oneCountsAtIndex += 1

            toRemove = "1" if oneCountsAtIndex >= len(scrubberLines) / 2 else "0"
            scrubberLines = filter(lambda l: l[index] == toRemove, scrubberLines)
            index += 1

    print(oxygenLines)
    print(scrubberLines)

if __name__ == "__main__":
    main()
