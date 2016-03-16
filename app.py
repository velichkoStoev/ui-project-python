import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

import custom_widgets as cw

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack(fill=tk.BOTH, expand=True)

		self._createMainMenu()
		self._createToolbar()
		self._createMainFrame()
		self._createGalleryFrame()

	# private methods

	def _createGalleryFrame(self):
		cw.GalleryFrame(self)

	def _createMainFrame(self):
		mainFrame = cw.MainFrame(self)
		mainFrame.addImageHolderFrame()
		mainFrame.addOptionsFrame()

	def _createMainMenu(self):
		mainMenu = cw.MainMenu(self)

		mainMenu.addFileMenu()
		mainMenu.addEditMenu()
		mainMenu.addHelpMenu()

	def _createToolbar(self):
		toolbar = cw.Toolbar(self)

		toolbar.addButton("Preview")
		toolbar.addButton("Next")
		toolbar.addIconButtons()
		toolbar.addButton("Comment")
		toolbar.addSettingsMenubutton()

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
