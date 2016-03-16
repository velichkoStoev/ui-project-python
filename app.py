import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

import custom_widgets as cw

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
		mainMenu = cw.MainMenu(self)
		mainMenu.addFileMenu()
		mainMenu.addEditMenu()
		mainMenu.addHelpMenu()

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

		self._exposureVar = tk.IntVar()
		settingsMenu.add_checkbutton(label="Exposure", command=self._showExposureWindow, variable=self._exposureVar)
		
		self._colorVar = tk.IntVar()
		settingsMenu.add_checkbutton(label="Color", command=self._showColorWindow, variable=self._colorVar)

		settingsDropdownButton.pack(side=tk.LEFT, fill=tk.Y)

		toolbar.pack(side=tk.TOP, fill=tk.X)

	def _photoCommentWindow(self):
		tk.simpledialog.askstring("Comment the picture", "Your comment")

	def _showExposureWindow(self):
		if self._exposureVar.get() == 1:
			self._exposureWindow = tk.Toplevel(self)
			self._exposureWindow.resizable(tk.FALSE, tk.FALSE)

			self._addHolderFrame()
			self._addSliders()
			self._addToneCurveFrame()
		else:
			self._exposureWindow.destroy()

	def _addHolderFrame(self):
		holderFrame = tk.Frame(self._exposureWindow)		

		autoButton = tk.Button(holderFrame, text="Auto")
		autoButton.pack(side=tk.LEFT, padx=5)

		clipLabel = tk.Label(holderFrame, text="Clip %")
		clipLabel.pack(side=tk.LEFT, padx=5)

		clipSpinbox = tk.Spinbox(holderFrame, from_=0, to=100, width=3)
		clipSpinbox.pack(side=tk.LEFT, padx=5)

		neutralButton = tk.Button(holderFrame, text="Neutral")
		neutralButton.pack(side=tk.RIGHT, padx=5)

		holderFrame.pack(fill=tk.X)

	def _addSliders(self):
		slidersNames = [
			"Exposure compensation", "Highlight compensation",
			"Highlight compensation treshold", "Black", "Lightness",
			"Contrast", "Saturation"
		]

		slidersCount = len(slidersNames)

		for i in range(slidersCount):
			self._addSlider(self._exposureWindow, slidersNames[i])

	def _addSlider(self, window, name, value = 0):
		frame = tk.Frame(window)

		separator = tk.Frame(frame, height=2, bg="black")
		separator.pack(fill=tk.X, pady=2)

		label = tk.Label(frame, text=name)
		label.pack(side=tk.TOP)

		slider = tk.Scale(frame, orient=tk.HORIZONTAL)
		slider.set(value)
		slider.pack(side=tk.LEFT)

		undoButton = tk.Button(frame, text="Undo", command= lambda: self._setSliderDefaultValue(slider))
		undoButton.pack(side=tk.RIGHT)

		frame.pack(fill=tk.X, padx=5)

	def _setSliderDefaultValue(self, slider):
		slider.set(0)

	def _addToneCurveFrame(self):
		frame = tk.Frame(self._exposureWindow)

		toneCurveLabel = tk.Label(frame, text="Text Curve")
		toneCurveLabel.pack(side=tk.LEFT)

		dropdownOptions1 = ["Linear","Custom","Parametric", "Control Cage"]
		stringVar1 = tk.StringVar()
		stringVar1.set(dropdownOptions1[0])
		dropdownMenu1 = tk.OptionMenu(frame,stringVar1,*dropdownOptions1)
		dropdownMenu1.pack(side=tk.LEFT)

		dropdownOptions2 = ["Standart","Weighted Standart","Film-like", "Saturation and Value Blending"]
		stringVar2 = tk.StringVar()
		stringVar2.set(dropdownOptions2[0])
		dropdownMenu2 = tk.OptionMenu(frame,stringVar2,*dropdownOptions2)
		dropdownMenu2.pack(side=tk.LEFT)

		undoButton = tk.Button(frame, text="Undo", command= lambda: self._setToneCurveDefaultValues(stringVar1, stringVar2))
		undoButton.pack(side=tk.RIGHT)

		frame.pack()

	def _setToneCurveDefaultValues(self, stringVar1, stringVar2):
		stringVar1.set("Linear")
		stringVar2.set("Standart")

	def _showColorWindow(self):
		if self._colorVar.get() == 1:
			self._colorWindow = tk.Toplevel(self)
			self._colorWindow.resizable(tk.FALSE, tk.FALSE)

			self._addWhiteBalanceFrame()
			self._addBlackWhiteFrame()
		else:
			self._colorWindow.destroy()

	def _addWhiteBalanceFrame(self):
		frame = tk.LabelFrame(self._colorWindow, text="White Balance")

		methodLabel = tk.Label(frame, text="Method")
		methodLabel.pack()

		methodDropdownOptions = [
			"Camera","Auto","Daylight", "Cloudy",
			"Shade", "Underwater", "Fluorescent",
			"Lamp", "LED", "Flash", "Custom"
		]
		stringVar = tk.StringVar()
		stringVar.set(methodDropdownOptions[0])
		dropdownMenu = tk.OptionMenu(frame,stringVar,*methodDropdownOptions)
		dropdownMenu.pack()

		self._addSlider(frame, "Temperature", 60)
		self._addSlider(frame, "Tint", 30)
		self._addSlider(frame, "Blue/Red Equilizer", 40)

		frame.pack(padx=5)

	def _addBlackWhiteFrame(self):
		self.blackWhiteFrame = tk.LabelFrame(self._colorWindow, text="Black and White")

		methodLabel = tk.Label(self.blackWhiteFrame, text="Method")
		methodLabel.pack()

		methodDropdownOptions = [
			"Desaturation","Luminance Equilizer", "Channel Mixer"
		]
		stringVar = tk.StringVar()
		stringVar.set(methodDropdownOptions[0])
		dropdownMenu = tk.OptionMenu(self.blackWhiteFrame,stringVar,*methodDropdownOptions)
		dropdownMenu.pack()

		self._addGammaCorrection(self.blackWhiteFrame)

		self.blackWhiteFrame.pack(padx=5)

	def _addGammaCorrection(self, blackWhiteFrame):
		frame = tk.Frame(blackWhiteFrame)

		blackWhiteLabel = tk.Label(frame, text="Gamma Correction")
		blackWhiteLabel.pack(side=tk.TOP)

		self._addSlider(frame, "Red")
		self._addSlider(frame, "Green")
		self._addSlider(frame, "Blue")

		frame.pack()

root = tk.Tk()
app = Application(master = root)
app.master.title("Velichko's UI")
root.mainloop()
