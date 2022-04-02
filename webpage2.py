import webbrowser
import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("Body of the Webpage")
frame.geometry('400x200')

# Function for getting Input from textbox and printing it at label widget
def textInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)

    #html process in textImput function to allow local variable to be wildcarded into the string           
    f = open("webpage.html", "w")
    f.write("<html><body><h1>Stay tuned for our amazing summer sale!</h1> {} </body></html>".format(inp))
    f.close()

    #location of the file
    url = 'webpage.html'

    #opens in new tab
    webbrowser.open_new_tab(url)


# TextBox Creation
inputtxt = tk.Text(frame,height = 5, width = 20)
inputtxt.pack()

# Button Creation
submitButton = tk.Button(frame, text = "Submit", command = textInput)
submitButton.pack()

#Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()






frame.mainloop()
