import PySimpleGUI as sg

# Create the Window
def create_login_window():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Enter your username : '), sg.InputText()],
                [sg.Text('Enter your password : '), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Login Window', layout)

    return window


def get_login_details(window):
# Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        elif event == "Ok":
            return values

def show_success_window():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text("Success")]]

    window = sg.Window('Success Window', layout)
    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED : # if user closes window or clicks cancel
            break
    window.close()


def show_failure_window():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text("Failure")],[sg.Button('Retry')]]
    window = sg.Window('Failue Window', layout)
    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED : # if user closes window or clicks cancel
            return False
        elif event == event == "Retry":
            return True

    
        


