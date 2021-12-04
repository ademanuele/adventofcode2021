from os import stat


def main():
    print("Starting...")

    with open('input.txt') as f:
        lines = f.readlines()

        drawNumbers = lines[0].split(",")
        boardLines = []
        boards = []

        for i in range(2, len(lines)):
            if lines[i] == "\n":
                boards.append(BingoBoard(boardLines))
                boardLines = []
                continue
            
            boardLines.append(lines[i])

        drawn = []
        for number in drawNumbers:
            print("Playing: " + number)
            drawn.append(int(number))
            for b in boards:
                b.play(int(number))
                if b.hasWon():
                    print(drawn)
                    print(b.lines)
                    print(b.unmarkedSum(drawn))
                    print(b.unmarkedSum(drawn) * int(number))
                    print("Done")
                    exit()

class BingoBoard:
    def __init__(self, lines):
        self.lines = list(map(BingoBoard._toArrayRow, lines))
        self._drawnColumns = [0] * 5
        self._drawnRows = [0] * 5

    @staticmethod
    def _toArrayRow(rowString) -> list[int]:
        row = list(map(lambda s: s.strip(), rowString.split(" ")))
        row = list(filter(lambda x: x != "", row))        
        return list(map(lambda s: int(s), row))

    def play(self, number):
        for i in range(5):
            for j in range(5):                
                if self.lines[i][j] == number:
                    self._drawnColumns[j] += 1
                    self._drawnRows[i] += 1                    

    def hasWon(self) -> bool:
        return 5 in self._drawnColumns or 5 in self._drawnRows        

    def unmarkedSum(self, drawnNumbers) -> int:
        boardNumbers = []
        for row in self.lines:
            for number in row:
                boardNumbers.append(number)
        
        unmarked = list(filter(lambda n: n not in drawnNumbers, boardNumbers))
        return sum(unmarked)
        
if __name__ == "__main__":
    main()
