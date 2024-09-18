import PySimpleGUI as sg
from time import time


def create_window():
    sg.theme("black")
    layout = [
        [sg.Text("StopWatch"), sg.Push()],
        [
            sg.Push(),
            sg.Button("X", pad=0, border_width=0, key="-CLOSE-", font="Franklin 12"),
        ],
        [sg.VPush()],
        [sg.Text("", font="Franklin 40", border_width=0, key="-TIME-")],
        [
            sg.Button(
                "Start",
                pad=0,
                button_color=("#FFFFFF", "#FF0000"),
                border_width=0,
                key="-STARTSTOP-",
            ),
            sg.Button(
                "Lap",
                button_color=("#FFFFFF", "#FF0000"),
                border_width=0,
                key="-LAP-",
                visible=False,
            ),
        ],
        [sg.Column([[]], key="-LAPS-")],
        [sg.VPush()],
    ]
    return sg.Window(
        "Stopwatch",
        layout,
        size=(300, 300),
        no_titlebar=True,
        element_justification="center",
    )


window = create_window()
start_time = 0
active = False
LapAmount = 1
while True:
    event, value = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, "-CLOSE-"):
        break
    if event == "-STARTSTOP-":
        if active:
            active = False
            window["-STARTSTOP-"].update("Reset")
            window["-LAP-"].update(visible=False)
        else:
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
            else:
                window["-STARTSTOP-"].update("Stop")
                window["-LAP-"].update(visible=True)
                start_time = time()
                active = True
    if active:
        elapsed_time = round(time() - start_time, 2)
        window["-TIME-"].update(elapsed_time)
    if event == "-LAP-" and LapAmount <= 5:
        window.extend_layout(
            window["-LAPS-"],
            [[sg.Text(LapAmount), sg.VSeparator(), sg.Text(elapsed_time)]],
        )
        LapAmount = 1 + LapAmount
