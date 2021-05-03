from tkinter import ttk

class LoginUI:
    def __init__(self, root):
        self._root = root
        self._frame = None

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

        login_label = ttk.Label(master=self._frame, text="Login")

        self._initialize_username_and_password()

        login_label.grid(row=0, column=1)