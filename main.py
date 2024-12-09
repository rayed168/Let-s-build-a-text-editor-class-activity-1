from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window=Tk()
window.title("My first text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
	"""Open a file for editing."""
	filepath = askopenfilename(
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
	if not filepath:
		return
	txt_edit.delete(1.0, END)
	with open(filepath, "r") as input_file:
		text = input_file.read()
		txt_edit.insert(END, text)
		input_file.close()
	window.title(f"Codingal's Text Editor - {filepath}")

          
def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")

txt_edit=Text(master=window)
frame1=Frame(master=window,relief=RAISED,bd=2)
open_button=Button(master=frame1,text="Open file",command=open_file)
save_as_button=Button(master=frame1,text="Save as",command=save_file)

open_button.grid(row=0,column=0,sticky="ew",padx=5,pady=10)
save_as_button.grid(row=1,column=0,sticky="ew",padx=5)
frame1.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()