from tkinter import ttk, constants, StringVar
from services.app_service import app_service, InvalidInputError, UsernameExistsError

class CreateUserUI:
    def __init__(self, root, handle_create_user, handle_show_login):
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login = handle_show_login
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

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if not username or not password:
            self._show_error('Username and password are required.')
            return

        try:
            app_service.create(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_and_password(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        password_label = ttk.Label(master=self._frame, text="Password")

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground='red')

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_and_password()

        create_user_button = ttk.Button(master=self._frame, text="Create", command=self._create_user_handler)

        login_button = ttk.Button(master=self._frame, text="Login", command=self._handle_show_login)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()