
# Frame 5 - Incident at B1


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\fizak\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("390x844")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    390.0,
    844.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    183.0,
    756.0,
    223.4595947265625,
    807.2326354980469,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    33.0,
    208.0,
    355.0,
    246.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    33.0,
    151.0,
    355.0,
    194.61538696289062,
    fill="#000000",
    outline="")

canvas.create_text(
    92.0,
    114.0,
    anchor="nw",
    text=" Incident at B1: ",
    fill="#D9498C",
    font=("Inter Bold", 20 * -1)
)

canvas.create_rectangle(
    78.0,
    649.0,
    318.9031982421875,
    681.0,
    fill="#000000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=60.0,
    y=688.0,
    width=270.103759765625,
    height=48.00213623046875
)

canvas.create_rectangle(
    29.0,
    261.0,
    360.0,
    633.0,
    fill="#000000",
    outline="")

canvas.create_text(
    136.0,
    49.0,
    anchor="nw",
    text="Report",
    fill="#706A63",
    font=("Inika Bold", 39 * -1)
)
window.resizable(False, False)
window.mainloop()
