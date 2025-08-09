from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator")


root.iconbitmap("passwordgenerator.ico")
root.geometry("600x300")
root.resizable(False , False)

lf = LabelFrame(root, text="How Many Characters?")
lf.pack(padx= 20 ,pady=20)

label = Label(lf, text="Enter length:")
label.pack(padx=10, pady=10)

box = Entry(label, border=5)
box.pack(padx=20, pady=10)

resultlabel = Text(root, height=1, width=30, font=("Arial", 12), wrap="none")
resultlabel.insert("1.0", "",  "center")
resultlabel.tag_configure("center", justify=CENTER)
resultlabel.config(state="disabled")  # Düzenlemeyi kapat
resultlabel.pack(pady=20)

def generatepass():
    length = int(box.get())
    mypass = ""
    for _ in range(length):
        mypass += chr(randint(33, 126))

    resultlabel.config(state="normal")        # Düzenlemeyi aç
    resultlabel.delete("1.0", END)             # eski metni sil
    resultlabel.insert("1.0", mypass, "center")  # yeni şifreyi yaz
    resultlabel.config(state="disabled")      # Düzenlemeyi kapat
    print(mypass)



def copy():
    text = resultlabel.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

btn_frame = Frame(root)
btn_frame.pack(pady=20)  

btn1 = Button(btn_frame, text="Generate Password", command=generatepass)
btn1.pack(side=LEFT, padx=20)  
btn2 = Button(btn_frame, text="Copy to clipboard", command=copy)
btn2.pack(side=LEFT, padx=20)






root.mainloop()
