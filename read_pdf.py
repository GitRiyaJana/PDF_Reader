from tkinter import *
import PyPDF2
from tkinter import filedialog
import pyttsx3

root = Tk()
root.title('Come - Read PDF!')
root.geometry("750x500")
root.configure(bg="sky blue")

Label(root,text="LET'S MAKE OUR TIME MORE USEFUL",font=('Boulder 18'),bg='teal',pady=10,padx=10).pack()

Label(root,bg='sky blue',fg='maroon',pady=10).pack()

Label(root,text="Choose Voice: Enter '1' for Female and '0' for Male:",font=('Calibri 15'),bg='sky blue',fg='maroon',pady=20).pack()

def select_voice():
    x = int(voice.get())
    i = int(page_no.get())
    e_d = int(a.get())
    y = int(r.get())
    open_file = filedialog.askopenfilename(
        initialdir="/",
        title="Open PDF File",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")))

    pdf_file = PyPDF2.PdfReader(open_file)

    pages = len(pdf_file.pages)
    player = pyttsx3.init()
    player.setProperty('engine', 'flite')
    voices = player.getProperty('voices')
    rate = player.getProperty('rate')
    for num in range(i - 1, pages):
        if e_d == 0:
            player.setProperty('rate', rate - 50 - y)
        else:
            player.setProperty('rate', rate - 50 + y)

        if x == 0:
            player.setProperty('voice', voices[0].id)  # male voice
        else:
            player.setProperty('voice', voices[1].id)  # female voice

        player.setProperty('volume', 2.0)
        page = pdf_file.pages[num]
        text = page.extract_text().split('\n')
        player.say(text)
        player.runAndWait()

voice = Entry(root, width=25)
voice.pack()

Label(root,text="Choose Page number from where you want to read from: ",font=('Calibri 15'),bg='sky blue',fg='maroon',pady=20).pack()
page_no = Entry(root, width=25)
page_no.pack()

Label(root,text="Enter '1' for Increase and '0' for Decrease: ",font=('Calibri 15'),bg='sky blue',fg='maroon',pady=20).pack()
a = Entry(root, width=25)
a.pack()

Label(root,text="Choose Reading Rate (between 10 to 50): ",font=('Calibri 15'),bg='sky blue',fg='maroon',pady=20).pack()
r = Entry(root, width=25)
r.pack()

Label(root,bg='sky blue',fg='maroon',pady=10).pack()

b1 = Button(root, text='CHOOSE PDF & PLAY', command=select_voice).pack()

root.mainloop()

