import PySimpleGUI as sg

layouts = {'Phone Number', 'Home', 'Pet Q1', "Pet Q2"}

phone_page = [[sg.Text('Enter your phone number')],
            [sg.Button('Next'), sg.Button('Exit')]]

layout1 = [[sg.Text('Home page')], 
        [sg.Button('Back'), sg.Button('Next'), sg.Button('Exit')]]

layout2 = [[sg.Text('Pet question 1')],
        [sg.Button('Back'), sg.Button('Next'), sg.Button('Exit')]]

layout3 = [[sg.Text('Pet question 2')],
        [sg.Button('Back'), sg.Button('Next'), sg.Button('Exit')]]

layout = [[sg.Column(phone_page, key='1'), sg.Column(layout1, visible=False, key='2'), sg.Column(layout2, visible=False, key='3'), sg.Column(layout3, visible=False, key='4')]]

window = sg.Window('Swapping the contents of a window', layout)

layout_num = 1 # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    elif "Next" in event:
        window[f'{layout_num}'].update(visible=False)
        layout_num += 1
        window[f'{layout_num }'].update(visible=True)
    elif "Back" in event:
        window[f'{layout_num}'].update(visible=False)
        layout_num -= 1
        window[f'{layout_num }'].update(visible=True)
window.close()