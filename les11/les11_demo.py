import tkinter as tk

def on_click():
    input_text = entry.get()
    label['text'] = "Hello, " + input_text


root = tk.Tk()

label = tk.Label(master=root,
                 text="Hello World",
                 background="red",
                 foreground="blue",
                 font=('Arial', 24))
label.pack()

img = tk.PhotoImage(file='naruto.png')
img_label = tk.Label(master=root, image=img)
img_label.pack()

button = tk.Button(master=root,
                   text="Don't click this...",
                   command=on_click
                   )
button.pack()

entry = tk.Entry(master=root)
entry.pack()

# Grid manager
# for row in range(5):
#     for col in range(10):
#         label = tk.Label(master=root, text=f"{row}-{col}")
#         label.grid(row=row, column=col)

root.mainloop()
