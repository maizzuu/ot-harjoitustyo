from tkinter import ttk, constants, StringVar
from services.app_service import AppService, InvalidInputError

class LoginUI:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            AppService.login(username, password)
        except InvalidInputError:
            self._show_error("Invalid username or password")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _initialize_username_and_password(self):

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(master=self._frame, text="Login")

        username_label.grid(row=2, column=1)
        self._username_entry.grid(row=2, column=2)

        password_label.grid(row=3, column=1)
        self._password_entry.grid(row=3, column=2)

        button.grid(row=4, column=1, columnspan=2)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame, 
            textvariable=self._error_variable, 
            foreground='red'
        )

        login_label = ttk.Label(master=self._frame, text="Login")
        login_label.grid(row=0, column=1)

        self._initialize_username_and_password()

        login_button = ttk.Button(master=self._frame, text="Login", command=self._login_handler)
