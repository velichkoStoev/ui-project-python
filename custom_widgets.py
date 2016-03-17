import tkinter as tk
import windows as w

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

class Toolbar(tk.Frame):
	ICON_NAMES = ["full_size", "plus", "minus", "delete"]
	ICONS_COUNT = len(ICON_NAMES)

	def __init__(self, frame = None):
		super().__init__(frame, bd=1)
		self._toolbarIcons = {}
		self.pack(side=tk.TOP, fill=tk.X)

	def addButton(self, text):
		button = tk.Button(self, text=text)
		button.pack(side=tk.LEFT, fill=tk.Y)

	def addIconButtons(self):
		for i in range(self.ICONS_COUNT):
			self._toolbarIcons[self.ICON_NAMES[i]] = tk.PhotoImage(file="icons/{}.png".format(self.ICON_NAMES[i]))
			toolbarIconButton = tk.Button(self, image=self._toolbarIcons[self.ICON_NAMES[i]])
			toolbarIconButton.pack(side=tk.LEFT)

	def addSettingsMenubutton(self):
		self._toolbarIcons["arrow_down"] = tk.PhotoImage(file="icons/arrow_down.png")
		settingsDropdownButton = tk.Menubutton(self, text="Settings", image=self._toolbarIcons["arrow_down"], compound=tk.RIGHT)

		settingsMenu = tk.Menu(settingsDropdownButton, tearoff=False)
		settingsDropdownButton.config(menu=settingsMenu)

		self._exposureVar = tk.IntVar()
		settingsMenu.add_checkbutton(label="Exposure", command=self._showExposureWindow, variable=self._exposureVar)
		
		self._colorVar = tk.IntVar()
		settingsMenu.add_checkbutton(label="Color", command=self._showColorWindow, variable=self._colorVar)

		settingsDropdownButton.pack(side=tk.LEFT, fill=tk.Y)

	def _showColorWindow(self):
		if self._colorVar.get() == 1:
			self._colorWindow = w.ColorWindow(self)

			self._colorWindow.addWhiteBalanceFrame()
			self._colorWindow.addBlackWhiteFrame()
		else:
			self._colorWindow.destroy()

	def _showExposureWindow(self):
		if self._exposureVar.get() == 1:
			self._exposureWindow = w.ExposureWindow(self)

			self._exposureWindow.addHolderFrame()
			self._exposureWindow.addSliders()
			self._exposureWindow.addToneCurveFrame()
		else:
			self._exposureWindow.destroy()

class MainFrame(tk.Frame):
	def __init__(self, frame = None):
		super().__init__(frame)
		self._optionsIcons = {}
		self.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

	def addImageHolderFrame(self):
		imageHolderFrame = tk.Frame(self, bd=1, bg="white", width=500)
		imageHolderFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

	def addOptionsFrame(self):
		buttonIconNames = ["save", "rotate_left", "rotate_right", "mirror", "flip", "resize", "crop", "info"]
		buttonTexts = ["Save as", "Rotate Left", "Rotate Right", "Mirror", "Flip", "Resize", "Crop", "Show information"]
		buttonCount = len(buttonIconNames)

		editOptionsFrame = tk.Frame(self, bd=1, height=500)

		for i in range(buttonCount):
			self._optionsIcons[buttonIconNames[i]] = tk.PhotoImage(file="icons/{}.png".format(buttonIconNames[i]))
			rotateRightButton = tk.Button(editOptionsFrame, text=buttonTexts[i], image=self._optionsIcons[buttonIconNames[i]], compound=tk.LEFT)
			rotateRightButton.pack(fill=tk.X, pady=1)

		editOptionsFrame.pack(side=tk.RIGHT, fill=tk.Y)

class GalleryFrame(tk.Frame):
	def __init__(self, frame = None):
		super().__init__(frame, height=150)
		
		galleryLabel = tk.Label(self, text="Gallery")
		galleryLabel.pack(side=tk.TOP, fill=tk.X)

		self._galleryImageIcon = tk.PhotoImage(file="icons/gallery_image.png")

		for i in range(8):
			galleryImageLabel = tk.Label(self, image=self._galleryImageIcon)
			galleryImageLabel.pack(side=tk.LEFT, pady=2)

		self.pack(side=tk.BOTTOM, fill=tk.X)

class Slider(tk.Frame):
	def __init__(self, frame, name, value=0):
		super().__init__(frame)

		separator = tk.Frame(self, height=2, bg="black")
		separator.pack(fill=tk.X, pady=2)

		label = tk.Label(self, text=name)
		label.pack(side=tk.TOP)

		self.slider = tk.Scale(self, orient=tk.HORIZONTAL)
		self.slider.set(value)
		self.slider.pack(side=tk.LEFT, padx=10)

		undoButton = tk.Button(self, text="Undo", command=self._setSliderDefaultValue)
		undoButton.pack(side=tk.RIGHT, padx=10)

		self.pack(fill=tk.X, padx=10, pady=10)

	def _setSliderDefaultValue(self):
		self.slider.set(0)