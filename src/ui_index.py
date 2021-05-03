from tkinter import Tk
from ui.user_interface import UI

def main():
    window = Tk()
    window.title("TrackApp")

    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()