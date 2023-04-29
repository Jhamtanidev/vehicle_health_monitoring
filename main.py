import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Create some data to plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data on the axis object
ax.plot(x, y)

# Create a Tkinter window
root = tk.Tk()

# Create a Tkinter canvas widget to display the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Pack the canvas widget into the Tkinter window
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
root.mainloop()