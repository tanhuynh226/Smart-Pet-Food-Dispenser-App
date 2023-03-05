import PySimpleGUI as sg
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

#sql functions 
def sql_phone(cur, phone_number):
    sql = "UPDATE Gen SET phone_number = " + phone_number + ";"
    cur.execute(sql)

def sql_motion_calibration(cur):
    sql = "UPDATE Gen SET calibrate_distance = true WHERE calibrate_distance = false;"
    cur.execute(sql)

def sql_pet1_id(cur):
    sql = "UPDATE Dispenser1 SET detect_pet = true WHERE detect_pet = false;"
    cur.execute(sql)

def sql_pet1_info(cur, pet_one_dispenses_per_day, pet_one_amount_dispensed, pet_one_increments, pet_one_time_between_increments):
    sql = "UPDATE Dispenser1 SET dispenses_per_day = " +  pet_one_dispenses_per_day + ", amount_dispensed = " + pet_one_amount_dispensed + ", increments = " + pet_one_increments + ", time_between_increments = " + pet_one_time_between_increments +  ";"
    cur.execute(sql)
    

def sql_pet2_id(cur):
    sql = "UPDATE Dispenser2 SET detect_pet = true WHERE detect_pet = false;"
    cur.execute(sql) 

def sql_pet2_info(cur, pet_two_dispenses_per_day, pet_two_amount_dispensed, pet_two_increments, pet_two_time_between_increments):
    sql = "UPDATE Dispenser2 SET dispenses_per_day = " +  pet_two_dispenses_per_day + ", amount_dispensed = " + pet_two_amount_dispensed + ", increments = " + pet_two_increments + ", time_between_increments = " + pet_two_time_between_increments +  ";"
    cur.execute(sql)

pet1_breed = 'Blank'
pet2_breed = 'Blank'

def sql_getpet(cur):
    sql = "SELECT pet_breed FROM Dispenser1"
    cur.execute(sql)
    global pet1_breed 
    pet1_breed= cur.fetchone()[0]

    sql = "SELECT pet_breed FROM Dispenser2"
    cur.execute(sql)
    global pet2_breed 
    pet2_breed = cur.fetchone()[0]

#functions needed for desktop window layout
def get_title_str(layout):
    return layout[0][0].DisplayText

def get_last_layout_num(layout_order):
    return len(layout_order) - 1

if __name__ == '__main__':
    db = pymysql.connect(host=os.environ['AWS_RDS_ENDPOINT'],
                            user=os.environ['AWS_RDS_USERNAME'],
                            passwd=os.environ['AWS_RDS_PASSWORD'],
                            db='dispenser',
                            autocommit=True)
    cur = db.cursor()
    sql_getpet(cur)

    phone_page = [[sg.Text('Enter your phone number (include country number):', font = ('Arial Bold', 12))],
                [sg.Input('', key = 'phone_number', enable_events = True, expand_x=True, justification='left')],
                [sg.Button('Next', key = 'phone_edit')], 
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

    pet_q1 = [[sg.Text('Input 1st Pet Info', font = ('Arial Bold', 12))],
            [sg.Text('How many times per day would you like your pet to be fed?')],
            [sg.Input('', key = 'pet_one_dispenses_per_day', expand_x=True, justification='left')],
            [sg.Text('How much should each meal be (cups)?')],
            [sg.Input('', key = 'pet_one_amount_dispensed', expand_x=True, justification='left')],
            [sg.Text('How many increments should the food be dispensed?')],
            [sg.Input('', key = 'pet_one_increments', expand_x=True, justification='left')],
            [sg.Text('How many seconds in between each increment (seconds)?')],
            [sg.Input('', key = 'pet_one_time_between_increments', expand_x=True, justification='left')],
            [sg.Button('Back'), sg.Button('Next', key = 'pet1_info')], 
            [sg.Button('Exit'), sg.Button('Home')]]

    pet_id2 = [[sg.Text('Dispenser 2 Pet Identification', font = ('Arial Bold', 12))], 
            [sg.Text('Please place your second pet in front of the camera. Click the "Next" button below after ensuring so.', justification = 'center')],
            [sg.Button('Ready', key = 'pet_id2')],
            [sg.Button('Back'), sg.Button('Next')], 
            [sg.Button('Exit'), sg.Button('Home')]]

    pet_q2 = [[sg.Text('Input 2nd Pet Info', font = ('Arial Bold', 12))],
            [sg.Text('How many times per day would you like your pet to be fed?')],
            [sg.Input('', key = 'pet_two_dispenses_per_day', expand_x=True, justification='left')],
            [sg.Text('How much should each meal be (cups)?')],
            [sg.Input('', key = 'pet_two_amount_dispensed', expand_x=True, justification='left')],
            [sg.Text('How many increments should the food be dispensed?')],
            [sg.Input('', key = 'pet_two_increments', expand_x=True, justification='left')],
            [sg.Text('How many seconds in between each increment (seconds)?')],
            [sg.Input('', key = 'pet_two_time_between_increments', expand_x=True, justification='left')],
            [sg.Button('Back'), sg.Button('Next', key = 'pet2_info')], 
            [sg.Button('Exit'), sg.Button('Home')]]

    layout_order = [phone_page, calibration_page, pet_id1, pet_q1, pet_id2, pet_q2] # The page order that the initial setup takes

    home_button_order = ['Edit Phone Number', 'Recalibrate Motion Sensor', 'Recalibrate Dispenser 1 Pet ID', 'Edit Dispenser 1 Attributes', 'Recalibrate Dispenser 2 Pet ID', 'Edit Dispenser 2 Attributes']
    home_dispenser_label_1 = [[sg.Text('Dispenser 1 Pet')]] + [[sg.Text(pet1_breed)]]
    home_dispenser_label_2 = [[sg.Text('Dispenser 2 Pet')]] + [[sg.Text(pet2_breed)]]
    home_page = [[sg.Text('Home Page', font = ('Arial Bold', 12))]] + [[sg.Column(home_dispenser_label_1), sg.Column(home_dispenser_label_2)]] + [[sg.Button(str(button_name))] for button_name in home_button_order] + [[sg.Button('Exit')]]

    layout_order.append(home_page)


    layout = [[sg.Column(layout, key=str(idx), visible=(idx==0)) for idx, layout in enumerate(layout_order)]]

    window = sg.Window('Smart Pet Food Dispenser', layout)

    layout_num = 0 # The first layout in [layout_order] has key 0 and is visible

    while True:
        event, values = window.read()
        #print(values)
        
        if 'Exit' in event or event is None:
            break
        elif event == 'phone_number':
            if values['phone_number'] and values['phone_number'][-1] not in ('0123456789'):
                sg.popup("Only digits allowed")
                window['phone_number'].update(values['phone_number'][:-1])

        elif event == 'phone_edit':
            # TODO: wait for db update from backend
            sql_phone(cur, values['phone_number'])
            window[f'{layout_num}'].update(visible=False)
            layout_num += 1
            window[f'{layout_num }'].update(visible=True)
            print("Phone added")

    ###the READY buttons don't need to go to the next page, they just need to send data to the backend
        elif event == 'calibration':
            # TODO: wait for db update from backend
            sql_motion_calibration(cur)
            print("DO CALIBRATION")

        elif event == 'pet_id1':
            # TODO: wait for db update from backend
            sql_pet1_id(cur)
            print("DO PET ID 1")

        elif event == 'pet_id2':
            # TODO: wait for db update from backend
            sql_pet2_id(cur)
            print("DO PET ID 2")

    ###whenever the user pressed 'Next', it is considered a submit button and should update the user inputs into the backend
        elif event == 'pet1_info':
            # TODO: wait for db update from backend
            sql_pet1_info(cur, values['pet_one_dispenses_per_day'], values['pet_one_amount_dispensed'], values['pet_one_increments'], values['pet_one_time_between_increments'])
            window[f'{layout_num}'].update(visible=False)
            layout_num += 1
            window[f'{layout_num }'].update(visible=True)
            print("EDITED PET 1 INFO")

        elif event == 'pet2_info':
            # TODO: wait for db update from backend
            sql_pet2_info(cur, values['pet_two_dispenses_per_day'], values['pet_two_amount_dispensed'], values['pet_two_increments'], values['pet_two_time_between_increments'])
            window[f'{layout_num}'].update(visible=False)
            layout_num += 1
            window[f'{layout_num }'].update(visible=True)
            print("EDITED PET 2 INFO")

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

