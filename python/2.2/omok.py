from tkinter import *

class OmokGame:
    def __init__(self, root):
        self.root = root
        self.root.title("오목 게임")
        self.size = 19  # 19x19 보드
        self.cell = 30  # 한 칸 크기
        self.turn = "black"  # 첫 수: 흑
        self.board = [[None]*self.size for _ in range(self.size)]

        # 캔버스 생성
        self.canvas = Canvas(root, width=self.size*self.cell, height=self.size*self.cell, bg="#F5DEB3")
        self.canvas.pack()
        self.draw_board()

        # 클릭 이벤트 연결
        self.canvas.bind("<Button-1>", self.click)

    def draw_board(self):
        # 가로줄
        for i in range(self.size):
            self.canvas.create_line(self.cell/2, self.cell/2 + i*self.cell,
                                    self.size*self.cell - self.cell/2, self.cell/2 + i*self.cell)
        # 세로줄
        for i in range(self.size):
            self.canvas.create_line(self.cell/2 + i*self.cell, self.cell/2,
                                    self.cell/2 + i*self.cell, self.size*self.cell - self.cell/2)

    def click(self, event):
        x = int(round((event.x - self.cell/2)/self.cell))
        y = int(round((event.y - self.cell/2)/self.cell))

        if 0 <= x < self.size and 0 <= y < self.size and not self.board[y][x]:
            cx = self.cell/2 + x*self.cell
            cy = self.cell/2 + y*self.cell
            r = self.cell/2 - 2  # 돌 크기

            self.board[y][x] = self.turn
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=self.turn)

            if self.check_win(x, y):
                self.canvas.unbind("<Button-1>")
                self.canvas.create_text(self.size*self.cell/2, self.size*self.cell/2,
                                        text=f"{self.turn.upper()} 승리!", font=("Arial", 30), fill="red")
            else:
                # 턴 바꾸기
                self.turn = "white" if self.turn == "black" else "black"

    def check_win(self, x, y):
        color = self.board[y][x]

        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for dx, dy in directions:
            count = 1
            # 한쪽 방향
            nx, ny = x+dx, y+dy
            while 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] == color:
                count += 1
                nx += dx
                ny += dy
            # 반대쪽
            nx, ny = x-dx, y-dy
            while 0 <= nx < self.size and 0 <= ny < self.size and self.board[ny][nx] == color:
                count += 1
                nx -= dx
                ny -= dy

            if count >= 5:
                return True
        return False

if __name__ == "__main__":
    root = Tk()
    game = OmokGame(root)
    root.mainloop()


