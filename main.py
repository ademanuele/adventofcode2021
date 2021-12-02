
def main():
    with open('input.txt') as f:
        lines = f.readlines()

        print("Starting...")
        
        x = 0
        d = 0
        a = 0

        for line in lines:
            parts = line.split(" ")
            command = parts[0]
            value = int(parts[1])

            if command == "forward":
                x += value
                d += a * value
            if command == "down":
                a += value
            if command == "up":
                a -= value

        print(x * d)

if __name__ == "__main__":
    main()
