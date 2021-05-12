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
        month_label = ttk.Label(master=item_frame, text=text)

        food = ttk.Label(master=item_frame, text=f"Food: {month.food}")
        living = ttk.Label(master=item_frame, text=f"Living: {month.living}")
        hobbies = ttk.Label(master=item_frame, text=f"Hobbies: {month.hobbies}")
        transportation = ttk.Label(master=item_frame, text=f"Transportation: {month.transportation}")
        culture = ttk.Label(master=item_frame, text=f"Culture: {month.culture}")
        other = ttk.Label(master=item_frame, text=f"Other: {month.other}")

        month_label.grid(padx=5, pady=5, sticky=constants.W)

        food.grid(padx=5, pady=5, row=0, column=1)
        living.grid(padx=5, pady=5, row=0, column=2)
        hobbies.grid(padx=5, pady=5, row=0, column=3)
        transportation.grid(padx=5, pady=5, row=0, column=4)
        culture.grid(padx=5, pady=5, row=0, column=5)
        other.grid(padx=5, pady=5, row=0, column=6)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for month in self._months:
            self._initialize_month(month)

class MonthUI:
    def __init__(self, root, hande_logout):
        self._root = root
        self._handle_logout = hande_logout
        self._frame = None
        self._month_list_frame = None
        self._month_list = None
        self._log_month_entry = None
        self._log_year_entry = None
        self._log_category_entry = None
        self._log_amount_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        app_service.logout()
        self._handle_logout()

    def _log_handler(self):
        month = self._log_month_entry.get()
        year = self._log_year_entry.get()
        category = self._log_category_entry.get()
        amount = self._log_amount_entry.get()

        if month and year and category and amount:
            app_service.log(month, year, category, int(amount))
            self._initialize_month_list()
            self._log_month_entry.delete(0, constants.END)
            self._log_year_entry.delete(0, constants.END)
            self._log_category_entry.delete(0, constants.END)
            self._log_amount_entry.delete(0, constants.END)
            self._log_month_entry.insert(-1, "Month")
            self._log_year_entry.insert(-1, "Year")
            self._log_category_entry.insert(-1, "Category")
            self._log_amount_entry.insert(-1, "Amount")

    def _initialize_month_list(self):
        if self._month_list:
            self._month_list.destroy()

        months = app_service.get_months()

        self._month_list = MonthList(self._month_list_frame, months)

        self._month_list.pack()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._month_list_frame = ttk.Frame(master=self._frame)

        logout_button = ttk.Button(master=self._frame, text="Log out", command=self._logout_handler)

        logout_button.grid(row=0, sticky=constants.E)

        self._initialize_month_list()

        self._month_list_frame.grid(row=1, column=0, columnspan=2, sticky=constants.EW)

        self._log_month_entry = ttk.Entry(master=self._frame)
        self._log_month_entry.insert(-1, "Month")

        self._log_year_entry = ttk.Entry(master=self._frame)
        self._log_year_entry.insert(-1, "Year")

        self._log_category_entry = ttk.Entry(master=self._frame)
        self._log_category_entry.insert(-1, "Category")

        self._log_amount_entry = ttk.Entry(master=self._frame)
        self._log_amount_entry.insert(-1, "Amount")

        log_button = ttk.Button(master=self._frame, text="Log", command=self._log_handler)

        self._log_month_entry.grid(padx=5, pady=5)
        self._log_year_entry.grid(padx=5, pady=5)
        self._log_category_entry.grid(padx=5, pady=5)
        self._log_amount_entry.grid(padx=5, pady=5)

        log_button.grid(padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)
        self._frame.grid_columnconfigure(1, weight=0)
