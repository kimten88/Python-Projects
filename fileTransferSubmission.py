import shutil
import os
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd


#create the GUI
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height =True)
        self.master.title('Copy/Update Files')
        

        self.source = StringVar()
        self.destination = StringVar()

        #text fields where the paths will be displayed
        self.Browse1 = Entry(self.master,text=self.source, font=("Helvetica",16), fg ='black')
        self.Browse1.grid(row=1 , column=3, padx=(10, 0), pady=(30, 0) )
    
        self.Browse2 = Entry(self.master,text=self.destination, font=("Helvetica",16), fg ='black')
        self.Browse2.grid(row=2 , column=3, padx=(10, 0), pady=(30, 0) )    

        #buttons to summon the paths to the directories
        self.btnBrowse1 = Button(self.master, text="From...", width = 15, command = self.sourceName)
        self.btnBrowse1.grid(row=1 , column=1, padx=(0, 0), pady=(30, 0))

        self.btnBrowse2 = Button(self.master, text="To...", width = 15, command = self.destinationName)
        self.btnBrowse2.grid(row=2 , column=1, padx=(0, 0), pady=(30, 0))

        #button to execute file copies
        self.btnSubmit = Button(self.master, text="Submit", width = 15, height = 2, command = self.submit)
        self.btnSubmit.grid(row=3 , column=1, padx=(10, 0), pady=(20, 0))
        
        #close GUI window
        self.btnCancel = Button(self.master, text="Close Program", width = 15, height = 2, command = self.cancel)
        self.btnCancel.grid(row=3 , column=3, padx=(0, 0), pady=(20, 10), sticky=SE)


    
    def sourceName(self):
        #set where the source of the files are, global variable used so it can be referenced in other functions
        global source
        source = fd.askdirectory()
        self.Browse1.insert("0", source)
        print(source)
            

    def destinationName(self):
        #set the destination path, global variable used so it can be referenced in other functions
        global destination
        destination = fd.askdirectory()
        self.Browse2.insert("0", destination)
        print(destination)


    def submit(self):
        #to find the directory where we are looking for the files
        files = os.listdir(source)
        print(files)
        for file in files:
            #list the files from the source folder
            sourceFile = os.path.join(source, file)
            print(sourceFile)
            #if this file does not exist or modified less than 24 hours ago copy the file to the Destination folder. 24hrs = 86,400 seonds st_mtime is measured in seconds
            if (not os.path.exists(destination)) or (os.stat(source).st_mtime - os.stat(destination).st_mtime < 86400) :
                    #we are saying copy the files represented by 'i' to their new destination
                shutil.copy(sourceFile, destination)

    #function to close GUI
    def cancel(self):
        self.master.destroy()


                

if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
