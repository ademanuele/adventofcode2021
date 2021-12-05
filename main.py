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
        winning_boards = []
        for number in drawNumbers:
            print("Playing: " + number)
            drawn.append(int(number))
            for b in boards:
                if b.hasWon():
                    continue

                b.play(int(number))

                if b.hasWon():
                    winning_boards.append(b)
                    print("Winner: " + str(b.lines))

        last_winning_board = winning_boards[-1]        
        print("Last winning: " + str(last_winning_board.lines))
        print(last_winning_board.unmarkedSum())
        print("Done")
                    

class BingoBoard:
    def __init__(self, lines):
        self.lines = list(map(BingoBoard._toArrayRow, lines))
        self._drawnColumns = [0] * 5
        self._drawnRows = [0] * 5
        self._playedNumbers = []

    @staticmethod
    def _toArrayRow(rowString) -> list[int]:
        row = list(map(lambda s: s.strip(), rowString.split(" ")))
        row = list(filter(lambda x: x != "", row))        
        return list(map(lambda s: int(s), row))

    def play(self, number):
        self._playedNumbers.append(number)
        for i in range(5):
            for j in range(5):                
                if self.lines[i][j] == number:
                    self._drawnColumns[j] += 1
                    self._drawnRows[i] += 1                    

    def hasWon(self):
        return 5 in self._drawnColumns or 5 in self._drawnRows        

    def unmarkedSum(self):
        boardNumbers = []
        for row in self.lines:
            for number in row:
                boardNumbers.append(number)
        
        unmarked = list(filter(lambda n: n not in self._playedNumbers, boardNumbers))
        s = sum(unmarked)
        winning_number = self._playedNumbers[len(self._playedNumbers) - 1]
        return s * winning_number
        
if __name__ == "__main__":
    main()
