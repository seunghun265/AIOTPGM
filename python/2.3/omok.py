import tkinter as tk
import copy

BOARD_SIZE = 9
CELL = 50
RADIUS = 20
EMPTY, BLACK, WHITE = 0, 1, 2

class GoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("9x9 바둑 - 사람 vs AI (중급)")

        self.canvas = tk.Canvas(root, width=BOARD_SIZE*CELL, height=BOARD_SIZE*CELL, bg="#DDB87D")
        self.canvas.pack()

        self.reset_btn = tk.Button(root, text="🔄 재시작", command=self.reset)
        self.reset_btn.pack(pady=5)

        self.board = [[EMPTY]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.turn = BLACK  # 사람은 흑
        self.draw_board()
        self.canvas.bind("<Button-1>", self.human_move)

    def reset(self):
        self.canvas.delete("all")
        self.board = [[EMPTY]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.turn = BLACK
        self.draw_board()

    def draw_board(self):
        for i in range(BOARD_SIZE):
            x = CELL//2 + i*CELL
            self.canvas.create_line(x, CELL//2, x, CELL*(BOARD_SIZE-0.5))
            self.canvas.create_line(CELL//2, x, CELL*(BOARD_SIZE-0.5), x)

    def human_move(self, e):
        if self.turn != BLACK:
            return
        x = round((e.x - CELL//2) / CELL)
        y = round((e.y - CELL//2) / CELL)
        if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
            return
        if self.board[y][x] != EMPTY:
            return
        if not self.is_legal(x, y, BLACK):
            return
        self.place(x, y, BLACK)
        self.turn = WHITE
        self.root.after(300, self.ai_move)

    def ai_move(self):
        best_score = -9999
        best_move = None
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.board[y][x] == EMPTY and self.is_legal(x, y, WHITE):
                    score = self.evaluate(x, y, WHITE)
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)
        if best_move:
            self.place(best_move[0], best_move[1], WHITE)
        self.turn = BLACK

    def place(self, x, y, color):
        self.board[y][x] = color
        self.draw_stone(x, y, color)
        self.remove_captured(3 - color)

    def draw_stone(self, x, y, color):
        cx = CELL//2 + x*CELL
        cy = CELL//2 + y*CELL
        fill = "black" if color == BLACK else "white"
        self.canvas.create_oval(cx-RADIUS, cy-RADIUS, cx+RADIUS, cy+RADIUS, fill=fill)

    def neighbors(self, x, y):
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                yield nx, ny

    def group_and_liberties(self, x, y, board):
        color = board[y][x]
        stack = [(x, y)]
        group = set(stack)
        liberties = set()
        while stack:
            cx, cy = stack.pop()
            for nx, ny in self.neighbors(cx, cy):
                if board[ny][nx] == EMPTY:
                    liberties.add((nx, ny))
                elif board[ny][nx] == color and (nx, ny) not in group:
                    group.add((nx, ny))
                    stack.append((nx, ny))
        return group, liberties

    def remove_captured(self, color):
        removed = False
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.board[y][x] == color:
                    group, libs = self.group_and_liberties(x, y, self.board)
                    if not libs:
                        for gx, gy in group:
                            self.board[gy][gx] = EMPTY
                            self.canvas.delete(f"stone_{gx}_{gy}")
                        removed = True
        return removed

    def is_legal(self, x, y, color):
        temp = copy.deepcopy(self.board)
        temp[y][x] = color
        _, libs = self.group_and_liberties(x, y, temp)
        if libs:
            return True
        # 자살 수면 상대 돌 잡는지 확인
        for nx, ny in self.neighbors(x, y):
            if temp[ny][nx] == 3 - color:
                g, l = self.group_and_liberties(nx, ny, temp)
                if not l:
                    return True
        return False

    def evaluate(self, x, y, color):
        score = 0
        for nx, ny in self.neighbors(x, y):
            if self.board[ny][nx] == 3 - color:
                g, l = self.group_and_liberties(nx, ny, self.board)
                if len(l) == 1:
                    score += 50  # 따먹기
            if self.board[ny][nx] == color:
                score += 5  # 연결
        return score

if __name__ == "__main__":
    root = tk.Tk()
    GoGame(root)
    root.mainloop()