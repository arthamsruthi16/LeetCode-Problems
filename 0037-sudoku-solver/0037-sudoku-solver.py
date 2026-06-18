class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(r, c, ch):
            return ch not in rows[r] and ch not in cols[c] and ch not in boxes[(r // 3) * 3 + (c // 3)]

        def place_number(r, c, ch):
            board[r][c] = ch
            rows[r].add(ch)
            cols[c].add(ch)
            boxes[(r // 3) * 3 + (c // 3)].add(ch)

        def remove_number(r, c, ch):
            board[r][c] = '.'
            rows[r].remove(ch)
            cols[c].remove(ch)
            boxes[(r // 3) * 3 + (c // 3)].remove(ch)

        def backtrack(pos=0):
            if pos == len(empty_cells):
                return True
            r, c = empty_cells[pos]
            for num in '123456789':
                if is_valid(r, c, num):
                    place_number(r, c, num)
                    if backtrack(pos + 1):
                        return True
                    remove_number(r, c, num)
            return False

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    empty_cells.append((i, j))
                else:
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[(i // 3) * 3 + (j // 3)].add(ch)

        backtrack()