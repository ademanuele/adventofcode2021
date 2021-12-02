
def main():
    with open('input.txt') as f:
        lines = f.readlines()

        print("Starting...")
        
        x = 0
        d = 0

        for line in lines:
            parts = line.split(" ")
            command = parts[0]
            value = int(parts[1])

            if command == "forward":
                x += value
            if command == "down":
                d += value
            if command == "up":
                d -= value

        print(x * d)

if __name__ == "__main__":
    main()
