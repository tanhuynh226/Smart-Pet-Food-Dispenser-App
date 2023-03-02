import PySimpleGUI as sg
import pymysql

def get_title_str(layout):
    return layout[0][0].DisplayText

def get_last_layout_num(layout_order):
    return len(layout_order) - 1

def sql_calls():
    return 

phone_page = [[sg.Text('Enter your phone number (include country number):', font = ('Arial Bold', 12))],
              [sg.Input('', key = 'phone_number', enable_events = True, expand_x=True, justification='left')],
            [sg.Button('Next')], 
            [sg.Button('Exit'), sg.Button('Home')]]

calibration_page = [[sg.Text('Motion Detection Calibration', font = ('Arial Bold', 12))], 
           [sg.Text('Please do not place anything in front of the device. Click the "Ready" button below after ensuring so.', justification = 'center')],
           [sg.Button('Ready', key = 'calibration')],
        [sg.Button('Back'), sg.Button('Next')], 
        [sg.Button('Exit'), sg.Button('Home')]]

pet_id1 = [[sg.Text('Dispenser 1 Pet Identification', font = ('Arial Bold', 12))], 
           [sg.Text('Please place your first pet in front of the camera. Click the "Ready" button below after ensuring so.', justification = 'center')],
           [sg.Button('Ready', key = 'pet_id1')],
        [sg.Button('Back'), sg.Button('Next')],
         [sg.Button('Exit'), sg.Button('Home')]]

pet_q1 = [[sg.Text('Input 1st Pet Info')],
           [sg.Text('How many times per day would you like your pet to be fed?')],
           [sg.Input('', key = 'pet_one_dispenses_per_day', expand_x=True, justification='left')],
           [sg.Text('How much should each meal be (cups)?')],
           [sg.Input('', key = 'pet_one_amount_dispensed', expand_x=True, justification='left')],
           [sg.Text('How many increments should the food be dispensed?')],
           [sg.Input('', key = 'pet_one_increments', expand_x=True, justification='left')],
           [sg.Text('How many seconds in between each increment (seconds)?')],
           [sg.Input('', key = 'pet_one_time_between_increments', expand_x=True, justification='left')],
        [sg.Button('Back'), sg.Button('Next')], 
        [sg.Button('Exit'), sg.Button('Home')]]

pet_id2 = [[sg.Text('Dispenser 2 Pet Identification', font = ('Arial Bold', 12))], 
           [sg.Text('Please place your second pet in front of the camera. Click the "Next" button below after ensuring so.', justification = 'center')],
           [sg.Button('Ready', key = 'pet_id2')],
        [sg.Button('Back'), sg.Button('Next')], 
        [sg.Button('Exit'), sg.Button('Home')]]

pet_q2 = [[sg.Text('Input 2nd Pet Info')],
           [sg.Text('How many times per day would you like your pet to be fed?')],
           [sg.Input('', key = 'pet_two_dispenses_per_day', expand_x=True, justification='left')],
           [sg.Text('How much should each meal be (cups)?')],
           [sg.Input('', key = 'pet_two_amount_dispensed', expand_x=True, justification='left')],
           [sg.Text('How many increments should the food be dispensed?')],
           [sg.Input('', key = 'pet_two_increments', expand_x=True, justification='left')],
           [sg.Text('How many seconds in between each increment (seconds)?')],
           [sg.Input('', key = 'pet_two_time_between_increments', expand_x=True, justification='left')],
        [sg.Button('Back'), sg.Button('Next')], 
        [sg.Button('Exit'), sg.Button('Home')]]

layout_order = [phone_page, calibration_page, pet_id1, pet_q1, pet_id2, pet_q2] # The page order that the initial setup takes

home_button_order = ['Edit Phone Number', 'Recalibrate Motion Sensor', 'Recalibrate Dispenser 1 Pet ID', 'Edit Dispenser 1 Attributes', 'Recalibrate Dispenser 2 Pet ID', 'Edit Dispenser 2 Attributes']
home_page = [[sg.Text('Home page')]] + [[sg.Button(str(button_name))] for button_name in home_button_order] + [[sg.Button('Exit')]]

layout_order.append(home_page)


layout = [[sg.Column(layout, key=str(idx), visible=(idx==0)) for idx, layout in enumerate(layout_order)]]

window = sg.Window('Swapping the contents of a window', layout)

layout_num = 0 # The first layout in [layout_order] has key 0 and is visible
while True:
    event, values = window.read()
    print(event, values)
    
    if 'Exit' in event or event is None:
        break
    elif event == 'phone_number':
        if values['phone_number'] and values['phone_number'][-1] not in ('0123456789'):
            sg.popup("Only digits allowed")
            window['phone_number'].update(values['phone_number'][:-1])
    elif event == 'calibration':
        # TODO: wait for db update from backend
        print("DO CALIBRATION")
    elif event == 'pet_id1':
        # TODO: wait for db update from backend
        print("DO PET ID 1")
    elif event == 'pet_id2':
        # TODO: wait for db update from backend
        print("DO PET ID 2")
    elif "Next" in event:
        window[f'{layout_num}'].update(visible=False)
        layout_num += 1
        window[f'{layout_num }'].update(visible=True)
    elif "Back" in event:
        window[f'{layout_num}'].update(visible=False)
        layout_num -= 1
        window[f'{layout_num }'].update(visible=True)
    elif "Home" in event:
        window[f'{layout_num}'].update(visible=False)
        layout_num = get_last_layout_num(layout_order)
        window[f'{layout_num }'].update(visible=True)
    elif layout_num == get_last_layout_num(layout_order):
        # For the home page, find the page with the title corresponding with the button text
        for idx, button_name in enumerate(home_button_order):
            if button_name in event:
                window[f'{layout_num}'].update(visible=False)
                layout_num = idx
                window[f'{layout_num }'].update(visible=True)

window.close()