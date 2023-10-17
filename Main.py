from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("600x750")
window.title("Ceaser Cipher GUI")

# TOP PART
frame_top = Frame(window, height=375)
frame_top.pack(fill="both", expand=True)

# SEPARATOR
separator = ttk.Separator(window, orient="horizontal")
separator.pack(fill="x", padx=0, pady=0)

# BOTTOM PART
frame_bottom = Frame(window, height=375)
frame_bottom.pack(fill="both", expand=True)

# STYLE
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#1b1c1b")
frame_top.config(background="#1b1c1b")
frame_bottom.config(background="#1b1c1b")


alphabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o',
            'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w',
            'x', 'y', 'z', 'ź', 'ż', 'a', 'ą', 'b', 'c', 'ć',
            'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's',
            'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']



# BUTTON ENCRYPT
def encryptClick():
    encryptText = normalText.get()
    encryptCode = encryptText.replace(" ", "").lower()
    shift_encrypt_value = int(clicked_encrypt.get())
    cipher_text = ""
    for letter in encryptCode:
        position = alphabet.index(letter)
        new_position = (position + shift_encrypt_value) % len(alphabet)
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    encText.config(text=cipher_text)


encrypt = Button(frame_top,
                 text="ENCRYPT",
                 command=encryptClick,
                 font=("Comic Sans", 20),
                 fg="#1b1c1b",
                 bg="#117827",
                 activeforeground="#1b1c1b",
                 activebackground="#117827")
encrypt.pack(side="top", pady=20)


# TEXT BLOCK BEFORE ENCRYPT
normalText = Entry(frame_top,
                   font="Arial, 20",
                   fg="#1b1c1b",
                   bg="#117827")
normalText.pack(side="top", pady=20)


# NUMBER CHOOSE FOR ENCRYPTION
shift_encrypt = [str(i) for i in range(1, 35)]
clicked_encrypt = StringVar()
clicked_encrypt.set(shift_encrypt[0])

drop_encrypt = OptionMenu(frame_top,
                  clicked_encrypt, *shift_encrypt)
drop_encrypt.config(bg="#117827")
drop_encrypt["menu"].config(bg="#117827")
drop_encrypt.pack(side="top", pady=20)


# TEXT BLOCK AFTER ENCRYPT
encText = Label(frame_top,
                text="",
                font="Arial, 19",
                width=20,
                height=1,
                fg="#1b1c1b",
                bg="#117827"
                )
encText.pack(side="top", pady=20)



# BUTTON DECRYPT
def decryptClick():
    decryptText = secretText.get()
    decryptCode = decryptText.replace(" ", "").lower()
    shift_decrypt_value = int(clicked_decrypt.get())
    plain_text = ""
    for letter in decryptCode:
        position = alphabet.index(letter)
        new_position = (position - shift_decrypt_value) % len(alphabet)
        new_letter = alphabet[new_position]
        plain_text += new_letter
    decText.config(text=plain_text)

decrypt = Button(frame_bottom,
                 text="DECRYPT",
                 command=decryptClick,
                 font=("Comic Sans", 20),
                 fg="#1b1c1b",
                 bg="#117827",
                 activeforeground="#1b1c1b",
                 activebackground="#117827")
decrypt.pack(side="top", pady=20)


# TEXT BLOCK BEFORE DECRYPT
secretText = Entry(frame_bottom,
                   font="Arial, 20",
                   fg="#1b1c1b",
                   bg="#117827")
secretText.pack(side="top", pady=20)


# NUMBER CHOOSE FOR DECRYPT
shift_decrypt = [str(i) for i in range(1, 35)]
clicked_decrypt = StringVar()
clicked_decrypt.set(shift_decrypt[0])

drop_decrypt = OptionMenu(frame_bottom,
                  clicked_decrypt, *shift_decrypt,)
drop_decrypt.config(bg="#117827")
drop_decrypt["menu"].config(bg="#117827")
drop_decrypt.pack(side="top", pady=20)


# TEXT BLOCK AFTER DECRYPT
decText = Label(frame_bottom,
                text="",
                font="Arial, 19",
                width=20,
                height=1,
                fg="#1b1c1b",
                bg="#117827")
decText.pack(side="top", pady=20)


# AUTHOR BLOCK
author_text = Label(frame_bottom,
                text="Piotr Hazior",
                font="Arial, 10",
                width=10,
                height=1,
                fg="#1b1c1b",
                bg="#117827")
author_text.pack(side="left", pady=0)

window.mainloop()