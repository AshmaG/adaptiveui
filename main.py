import PySimpleGUI as sg

def create_layout(theme):
    sg.theme(theme)
    layout = [
        [sg.Text("Choose a theme:")],
        [sg.Button("Light"), sg.Button("Dark"), sg.Button("Purple"), sg.Button("Green"), sg.Button("Yellow")]

    ]
    return layout

def main():
    window = sg.Window("Adaptive UI", create_layout("Light"))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Light":
            window.close()
            window = sg.Window("Adaptive UI", create_layout("Light"))
        if event == "Dark":
            window.close()
            window = sg.Window("Adaptive UI", create_layout("Dark"))
        if event == "Purple":
            window.close()
            window = sg.Window("Adaptive UI", create_layout("'BluePurple"))
        if event == "Green":
            window.close()
            window = sg.Window("Adaptive UI", create_layout("DarkGreen5"))
        if event == "Yellow":
            window.close()
            window = sg.Window("Adaptive UI", create_layout("LightYellow"))



    window.close()

if __name__ == "__main__":
    main()