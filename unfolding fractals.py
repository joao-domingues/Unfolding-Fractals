import tkinter as tk
import math

class DragonCurveApp:
    def __init__(self, window, width, height, length):
        #variaveis globais
        self.window = window
        self.width = width
        self.height = height
        self.length = length
        self.canvas = tk.Canvas(window, width=width, height=height, bg="white")
        self.canvas.pack()
        self.iteration = 0
        self.sequence = []  
        self.x, self.y = width // 2, height // 2  
        self.angle = 0  
        self.window.bind("<Button-1>", self.on_click)

    def generate_next_iteration(self):
        if self.iteration == 0:
            self.sequence = [1] 
        else:
            self.sequence = self.sequence + [1] + [-i for i in reversed(self.sequence)]
            #print(self.sequence)
        self.iteration += 1

    def draw_next_segment(self):
        if not self.sequence:
            self.generate_next_iteration()
        for turn in self.sequence:
            self.angle += turn * 90
            angle_radians = math.radians(self.angle)
            new_x = self.x + self.length * math.cos(angle_radians)
            new_y = self.y + self.length * math.sin(angle_radians)
            self.canvas.create_line(self.x, self.y, new_x, new_y, fill="blue")
            print(self.x, self.y, new_x,new_y)
            self.x, self.y = new_x, new_y

    def on_click(self, event):
        self.generate_next_iteration()
        self.draw_next_segment()

def main():
    window = tk.Tk()
    window.title("Dragon's Curve Fractal")
    width = 800
    height = 600
    length = 5 
    app = DragonCurveApp(window, width, height, length)
    window.mainloop()

if __name__ == "__main__":
    main()
