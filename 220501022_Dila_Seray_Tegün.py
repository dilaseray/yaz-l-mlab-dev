import tkinter as tk
import random

class BallAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Ball Animation")

        # Canvas creation
        self.canvas = tk.Canvas(root, width=400, height=500, bg="lightgray")
        self.canvas.pack()

        # Buttons
        self.add_ball_button = tk.Button(root, text="Add Ball", command=self.add_ball, bg="green")
        self.add_ball_button.pack(side=tk.LEFT, padx=10)

        self.start_button = tk.Button(root, text="START", command=self.start_animation, bg="red")
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="STOP", command=self.stop_animation, bg="blue")
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="RESET", command=self.reset_canvas, bg="yellow")
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.speed_up_button = tk.Button(root, text="Speed Up", command=self.speed_up)
        self.speed_up_button.pack(side=tk.LEFT, padx=10)

        # Ball tracking and animation status
        self.balls = []
        self.running = False
        self.speed = 5

        # Ball options for user selection
        self.size_var = tk.IntVar(value=20)
        self.color_var = tk.StringVar(value="red")

        # Size selection
        tk.Label(root, text="Size:").pack(side=tk.LEFT)
        tk.Radiobutton(root, text="Small", variable=self.size_var, value=20).pack(side=tk.LEFT)
        tk.Radiobutton(root, text="Medium", variable=self.size_var, value=30).pack(side=tk.LEFT)
        tk.Radiobutton(root, text="Large", variable=self.size_var, value=40).pack(side=tk.LEFT)

        # Color selection
        tk.Label(root, text="Color:").pack(side=tk.LEFT)
        tk.Radiobutton(root, text="Red", variable=self.color_var, value="red").pack(side=tk.LEFT)
        tk.Radiobutton(root, text="Yellow", variable=self.color_var, value="yellow").pack(side=tk.LEFT)
        tk.Radiobutton(root, text="Blue", variable=self.color_var, value="blue").pack(side=tk.LEFT)

    def add_ball(self):
        # Create a ball with user-selected size and color
        size = self.size_var.get()
        color = self.color_var.get()
        self.create_ball(size, color)

    def create_ball(self, size=None, color=None):
        # Create a ball with specified size and color
        if size is None:
            size = random.choice([20, 30, 40])
        if color is None:
            color = random.choice(["red", "green", "blue"])
        x = random.randint(size, 400 - size)
        y = random.randint(size, 500 - size)
        ball = self.canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
        dx = random.choice([-self.speed, self.speed])
        dy = random.choice([-self.speed, self.speed])
        self.balls.append((ball, dx, dy))

    def start_animation(self):
        if not self.running:
            self.running = True
            self.animate()

    def stop_animation(self):
        self.running = False

    def reset_canvas(self):
        self.running = False
        for ball, _, _ in self.balls:
            self.canvas.delete(ball)
        self.balls = []

    def speed_up(self):
        self.speed += 2
        # Update the speed of all existing balls
        self.balls = [(ball, random.choice([-self.speed, self.speed]), random.choice([-self.speed, self.speed])) for ball, _, _ in self.balls]

    def animate(self):
        if self.running:
            for i in range(len(self.balls)):
                ball, dx, dy = self.balls[i]
                coords = self.canvas.coords(ball)
                if coords[0] <= 0 or coords[2] >= 400:
                    dx = -dx
                if coords[1] <= 0 or coords[3] >= 500:
                    dy = -dy
                self.canvas.move(ball, dx, dy)
                self.balls[i] = (ball, dx, dy)

            self.root.after(50, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = BallAnimation(root)
    root.mainloop()
