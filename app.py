import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Application(tk.Frame):
	MAIN_WINDOW_WIDTH = 1000
	MAIN_WINDOW_HEIGHT = 600

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		
		self.toolbarIcons = {}

		self.master.minsize(width=self.MAIN_WINDOW_WIDTH, height=self.MAIN_WINDOW_HEIGHT)
		self.pack()
		self._createMainMenu()
		self._createToolbar()

	# private methods

	def _createMainMenu(self):
		mainMenu = tk.Menu(self)
		self.master.config(menu=mainMenu)

		fileMenu = tk.Menu(mainMenu, tearoff=False)
		mainMenu.add_cascade(label="File", menu=fileMenu)

		fileMenu.add_command(label="New")
		fileMenu.add_command(label="Open")
		fileMenu.add_command(label="Save")
		fileMenu.add_command(label="Save as")
		fileMenu.add_command(label="Print")
		fileMenu.add_separator()
		fileMenu.add_command(label="Exit", command=self.quit)

		editMenu = tk.Menu(mainMenu, tearoff=False)
		mainMenu.add_cascade(label="Edit", menu=editMenu)

		editMenu.add_command(label="Cut")
		editMenu.add_command(label="Copy")
		editMenu.add_command(label="Paste")
		editMenu.add_command(label="Rename")
		editMenu.add_separator()
		editMenu.add_command(label="Preferences")

		helpMenu = tk.Menu(mainMenu, tearoff=False)
		mainMenu.add_cascade(label="Help", menu=helpMenu)

		helpMenu.add_command(label="About", command=self._showAboutWindow)

	def _createToolbar(self):
		toolbar = tk.Frame(self, relief=tk.SUNKEN)

		previewButton = tk.Button(toolbar, text="Preview")
		previewButton.pack(side=tk.LEFT, fill=tk.Y)

		nextButton = tk.Button(toolbar, text="Next")
		nextButton.pack(side=tk.LEFT, fill=tk.Y)

		self.toolbarIcons["full_size"] = tk.PhotoImage(file="icons/fullsize.png")
		fullSizeButton = tk.Button(toolbar, image=self.toolbarIcons["full_size"])
		fullSizeButton.pack(side=tk.LEFT)

		self.toolbarIcons["plus"] = tk.PhotoImage(file="icons/plus.png")
		plusButton = tk.Button(toolbar, image=self.toolbarIcons["plus"])
		plusButton.pack(side=tk.LEFT)

		self.toolbarIcons["minus"] = tk.PhotoImage(file="icons/minus.png")
		minusButton = tk.Button(toolbar, image=self.toolbarIcons["minus"])
		minusButton.pack(side=tk.LEFT)

		self.toolbarIcons["delete"] = tk.PhotoImage(file="icons/delete.png")
		deleteButton = tk.Button(toolbar, image=self.toolbarIcons["delete"])
		deleteButton.pack(side=tk.LEFT)

		commentButton = tk.Button(toolbar, text="Comment", command=self._photoCommentWindow)
		commentButton.pack(side=tk.LEFT, fill=tk.Y)

		self.toolbarIcons["arrow_down"] = tk.PhotoImage(file="icons/arrow_down.png")
		settingsDropdownButton = tk.Menubutton(toolbar, text="Settings", image=self.toolbarIcons["arrow_down"], compound=tk.RIGHT)

		settingsMenu = tk.Menu(settingsDropdownButton, tearoff=False)
		settingsDropdownButton.config(menu=settingsMenu)

		settingsMenu.add_checkbutton(label="Exposure")
		settingsMenu.add_checkbutton(label="Color")

		settingsDropdownButton.pack(side=tk.LEFT, fill=tk.Y)

		toolbar.pack(side=tk.TOP, fill=tk.X)

	def _showAboutWindow(self):
		tk.messagebox.showinfo("About", "Velichko Stoev made this using TkInter!")

	def _photoCommentWindow(self):
		tk.simpledialog.askstring("Comment the picture", "Your comment")


root = tk.Tk()
app = Application(master = root)
app.master.title("Velichko's UI")
root.mainloop()
