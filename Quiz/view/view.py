#ifndef GUARD_DAEDEA8A_C0C5_4861_A200_7B80351A8703
#define GUARD_DAEDEA8A_C0C5_4861_A200_7B80351A8703

import PySimpleGUI as sg


def create_quiz_window(question,answer):
    
    sg.theme("DarkBlue15")
    font = ("Arial", 16)
    layout = []
    key_counter = 0
    
    layout.append([sg.Text(question,font=font)])

    for item in answer:
        layout.append([sg.Text("         "),sg.Radio(item, "RADIO1", default=False, key=str(key_counter),font=font)])
        key_counter+=1

    layout.append([sg.Button("Next")])

    window = sg.Window('Quiz Window', layout, size=(300,300))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            return None
        elif event == "Next":
            window.close()
            return values

def show_score(score):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    font = ("Arial", 20)
    layout = [[sg.Text("Your Score Is : ",font=font),sg.Text(score,font=font)]]
    window = sg.Window('Score Window', layout)
    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED : # if user closes window or clicks cancel
            break

    window.close()



#endif /* GUARD_DAEDEA8A_C0C5_4861_A200_7B80351A8703 */




