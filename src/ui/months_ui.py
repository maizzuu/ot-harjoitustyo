from tkinter import ttk, constants
from services.app_service import app_service
from entities.month import Month

class MonthList:
    def __init__(self, root, months):
        self._root = root
        self._months = months
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_month(self, month=Month):
        item_frame = ttk.Frame(master=self._frame)
        text = f"{month.month}, {month.year}"
        label = ttk.Label(master=item_frame, text=text)

        label.grid(padx=5, pady=5, sticky=constants.W)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for month in self._months:
            self._initialize_month(month)

class MonthUI:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._month_list_frame = None
        self._month_list = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_month_list(self):
        if self._month_list:
            self._month_list.destroy()

        months = app_service.get_months()

        self._month_list = MonthList(self._month_list_frame, months)

        self._month_list.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._month_list_frame = ttk.Frame(master=self._frame)

        self._initialize_month_list()

        self._month_list_frame.grid(row=1, column=0, columnspan=2, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
