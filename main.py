
def main():
    with open('input.txt') as f:
        lines = f.readlines()

        print("Starting...")
        
        oneCounts = [0] * (len(lines[0]) - 1)

        for line in lines:
            for i in range(len(line)):
                bit = line[i]
                if bit == "1":
                    oneCounts[i] += 1

        gammaC = map(lambda c: "1" if c > len(lines) / 2 else "0", oneCounts)
        gamma = "".join(str(x) for x in gammaC)
        gammaInt = int(gamma, 2)

        epsilonC = map(lambda c: "0" if c > len(lines) / 2 else "1", oneCounts)
        epsilon = "".join(str(x) for x in epsilonC)
        epsilonInt = int(epsilon, 2)

        print(oneCounts)
        print(gammaC)
        print(gammaInt)
        print(epsilonInt)
        print(gammaInt * epsilonInt)

if __name__ == "__main__":
    main()
