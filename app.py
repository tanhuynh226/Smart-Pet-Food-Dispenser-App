import PySimpleGUI as sg

layouts = {'Home': 1, 'Pet Q1': 2, "Pet Q2": 3}

layout1 = [[sg.Text('Home page')]]

layout2 = [[sg.Text('Pet question 1')]]

layout3 = [[sg.Text('Pet question 2')]]

layout = [[sg.Column(layout1, key='1'), sg.Column(layout2, visible=False, key='2'), sg.Column(layout3, visible=False, key='3')],
          [sg.Button('Home'), sg.Button('Pet Q1'), sg.Button('Pet Q2'), sg.Button('Exit')]]

window = sg.Window('Swapping the contents of a window', layout)

layout_num = 1  # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    elif event in layouts.keys():
        window[f'{layout_num}'].update(visible=False)
        layout_num = int(layouts[event])
        window[f'{layout_num }'].update(visible=True)
window.close()