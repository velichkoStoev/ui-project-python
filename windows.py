import tkinter as tk
import custom_widgets as cw

class ExposureWindow(tk.Toplevel):
	SLIDERS_NAMES = [
		"Exposure compensation", "Highlight compensation",
		"Highlight compensation treshold", "Black", "Lightness",
		"Contrast", "Saturation"
	]
	SLIDERS_COUNT = len(SLIDERS_NAMES)

	def __init__(self, frame):
		super().__init__(frame)
		self.resizable(tk.FALSE, tk.FALSE)

	def addHolderFrame(self):
		holderFrame = tk.Frame(self)		

		autoButton = tk.Button(holderFrame, text="Auto")
		autoButton.pack(side=tk.LEFT, padx=10, pady=5)

		clipLabel = tk.Label(holderFrame, text="Clip %")
		clipLabel.pack(side=tk.LEFT, padx=10, pady=5)

		clipSpinbox = tk.Spinbox(holderFrame, from_=0, to=100, width=3)
		clipSpinbox.pack(side=tk.LEFT, padx=10, pady=5)

		neutralButton = tk.Button(holderFrame, text="Neutral")
		neutralButton.pack(side=tk.RIGHT, padx=10, pady=5)

		holderFrame.pack(fill=tk.X)

	def addSliders(self):
		for i in range(self.SLIDERS_COUNT):
			cw.Slider(self, self.SLIDERS_NAMES[i])

	def addToneCurveFrame(self):
		frame = tk.Frame(self)

		toneCurveLabel = tk.Label(frame, text="Text Curve")
		toneCurveLabel.pack(side=tk.LEFT, padx=10, pady=5)

		dropdownOptions1 = ["Linear","Custom","Parametric", "Control Cage"]
		self.stringVar1 = tk.StringVar()
		self.stringVar1.set(dropdownOptions1[0])
		dropdownMenu1 = tk.OptionMenu(frame,self.stringVar1,*dropdownOptions1)
		dropdownMenu1.pack(side=tk.LEFT, padx=10, pady=5)

		dropdownOptions2 = ["Standart","Weighted Standart","Film-like", "Saturation and Value Blending"]
		self.stringVar2 = tk.StringVar()
		self.stringVar2.set(dropdownOptions2[0])
		dropdownMenu2 = tk.OptionMenu(frame,self.stringVar2,*dropdownOptions2)
		dropdownMenu2.pack(side=tk.LEFT, padx=10, pady=5)

		undoButton = tk.Button(frame, text="Undo", command=self._setToneCurveDefaultValues)
		undoButton.pack(side=tk.RIGHT, padx=10, pady=5)

		frame.pack(pady=5)
		
	def addApplyButton(self):
		applyButton = tk.Button(self, text="Apply")
		applyButton.pack(padx=5, pady=5)

	def _setToneCurveDefaultValues(self):
		self.stringVar1.set("Linear")
		self.stringVar2.set("Standart")

class ColorWindow(tk.Toplevel):
	WHITE_BALANCE_OPTIONS = [
		"Camera","Auto","Daylight", "Cloudy",
		"Shade", "Underwater", "Fluorescent",
		"Lamp", "LED", "Flash", "Custom"
	]

	BLACK_WHITE_OPTIONS = [
		"Desaturation","Luminance Equilizer", "Channel Mixer"
	]

	def __init__(self, frame):
		super().__init__(frame)
		self.resizable(tk.FALSE, tk.FALSE)

	def addWhiteBalanceFrame(self):
		frame = tk.LabelFrame(self, text="White Balance")

		methodLabel = tk.Label(frame, text="Method")
		methodLabel.pack()

		stringVar = tk.StringVar()
		stringVar.set(self.WHITE_BALANCE_OPTIONS[0])
		dropdownMenu = tk.OptionMenu(frame,stringVar,*self.WHITE_BALANCE_OPTIONS)
		dropdownMenu.pack()

		cw.Slider(frame, "Temperature", 30)
		cw.Slider(frame, "Tint", 30)
		cw.Slider(frame, "Blue/Red Equilizer", 40)

		frame.pack(padx=5, pady=(0, 15))

	def addBlackWhiteFrame(self):
		self.blackWhiteFrame = tk.LabelFrame(self, text="Black and White")

		methodLabel = tk.Label(self.blackWhiteFrame, text="Method")
		methodLabel.pack()

		stringVar = tk.StringVar()
		stringVar.set(self.BLACK_WHITE_OPTIONS[0])
		dropdownMenu = tk.OptionMenu(self.blackWhiteFrame,stringVar,*self.BLACK_WHITE_OPTIONS)
		dropdownMenu.pack()

		self._addGammaCorrection()

		self.blackWhiteFrame.pack(padx=5)

	def addApplyButton(self):
		applyButton = tk.Button(self, text="Apply")
		applyButton.pack(padx=5, pady=5)

	def _addGammaCorrection(self):
		frame = tk.Frame(self.blackWhiteFrame)

		blackWhiteLabel = tk.Label(frame, text="Gamma Correction")
		blackWhiteLabel.pack(side=tk.TOP)

		cw.Slider(frame, "Red")
		cw.Slider(frame, "Green")
		cw.Slider(frame, "Blue")

		frame.pack()
