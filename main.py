
def main():
    with open('input.txt') as f:
        lines = f.readlines()

        print("Starting...")
        count = 0
        previous = int(lines[0])

        for line in lines:
            depth = int(line)
            if depth > previous:
                count += 1
            previous = depth
        
        print(count)

if __name__ == "__main__":
    main()
