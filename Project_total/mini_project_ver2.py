import tkinter as tk
import random, math

배경색, 글자색, 강조색 = "#1f1f39", "#b3e7f4", "#e94560"
basic_font, font = ("Georgia", 15), ("Georgia", 20, "bold")

figurelist = {
    "원":     ("#3498db", "circle"),
    "네모":   ("#f39c12", "square"),
    "세모":   ("#9b59b6", "triangle"),
    "육각형": ("#1abc9c", "hexagon"),
    "타원":   ("#e67e22", "oval"),
}

round, display_time, Empty_time = 18, 1200, 300


def drow(canvas, figurename):
    canvas.delete("all")
    color, kind = figurelist[figurename]
    cx, cy, r = 110, 110, 75
    if kind == "circle":
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color, outline="")
    elif kind == "square":
        canvas.create_rectangle(cx-r, cy-r, cx+r, cy+r, fill=color, outline="")
    elif kind == "triangle":
        canvas.create_polygon([cx, cy-r, cx-r, cy+r, cx+r, cy+r], fill=color, outline="")
    elif kind == "oval":
        canvas.create_oval(cx-r, cy-45, cx+r, cy+45, fill=color, outline="")
    elif kind == "hexagon":
        point = []
        for i in range(6):
            angular = math.radians(i*60 - 30)
            point += [cx + r*math.cos(angular), cy + r*math.sin(angular)]
        canvas.create_polygon(point, fill=color, outline="")


class game:
    def __init__(self, 창):
        self.basic_window = 창
        self.basic_window.title("인지 검사")
        self.basic_window.geometry("700x520")
        self.basic_window.config(bg=배경색)
        self.basic_window.resizable(False, False)
        self.window = tk.Frame(창, bg=배경색)
        self.window.pack(fill="both", expand=True)
        self.total = 0
        self.starting_window()

    def 화면초기화(self):
        for 위젯 in self.window.winfo_children():
            위젯.destroy()

    def label(self, 텍스트, 폰트=basic_font, 색=글자색, **kw):
        return tk.Label(self.window, text=텍스트, font=폰트, bg=배경색, fg=색, **kw)

    def 버튼(self, 텍스트, 색, 동작):
        return tk.Button(self.window, text=텍스트, font=basic_font, bg=색, fg="white",
                         relief="flat", padx=22, pady=6, command=동작)

    # ── 시작 화면 ───────────────────────────────────────────
    def starting_window(self):
        self.화면초기화()
        self.label("인지 검사", font).pack(pady=40)
        self.label("1. 도형 2-back  |  2. 좌우 개수 비교").pack()
        self.버튼("시작", 강조색, self.도형게임).pack(pady=30)

    # ── 1. 도형 2-back ──────────────────────────────────────
    def 도형게임(self):
        self.화면초기화()
        self.도형순서 = [random.choice(list(figurelist)) for _ in range(round)]
        self.현재순서, self.도형점수, self.응답기록 = 0, 0, {}

        self.label("1. 도형 2-back", font).pack(pady=14)
        self.label("2번째 전과 같으면 [맞다], 다르면 [아니다]",
                 색="#aaa", 폰트=("Georgia", 12)).pack()

        self.도형캔버스 = tk.Canvas(self.window, width=220, height=220,
                                   bg=배경색, highlightthickness=0)
        self.도형캔버스.pack(pady=14)

        self.순서표시 = self.label("")
        self.순서표시.pack()

        버튼프레임 = tk.Frame(self.window, bg=배경색)
        버튼프레임.pack(pady=12)

        def O():
            self.save(True)

        def X():
            self.save(False)

        tk.Button(버튼프레임, text="맞다", font=basic_font, bg="#27ae60", fg="white",
                  relief="flat", padx=22, pady=6, command=O).pack(side="left", padx=10)
        tk.Button(버튼프레임, text="아니다", font=basic_font, bg="#c0392b", fg="white",
                  relief="flat", padx=22, pady=6, command=X).pack(side="left", padx=10)

        self.next_figure()

    def next_figure(self):
        if self.현재순서 >= round:
            for i in range(2, round):
                정답 = self.도형순서[i] == self.도형순서[i-2]
                if self.응답기록.get(i, False) == 정답:
                    self.도형점수 += 10
            self.total += self.도형점수
            self.좌우게임()
            return
        drow(self.도형캔버스, self.도형순서[self.현재순서])
        self.순서표시.config(text=f"{self.현재순서+1}/{round}")
        self.basic_window.after(display_time, self.도형지우기)

    def 도형지우기(self):
        self.도형캔버스.delete("all")
        self.현재순서 += 1
        self.basic_window.after(Empty_time, self.next_figure)

    def save(self, 값):
        if self.현재순서 >= 2 and self.현재순서 not in self.응답기록:
            self.응답기록[self.현재순서] = 값










    # ── 2. 좌우 개수 비교 ───────────────────────────────────
    def 좌우게임(self):
        self.화면초기화()
        self.좌우라운드, self.좌우점수, self.응답완료 = 1, 0, False

        self.label("2. 좌우 개수 비교", font).pack(pady=14)
        self.라운드표시 = self.label("")
        self.라운드표시.pack()

        self.좌우캔버스 = tk.Canvas(self.window, width=640, height=260,
                                   bg="#0f0f1e", highlightthickness=0)
        self.좌우캔버스.pack(pady=10)

        버튼프레임 = tk.Frame(self.window, bg=배경색)
        버튼프레임.pack(pady=10)
        for 텍스트, 방향, 색 in [("왼쪽", "left", "#2980b9"), ("오른쪽", "right", "#8e44ad")]:
            tk.Button(버튼프레임, text=텍스트, font=basic_font, bg=색, fg="white",
                      relief="flat", padx=22, pady=6,
                      command=lambda d=방향: self.좌우정답확인(d)).pack(side="left", padx=10)

        self.좌우화면그리기()

    def 좌우화면그리기(self):
        if self.좌우라운드 > 5:
            self.total += self.좌우점수
            self.결과화면()
            return
        self.응답완료 = False
        self.좌우캔버스.delete("all")
        self.좌우캔버스.create_line(320, 0, 320, 260, fill="#444", width=2)
        기준 = 8 + self.좌우라운드 * 2
        if random.choice([True, False]):
            왼쪽수, 오른쪽수, self.정답방향 = 기준+3, 기준, "left"
        else:
            왼쪽수, 오른쪽수, self.정답방향 = 기준, 기준+3, "right"
        for _ in range(왼쪽수):
            x, y = random.randint(20, 290), random.randint(20, 240)
            self.좌우캔버스.create_oval(x, y, x+10, y+10, fill="#3498db", outline="")
        for _ in range(오른쪽수):
            x, y = random.randint(340, 610), random.randint(20, 240)
            self.좌우캔버스.create_oval(x, y, x+10, y+10, fill="#e74c3c", outline="")
        self.라운드표시.config(text=f"라운드 {self.좌우라운드}/5  |  더 많은 쪽은?")

    def 좌우정답확인(self, 방향):
        if self.응답완료:
            return
        self.응답완료 = True
        if 방향 == self.정답방향:
            self.좌우점수 += 10
        self.좌우라운드 += 1
        self.basic_window.after(700, self.좌우화면그리기)








    # ── 결과 화면 ───────────────────────────────────────────
    def game_reset(self):
        self.total = 0
        self.starting_window()

    def 결과화면(self):
        self.화면초기화()
        self.label("결과", font).pack(pady=40)
        self.label(f"도형 2-back : {self.도형점수}/ 180 점\n"
                 f"좌우 비교   : {self.좌우점수}/ 50 점\n\n"
                 f"총점 : {self.total}점",
                 폰트=("Georgia", 17), justify="center").pack(pady=20)
        self.버튼("다시 하기", 강조색, self.game_reset).pack(pady=10)
        self.버튼("종료", "#555", self.basic_window.destroy).pack()






## 해당 파일이 다른 파일에 import 될 때는
## 아래코드가 실행되지 않음
if __name__ == "__main__":
    창 = tk.Tk()
    game(창)
    창.mainloop()