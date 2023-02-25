import PySimpleGUI as sg

layouts = {'Phone Number', 'Home', 'Dispense 1 Pet ID', 'Pet Q1', 'Dispense 2 Pet ID', 'Pet Q2'}

phone_page = [[sg.Text('Enter your phone number (include country number):')],
              [sg.Input('', key = 'phone_number', enable_events = True, expand_x=True, justification='left')],
            [sg.Button('Next'), sg.Button('Exit')]]

layout1 = [[sg.Text('Home page')], 
        [sg.Button('Back'), sg.Button('Next'), sg.Button('Exit')]]

layout2 = [[sg.Text('Dispenser 1 Pet Identification', font = ('Arial Bold', 12))], 
           [sg.Text('Please place your first pet in front of the camera. Click the "Next" button below after ensuring so.', justification = 'center')],
        [sg.Button('Back'), sg.Button('Next'), sg.Button('Exit')]]

layout3 = [[sg.Text('Pet question 1')],
           [sg.Text('How many times per day would you like your pet to be fed?')],
           [sg.Input('', key = 'pet_one_dispenses_per_day', expand_x=True, justification='left')],
           [sg.Text('How much should each meal be (cups)?')],
           [sg.Input('', key = 'pet_one_amount_dispensed', expand_x=True, justification='left')],
           [sg.Text('How many increments should the food be dispensed?')],
           [sg.Input('', key = 'pet_one_increments', expand_x=True, justification='left')],
           [sg.Text('How many seconds in between each increment (seconds)?')],
           [sg.Input('', key = 'pet_one_time_between_increments', expand_x=True, justification='left')],
        [sg.Button('Back'), sg.Button('Next'), sg.Button('Exit')]]

layout4 = [[sg.Text('Dispenser 2 Pet Identification', font = ('Arial Bold', 12))], 
           [sg.Text('Please place your second pet in front of the camera. Click the "Next" button below after ensuring so.', justification = 'center')],
        [sg.Button('Back'), sg.Button('Next'), sg.Button('Exit')]]

layout5 = [[sg.Text('Pet question 2')],
           [sg.Text('How many times per day would you like your pet to be fed?')],
           [sg.Input('', key = 'pet_one_dispenses_per_day', expand_x=True, justification='left')],
           [sg.Text('How much should each meal be (cups)?')],
           [sg.Input('', key = 'pet_one_amount_dispensed', expand_x=True, justification='left')],
           [sg.Text('How many increments should the food be dispensed?')],
           [sg.Input('', key = 'pet_one_increments', expand_x=True, justification='left')],
           [sg.Text('How many seconds in between each increment (seconds)?')],
           [sg.Input('', key = 'pet_one_time_between_increments', expand_x=True, justification='left')],
        [sg.Button('Back'), sg.Button('Exit')]]

layout = [[sg.Column(phone_page, key='1'), sg.Column(layout1, visible=False, key='2'), sg.Column(layout2, visible=False, key='3'), sg.Column(layout3, visible=False, key='4'), sg.Column(layout4, visible=False, key='5'), sg.Column(layout5, visible=False, key='6')]]

window = sg.Window('Swapping the contents of a window', layout)

layout_num = 1 # The currently visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event == 'phone_number':
        if values['phone_number'][-1] not in ('0123456789'):
            sg.popup("Only digits allowed")
            window['phone_number'].update(values['phone_number'][:-1])
    elif event in (None, 'Exit'):
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