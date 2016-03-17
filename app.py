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

root = tk.Tk()
app = Application(master = root)
app.master.title("Velichko's UI")
root.mainloop()
