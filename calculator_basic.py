import PySimpleGUI as sg
import re

sg.theme("dark")
pattern = r"^[0-9+\-*/%]+$"
layout = [
    [sg.Push(), sg.Button("X", key="-X-")],
    [sg.Text("Calculator"), sg.Push()],
    [sg.Text("Enter numbers : ")],
    [sg.Input(key="-Input-")],
    [sg.Button("Calculate", key="-Button-")],
    [sg.Text("You can provide a whole string of numbers", key="-Output-")],
]
window = sg.Window("Calculator", layout, no_titlebar=True)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "-X-"):
        break
    if event == "-Button-":
        input_values = values["-Input-"]
        if re.match(pattern, input_values):
            result = eval(input_values)
            result = round(result, 3)
            window["-Output-"].update(f"Result is = {result}")
        else:
            window["-Output-"].update("Please enter valid numbers")
