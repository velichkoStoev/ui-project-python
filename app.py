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
