import tkinter as tk
from tkinter.filedialog import askopenfile 
import PyPDF2
import subprocess, sys

def open_file(entry):
    """Open file dialog that allows user to chose file"""
    entry.delete(0, 'end')
    file = askopenfile(mode ='r', filetypes =[('PDF Files', '*.pdf')])
    if file is not None: 
        entry.insert(0, file.name)
		

def join_files():
    """Merge the files into a single pdf"""
    files = [ent_1.get(), ent_2.get()]
    out_writer = PyPDF2.PdfFileWriter()
    for file in files:
        pdf_file = open(file, 'rb')
        file_reader = PyPDF2.PdfFileReader(pdf_file)
        for page in range(file_reader.numPages):
            pageObj = file_reader.getPage(page)
            out_writer.addPage(pageObj)

    output_file_name = result_entry.get()
    output_file = open(output_file_name, 'wb')
    out_writer.write(output_file)
    output_file.close()
    pdf_file.close()
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, output_file_name])
    clear_labels()

def clear_labels():
    ent_1.delete(0, 'end')
    ent_2.delete(0, 'end')
    result_entry.delete(0, 'end')

window = tk.Tk()
window.title("JoinPDF")

# first file
form_1 = tk.Frame(master=window)
label_1 = tk.Label(master=form_1, text="File URL:", width=10)
ent_1 = tk.Entry(master=form_1, width=30)
btn_1 = tk.Button(master=form_1, text="Open", command= lambda:open_file(ent_1))
btn_1.config(width=10)

label_1.grid(row=0, column=0, sticky="w")
ent_1.grid(row=0, column=1, sticky="w")
btn_1.grid(row=0, column=2, sticky="w", padx=(10,0))

# seconf file
form_2 = tk.Frame(master=window)
label_2 = tk.Label(master=form_2, text="File URL:", width=10)
ent_2 = tk.Entry(master=form_2, width=30)
btn_2 = tk.Button(master=form_2, text="Open", command= lambda:open_file(ent_2))
btn_2.config(width=10)

label_2.grid(row=0, column=0, sticky="w")
ent_2.grid(row=0, column=1, sticky="w")
btn_2.grid(row=0, column=2, sticky="w", padx=(10,0))

# result form
result_form = tk.Frame(master=window)
result_label = label_2 = tk.Label(master=result_form, text="File name:", width=10)
result_entry = tk.Entry(master=result_form, width=30)

# button to join files
btn_join = tk.Button(master=result_form, text="JOIN", command=join_files)
btn_join.config(width=10)

result_label.grid(row=0, column=0, sticky="w")
result_entry.grid(row=0, column=1, sticky="w")
btn_join.grid(row=0, column=2, sticky="w", padx=(10,0))

# Grid build
form_1.grid(row=0, column=0, pady=10, padx=10, sticky="w")
form_2.grid(row=1, column=0, pady=10, padx=10, sticky="w")
result_form.grid(row=2, column=0, pady=(50,10), padx=10, sticky="w")

files = [ent_1.get(), ent_2.get()]

window.mainloop()
