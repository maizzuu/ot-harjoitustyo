from tkinter import Tk, ttk
from ui.login_ui import LoginUI

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        label = ttk.Label(master=self._root, text="Welcome to TrackApp!")
        
        self._current_view = LoginUI(self._root)
        self._current_view.pack()
        label.pack()
