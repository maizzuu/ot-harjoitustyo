from tkinter import Tk, ttk
from ui.login_ui import LoginUI
from ui.months_ui import MonthUI
from ui.create_ui import CreateUserUI

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login(self):
        self._hide_current_view()

        self._current_view = LoginUI(self._root, self._show_months, self._show_create_view)

        self._current_view.pack()

    def _show_months(self):
        self._hide_current_view()

        self._current_view = MonthUI(self._root, self._show_login)

        self._current_view.pack()

    def _show_create_view(self):
        self._hide_current_view()

        self._current_view = CreateUserUI(self._root, self._show_months, self._show_login)

        self._current_view.pack()