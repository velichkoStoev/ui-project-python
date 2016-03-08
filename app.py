import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		
		self._toolbarIcons = {}
		self._rightFrameOptionsIcons = {}

		self.pack(fill=tk.BOTH, expand=True)
		self._createMainMenu()
		self._createToolbar()
		self._createMainFrame()
		self._createGalleryFrame()

	# private methods

	def _createGalleryFrame(self):
		galleryFrame = tk.Frame(self, height=150)

		galleryLabel = tk.Label(galleryFrame, text="Gallery")
		galleryLabel.pack(side=tk.TOP, fill=tk.X)

		self._galleryImageIcon = tk.PhotoImage(file="icons/gallery_image.png")

		for i in range(8):
			galleryImageLabel = tk.Label(galleryFrame, image=self._galleryImageIcon)
			galleryImageLabel.pack(side=tk.LEFT, pady=2)

		galleryFrame.pack(side=tk.BOTTOM, fill=tk.X)

	def _createMainFrame(self):
		mainFrame = tk.Frame(self)

		self._createLeftFrame(mainFrame)
		self._createRightFrame(mainFrame)

		mainFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

	def _createLeftFrame(self, mainFrame):
		leftFrame = tk.Frame(mainFrame, bd=1, bg="white", width=500)
		leftFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


	def _createRightFrame(self, mainFrame):
		buttonIconNames = ["save", "rotate_left", "rotate_right", "mirror", "flip", "resize", "crop", "info"]
		buttonTexts = ["Save as", "Rotate Left", "Rotate Right", "Mirror", "Flip", "Resize", "Crop", "Show information"]
		buttonCount = len(buttonIconNames)

		rightFrame = tk.Frame(mainFrame, bd=1, height=500)

		for i in range(buttonCount):
			self._rightFrameOptionsIcons[buttonIconNames[i]] = tk.PhotoImage(file="icons/{}.png".format(buttonIconNames[i]))
			rotateRightButton = tk.Button(rightFrame, text=buttonTexts[i], image=self._rightFrameOptionsIcons[buttonIconNames[i]], compound=tk.LEFT)
			rotateRightButton.pack(fill=tk.X, pady=1)

		rightFrame.pack(side=tk.RIGHT, fill=tk.Y)

	def _createMainMenu(self):
		# mainMenu class

		mainMenu = tk.Menu(self)
		self.master.config(menu=mainMenu)

		self._addFileMenu(mainMenu)
		self._addEditMenu(mainMenu)
		self._addHelpMenu(mainMenu)

	def _addFileMenu(self, mainMenu):
		fileMenuOptions = ["New", "Open", "Save", "Save as", "Print"]
		fileMenuOptionsCount = len(fileMenuOptions)

		fileMenu = tk.Menu(mainMenu, tearoff=False)
		mainMenu.add_cascade(label="File", menu=fileMenu)

		for i in range(fileMenuOptionsCount):
			fileMenu.add_command(label=fileMenuOptions[i])

		fileMenu.add_separator()
		fileMenu.add_command(label="Exit", command=self.quit)

	def _addEditMenu(self, mainMenu):
		editMenuOptions = ["Cut", "Copy", "Paste", "Rename", "Preferences"]
		editMenuOptionsCount = len(editMenuOptions)

		editMenu = tk.Menu(mainMenu, tearoff=False)
		mainMenu.add_cascade(label="Edit", menu=editMenu)

		for i in range(editMenuOptionsCount):
			editMenu.add_command(label=editMenuOptions[i])

	def _addHelpMenu(self, mainMenu):
		helpMenu = tk.Menu(mainMenu, tearoff=False)
		mainMenu.add_cascade(label="Help", menu=helpMenu)

		helpMenu.add_command(label="About", command=self._showAboutWindow)

	def _createToolbar(self):
		# toolbar class

		toolbarIconTags = ["full_size", "plus", "minus", "delete"]
		toolbarIconTagsCount = len(toolbarIconTags)

		toolbar = tk.Frame(self, bd=1)

		previewButton = tk.Button(toolbar, text="Preview")
		previewButton.pack(side=tk.LEFT, fill=tk.Y)

		nextButton = tk.Button(toolbar, text="Next")
		nextButton.pack(side=tk.LEFT, fill=tk.Y)

		for i in range(toolbarIconTagsCount):
			self._toolbarIcons[toolbarIconTags[i]] = tk.PhotoImage(file="icons/{}.png".format(toolbarIconTags[i]))
			toolbarIconButton = tk.Button(toolbar, image=self._toolbarIcons[toolbarIconTags[i]])
			toolbarIconButton.pack(side=tk.LEFT)

		commentButton = tk.Button(toolbar, text="Comment", command=self._photoCommentWindow)
		commentButton.pack(side=tk.LEFT, fill=tk.Y)

		self._toolbarIcons["arrow_down"] = tk.PhotoImage(file="icons/arrow_down.png")
		settingsDropdownButton = tk.Menubutton(toolbar, text="Settings", image=self._toolbarIcons["arrow_down"], compound=tk.RIGHT)

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
