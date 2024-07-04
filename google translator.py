from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
import tkinter as tk
import tkinter.font as tkFont

root = Tk()
root.title("Google Translator")
root.geometry("1080x500")
root.resizable(False, False)
root.configure(bg='#f0f0f0')

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    t1 = googletrans.Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)

# icon
image_icon = PhotoImage(file="google.png")
root.iconphoto(False, image_icon)

# arrow
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=465, y=1)

language = googletrans.LANGUAGES
languageV = list(language.values())

# First combobox
combo1 = ttk.Combobox(root, values=languageV, font=("Rockwell", 16), state="r")
combo1.place(x=130, y=20)
combo1.set("English")

label1 = Label(root, text="English", font=("Rockwell", 16, "bold"), bg="#f0f0f0", fg="#003366", width=18, bd=5, relief=GROOVE)
label1.place(x=130, y=60)

# Second combobox
combo2 = ttk.Combobox(root, values=languageV, font=("Rockwell", 16), state="r")
combo2.place(x=700, y=20)
combo2.set("Select Language")

label2 = Label(root, text="Select Language", font=("Rockwell", 16, "bold"), bg="#f0f0f0", fg="#003366", width=18, bd=5, relief=GROOVE)
label2.place(x=700, y=60)

# First frame
f = Frame(root, bg="#003366", bd=5, relief=GROOVE)
f.place(x=10, y=120, width=520, height=250)

text1 = Text(f, font=("Rockwell", 16), bg="white", fg="#003366", relief=GROOVE, wrap=WORD, bd=0)
text1.place(x=0, y=0, width=510, height=240)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Second frame
f1 = Frame(root, bg="#003366", bd=5, relief=GROOVE)
f1.place(x=550, y=120, width=520, height=250)

text2 = Text(f1, font=("Rockwell", 16), bg="white", fg="#003366", relief=GROOVE, wrap=WORD, bd=0)
text2.place(x=0, y=0, width=510, height=240)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font=("Rockwell", 16, "bold"), activebackground="white", cursor="hand2", bd=1, width=10, height=2, bg="#003366", fg="white", command=translate_now)
translate.place(x=466, y=400)

label_change()

root.mainloop()
