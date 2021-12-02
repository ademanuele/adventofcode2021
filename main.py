
def main():
    with open('input.txt') as f:
        lines = map(lambda l: int(l), f.readlines())

        print("Starting...")
        count = 0
        previousTotal = lines[0] + lines[1] + lines[2]

        for i in range(len(lines) - 2):            
            currentTotal = lines[i] + lines[i + 1] + lines[i + 2]
                    
            if currentTotal > previousTotal:
                count += 1

            previousTotal = currentTotal
        
        print(count)

if __name__ == "__main__":
    main()
