import pytest

ENDPOINT3 = 'employee'
ENDPOINT4 = 'employees'
ENDPOINT5 = 'employeeFromDiv'
PARAM1 = '1'
PARAM2 = 'text=QA'
PARAM3 = 'name=Maslov'


@pytest.mark.parametrize('endpoint3', [ENDPOINT3])
@pytest.mark.parametrize('param1', PARAM1)
def test_endpoints_encoding(client, endpoint3, param1):
    """Check employee in list"""
    endpoint = '/'.join([endpoint3, param1])
    response = client.do_get(endpoint)
    jsons = response.json()
    assert jsons[0]['text'] == 'Maslov'


@pytest.mark.parametrize('endpoint5', ENDPOINT5)
@pytest.mark.parametrize('param2', PARAM2)
def test_endpoints_encoding(client, endpoint5, param2):
    """Find employee dy division"""
    endpoint = '?'.join([endpoint5, param2])
    response = client.do_get(endpoint)
    jsons = response.json()
    assert jsons[0]['text'] == 'Maslov'


@pytest.mark.parametrize('endpoint3', ENDPOINT3)
@pytest.mark.parametrize('param3', PARAM3)
def test_endpoints_encoding(client, endpoint3, param3):
    """Find employee dy division"""
    endpoint = '?'.join([endpoint3, param3])
    response = client.do_get(endpoint)
    jsons = response.json()
    assert jsons[0]['text'] == 'Maslov'


@pytest.mark.parametrize('endpoint4', ENDPOINT4)
def test_endpoints_encoding(client, endpoint4):
    """Find all employees"""
    response = client.do_get(endpoint4)
    jsons = response.json()
    assert jsons[0]['text'] == 'Maslov'
