from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk,Image
import glob
import os
import time

master = Tk()
master.title("Slide Show")

#Get Images
imageDir = os.path.dirname(os.path.abspath(__file__)) + '/images'
imageList = glob.glob(imageDir + '/*.jpeg')
imageCounter = 0

#File types
files = [('All Files', '*.*'), ('Images', '*.jpeg')]

#Main Menu
mainMenu = Menu(master)

#Callback function- for saving files
def saveAs():
	global imageDir
	global imageList
	global imageCounter
	global files

	saveFile = asksaveasfile(mode='w', filetypes = files, defaultextension = files)
	if saveFile:
		img1 = Image.open(imageList[imageCounter])
		img1.save(saveFile)
		imageList = glob.glob(imageDir + '/*.jpeg')
	saveFile.close()

#Create the submenu 
fileMenu = Menu(master)
fileMenu.add_command(label="Save As..", command=saveAs)
mainMenu.add_cascade(label="File", menu=fileMenu)

#Add the rest of the menu options to the main menu
mainMenu.add_command(label="Quit", command=master.destroy)
master.config(menu=mainMenu)

#Add Image
img = ImageTk.PhotoImage(Image.open(imageList[imageCounter]))
canvasImage = Canvas(master, width = 200, height = 200)
canvasImage.create_image(20, 20, anchor=NW, image=img)
canvasImage.grid(row=0, column=1)

#Function to show images
def showImage():
	global imageCounter
	global imageList
	global canvasImage
	global master

	img = ImageTk.PhotoImage(Image.open(imageList[imageCounter]))
	canvasImage.create_image(20, 20, anchor=NW, image=img)
	nameLabel = Label(text=os.path.basename(imageList[imageCounter]), relief=SUNKEN, width=10, height=2, padx=1, pady=1)
	nameLabel.grid(row=1,column=1)
	master.mainloop()

#Callback function- to view previous image
def previousImage():
	global imageCounter

	imageCounter -= 1
	showImage()

#Callback function- to view next image
def nextImage():
	global imageCounter

	if imageCounter == len(imageList)-1:
		imageCounter = 0
	else:
		imageCounter += 1
	showImage()


#Add Buttons
nameLabel = Label(text=os.path.basename(imageList[imageCounter]), relief=SUNKEN, width=10, height=2, padx=1, pady=1)
nameLabel.grid(row=1,column=1)
previousButton = ttk.Button(master, text="←", command=previousImage)
previousButton.grid(row=1, column=0)
nextButton = ttk.Button(master, text="→", command=nextImage)
nextButton.grid(row=1, column=2)

master.mainloop()