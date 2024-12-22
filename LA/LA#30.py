import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter Widgets")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack(pady=20)

def display_text():
    print("My favorite anime is Haikyuu")
    
button = tk.Button(root, text="run", command=display_text)
button.pack(pady=10)

root.mainloop()