import tkinter as tk

root = tk.Tk()

HEIGHT = 800

WIDTH = 800



def wordchange(event = None):
	word1 = entry.get()
	word2 = entry1.get()
	text1.delete("1.0","end-1c")
	text1.insert("1.0", text.get("1.0", "end").replace(word1, word2))




root.title("Word Changer")


canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

text = tk.Text(root)
text.place(rely = 0, relx = 0.05, relheight = 0.3, relwidth = 0.9)

entry = tk.Entry(root)
entry.place(rely = 0.32, relx = 0.35, relheight = 0.05, relwidth = 0.6)

entry1 = tk.Entry(root)
entry1.place(rely = 0.39, relx = 0.35, relheight = 0.05, relwidth = 0.6)

label = tk.Label(root, text = "Find text :", font = ("Helvetica", 11))
label.place(rely = 0.32, relx = 0.01, relheight = 0.05, relwidth = 0.31)

label2 = tk.Label(root, text = "Replace with:", font = ("Helvetica", 11))
label2.place(rely = 0.39, relx = 0.01, relheight = 0.05, relwidth = 0.31)

text1 = tk.Text(root)
text1.place(rely = 0.48, relx = 0.05, relheight = 0.48, relwidth = 0.9)

root.bind("<KeyRelease>", wordchange)



root.mainloop()