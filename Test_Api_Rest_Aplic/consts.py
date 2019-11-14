import json

ENDPOINT1 = 'message'
ENDPOINT2 = 'division'
ENDPOINT3 = 'employee'
ENDPOINT4 = 'employees'
ENDPOINT5 = 'employeeFromDiv'
ENDPOINT6 = 'telephone'

ENDPOINTS = [ENDPOINT3, ENDPOINT4, ENDPOINT5]

HEADERS = {'Content-type': 'application/json', 'Accept': 'application/json'}

PARAM_EMPLOYEE_1 = '1'
PARAM_EMPLOYEE_2 = 'text=QA'
PARAM_EMPLOYEE_3 = 'name=Yury'
PARAM_DIV_1 = '6'
PARAM_DIV_2 = '21'
PARAM_TELEPHONE_1 = '4'
PARAM_TELEPHONE_2 = '2'
PARAM_TELEPHONE_3 = '13'
PARAM_MESSAGE_1 = '1'
PARAM_MESSAGE_2 = '7'

DATA_EMPLOYEE = json.dumps({"name": "MaslovU", "newTelephone": {"text": "777"}, "newDivision": {"text": "Pycharm"}})
DATA_DIVISION = json.dumps({'text': 'QA'})
DATA_TELEPHONE_1 = json.dumps({'text': '177771'})
DATA_TELEPHONE_2 = json.dumps({'text': '3433656565'})
DATA_MESSAGE_1 = json.dumps({'text': 'For test'})
DATA_MESSAGE_2 = json.dumps({'text': 'Added from Autotests'})
