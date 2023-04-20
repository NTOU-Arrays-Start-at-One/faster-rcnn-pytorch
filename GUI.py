import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

class ImageCompareGUI:
    def __init__(self, img_data1, img_data2):
        self.image1 = Image.fromarray(np.uint8(img_data1))
        self.image2 = Image.fromarray(np.uint8(img_data2))
        self.root = tk.Tk()
        self.root.title("ImageCompare")
        self.canvas = tk.Canvas(self.root, width=800, height=400)
        self.canvas.pack()
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.image1_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo1)
        self.image2_id = self.canvas.create_image(400, 0, anchor=tk.NW, image=self.photo2)
        self.line_id = self.canvas.create_line(400, 0, 400, 400, fill="red", width=2)
        self.canvas.tag_bind(self.line_id, "<B1-Motion>", self.move_line)

    def move_line(self, event):
        self.canvas.coords(self.line_id, event.x, 0, event.x, 400)
        line_x = event.x
        self.canvas.coords(self.image1_id, 0, 0, line_x, 400)
        self.canvas.coords(self.image2_id, line_x, 0, 800, 400)

    def run(self):
        self.root.mainloop()