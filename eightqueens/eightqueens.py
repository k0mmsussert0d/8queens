from multiprocessing import Queue


def find_path(n: int, events_queue: Queue = None):

    def get_empty_board(size: int):
        """Returns 2D n*n array, each value initialized with false"""
        return [[False for i in range(size)] for j in range(size)]

    def count_queens(board):
        count = 0
        for row in board:
            for field in row:
                if field is True:
                    count = count + 1

        return count

    def is_field_safe(row: int, col: int, board: list):
        if board[row][col] is True:
            return False

        for i in board[row]:
            if i is True:
                return False

        row_check = row - 1
        col_check = col - 1
        while row_check >= 0 and col_check >= 0:
            if board[row_check][col_check] is True:
                return False
            row_check = row_check - 1
            col_check = col_check - 1

        row_check = row + 1
        col_check = col - 1
        while row_check <= len(board) - 1 and col_check >= 0:
            if board[row_check][col_check] is True:
                return False
            row_check = row_check + 1
            col_check = col_check - 1

        return True

    def print_board(board):
        for col in board:
            for i, row in enumerate(col):
                if row:
                    print(len(col) - i, end='')

    def solve(board, col):
        if count_queens(board) == n:
            if events_queue:
                events_queue.put({'board': board})
                events_queue.put({'state': 'finished'})
            print_board(board)
            return board

        for row in range(len(board)):
            if is_field_safe(row, col, board):
                board[row][col] = True

                if solve(board, col + 1):
                    return True

                board[row][col] = False

        return False

    return solve(get_empty_board(n), 0)