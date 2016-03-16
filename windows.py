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
		autoButton.pack(side=tk.LEFT, padx=5)

		clipLabel = tk.Label(holderFrame, text="Clip %")
		clipLabel.pack(side=tk.LEFT, padx=5)

		clipSpinbox = tk.Spinbox(holderFrame, from_=0, to=100, width=3)
		clipSpinbox.pack(side=tk.LEFT, padx=5)

		neutralButton = tk.Button(holderFrame, text="Neutral")
		neutralButton.pack(side=tk.RIGHT, padx=5)

		holderFrame.pack(fill=tk.X)

	def addSliders(self):
		for i in range(self.SLIDERS_COUNT):
			cw.Slider(self, self.SLIDERS_NAMES[i])

	def addToneCurveFrame(self):
		frame = tk.Frame(self)

		toneCurveLabel = tk.Label(frame, text="Text Curve")
		toneCurveLabel.pack(side=tk.LEFT)

		dropdownOptions1 = ["Linear","Custom","Parametric", "Control Cage"]
		self.stringVar1 = tk.StringVar()
		self.stringVar1.set(dropdownOptions1[0])
		dropdownMenu1 = tk.OptionMenu(frame,self.stringVar1,*dropdownOptions1)
		dropdownMenu1.pack(side=tk.LEFT)

		dropdownOptions2 = ["Standart","Weighted Standart","Film-like", "Saturation and Value Blending"]
		self.stringVar2 = tk.StringVar()
		self.stringVar2.set(dropdownOptions2[0])
		dropdownMenu2 = tk.OptionMenu(frame,self.stringVar2,*dropdownOptions2)
		dropdownMenu2.pack(side=tk.LEFT)

		undoButton = tk.Button(frame, text="Undo", command=self._setToneCurveDefaultValues)
		undoButton.pack(side=tk.RIGHT)

		frame.pack()

	def _setToneCurveDefaultValues(self):
		self.stringVar1.set("Linear")
		self.stringVar2.set("Standart")