import tkinter as tk
from tkinter import Canvas, Button, messagebox, Frame
from PIL import Image, ImageDraw

class SignatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Signature Pad")
        self.root.geometry("500x350")  # Increased window size
        self.root.configure(bg="#ADD8E6")  # Light blue background

        self.canvas_width = 400
        self.canvas_height = 200
        
        # Create a frame for the canvas and buttons
        self.frame = Frame(root, bg="#ADD8E6")
        self.frame.pack(pady=20)

        # Create a canvas for drawing with a light beige background
        self.canvas = Canvas(self.frame, width=self.canvas_width, height=self.canvas_height, bg='#F6EEE3', bd=2, relief='groove')
        self.canvas.pack()

        # Create buttons with improved styling
        self.button_save = Button(root, text="Save Signature", command=self.save_signature, bg="#4CAF50", fg="black", font=("Arial", 12, "bold"), padx=10, pady=5)
        self.button_save.pack(pady=5)

        self.button_clear = Button(root, text="Clear", command=self.clear_canvas, bg="#f44336", fg="black", font=("Arial", 12, "bold"), padx=10, pady=5)
        self.button_clear.pack(pady=5)

        # Bind mouse events for drawing
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Initialize image for saving the signature
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.last_x, self.last_y = None, None

    def paint(self, event):
        x, y = event.x, event.y
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line((self.last_x, self.last_y, x, y), fill='black', width=2)
            self.draw.line((self.last_x, self.last_y, x, y), fill='black', width=2)
        self.last_x, self.last_y = x, y

    def reset(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def save_signature(self):
        file_path = "signature.png"
        self.image.save(file_path)
        messagebox.showinfo("Signature Saved", f"Your signature has been saved as {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureApp(root)
    root.mainloop()