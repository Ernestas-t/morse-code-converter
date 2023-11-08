from tkinter import *
import customtkinter
from CTkMessagebox import CTkMessagebox

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
morse_code = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
    '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
    '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
    '-.--', '--..'
]


def convert():
    converted = []
    if radio_var.get() == 1:
        output.delete("0.0", "end")
        for character in entry.get("0.0", "end").lower():
            if character in alphabet:
                index = alphabet.index(character)
                converted.append(morse_code[index])
            elif character == ' ':
                converted.append('/')
            else:
                converted.append(character)
        output.insert(END, ' '.join(converted))
    elif radio_var.get() == 2:
        output.delete("0.0", "end")
        morse_entry = entry.get("0.0", "end").split(' ')
        for character in morse_entry:
            if character in morse_code:
                index = morse_code.index(character)
                converted.append(alphabet[index])
            elif character == '/':
                converted.append(' ')
            else:
                converted.append(character)
        output.insert(END, ''.join(converted))
    else:
        CTkMessagebox(title="Error", message="Please select the conversion type", icon="cancel", justify='center')


app = customtkinter.CTk()
app.geometry("350x600")
app.config(padx=25, pady=20)

radio_var = IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(app, text="Encode", variable=radio_var, value=1)
radiobutton_2 = customtkinter.CTkRadioButton(app, text="Decode", variable=radio_var, value=2)

radiobutton_1.grid(column=0, row=0)
radiobutton_2.grid(column=1, row=0, sticky=E)

entry = customtkinter.CTkTextbox(app, width=300, font=('Helvetica', 15))
entry.grid(column=0, row=1, pady=20, columnspan=2)

button = customtkinter.CTkButton(app, text="Convert", command=convert)
button.grid(column=0, row=2, columnspan=2)

output = customtkinter.CTkTextbox(app, width=300, font=('Helvetica', 15))
output.grid(column=0, row=3, pady=20, columnspan=2)

app.mainloop()
