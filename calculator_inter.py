import PySimpleGUI as sg

pattern = ["+", "-", ".", "/", "*"]


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font="franklin 14", button_element_size=(6, 6))
    button_size = (7, 3)
    layout = [
        [sg.Push(), sg.Text("", key="-Ques-")],
        [
            sg.Text(
                "",
                font="franklin 26",
                pad=(10, 20),
                expand_x=True,
                justification="right",
                right_click_menu=theme_menu,
                key="-Output-",
            ),
        ],
        [sg.Button("Clear", expand_x=True), sg.Button("Enter", expand_x=True)],
        [
            sg.Button("7", size=button_size),
            sg.Button("8", size=button_size),
            sg.Button("9", size=button_size),
            sg.Button("*", size=button_size),
        ],
        [
            sg.Button("4", size=button_size),
            sg.Button("5", size=button_size),
            sg.Button("6", size=button_size),
            sg.Button("/", size=button_size),
        ],
        [
            sg.Button("1", size=button_size),
            sg.Button("2", size=button_size),
            sg.Button("3", size=button_size),
            sg.Button("-", size=button_size),
        ],
        [
            sg.Button("0", size=button_size, expand_x=True),
            sg.Button(".", size=button_size),
            sg.Button("+", size=button_size),
        ],
    ]
    return sg.Window("Calculator", layout)


theme_menu = [["menu"], ["DarkGrey", "BlueMono", "Python", "Random"]]
window = create_window("DarkGrey1")
num_list = []
operation = []
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in theme_menu[1]:
        window.close()
        operation = []
        num_list = []
        window = create_window(event)
    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        num_list.append(event)
        num_string = "".join(num_list)
        window["-Output-"].update(num_string)
    if event in ["+", "-", ".", "/", "*"]:
        operation.append("".join(num_string))
        num_list = []
        operation.append(event)
        window["-Output-"].update(event)
    if event == "Enter":
        operation.append("".join(num_list))
        res = "".join(operation)
        if not (res == ""):
            result = round(eval(res), 3)
            window["-Ques-"].update(res)
            window["-Output-"].update(result)
            operation = []
    if event == "Clear":
        operation = []
        num_list = []
        window["-Output-"].update("")
        window["-Ques-"].update("")
