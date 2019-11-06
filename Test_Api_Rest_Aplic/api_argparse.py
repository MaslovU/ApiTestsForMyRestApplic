"""ARGPARSE"""
import argparse
import subprocess
ALL_ENTITY = 'python -m pytest -s -v /home/yury/PycharmProjects/uiTestsForMyRestAplic'
DIVISION = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_division_entity.py'
EMPLOYEE = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_employee_entity.py'
MESSAGE = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_message_entity.py'
TELEPHONE = 'python -m pytest -s -v /home/yury/PycharmProjects/Otus/Test_API/test_telephones_entity.py'

PARSER = argparse.ArgumentParser(description='Test API throw Argparse')
PARSER.add_argument('--entity',
                    dest='entity',
                    action='store',
                    default=["division", "employee", "message", "telephones"],
                    help='websites: "division", "employee", "message", "telephones"')
ARGS = PARSER.parse_args()
URLS_ADR = ARGS.site
ENTITIES = ["division", "employee", "message", "telephones"]


if URLS_ADR == ENTITIES:
    subprocess.run(ALL_ENTITY, shell=True)
else:
    assert URLS_ADR in ENTITIES
    if URLS_ADR == 'division':
        subprocess.run(DIVISION, shell=True)
    if URLS_ADR == 'employee':
        subprocess.run(EMPLOYEE, shell=True)
    if URLS_ADR == 'message':
        subprocess.run(MESSAGE, shell=True)
    if URLS_ADR == 'telephones':
        subprocess.run(TELEPHONE, shell=True)
