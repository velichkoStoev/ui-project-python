import tkinter as tk

class MainMenu(tk.Menu):
	def __init__(self, frame = None):
		super().__init__(frame)
		frame.master.config(menu = self)

	def addFileMenu(self):
		fileMenuOptions = ["New", "Open", "Save", "Save as", "Print"]
		fileMenuOptionsCount = len(fileMenuOptions)

		fileMenu = tk.Menu(self, tearoff=False)
		self.add_cascade(label="File", menu=fileMenu)

		for i in range(fileMenuOptionsCount):
			fileMenu.add_command(label=fileMenuOptions[i])

		fileMenu.add_separator()
		fileMenu.add_command(label="Exit", command=self.quit)

	def addEditMenu(self):
		editMenuOptions = ["Cut", "Copy", "Paste", "Rename", "Preferences"]
		editMenuOptionsCount = len(editMenuOptions)

		editMenu = tk.Menu(self, tearoff=False)
		self.add_cascade(label="Edit", menu=editMenu)

		for i in range(editMenuOptionsCount):
			editMenu.add_command(label=editMenuOptions[i])

	def addHelpMenu(self):
		helpMenu = tk.Menu(self, tearoff=False)
		self.add_cascade(label="Help", menu=helpMenu)

		helpMenu.add_command(label="About", command=self._showAboutWindow)

	def _showAboutWindow(self):
		tk.messagebox.showinfo("About", "Velichko Stoev made this using TkInter!")