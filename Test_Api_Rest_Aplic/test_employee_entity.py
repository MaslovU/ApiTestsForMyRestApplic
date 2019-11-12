import pytest

ENDPOINT3 = 'employee'
ENDPOINT4 = 'employees'
ENDPOINT5 = 'employeeFromDiv'
ENDPOINTS = [ENDPOINT3, ENDPOINT4, ENDPOINT5]
PARAM1 = '1'
PARAM2 = 'text=QA'
PARAM3 = 'name=Yury'
DATA = {"name": "Test"}


@pytest.mark.parametrize('endpoint3', [ENDPOINT3])
@pytest.mark.parametrize('param1', [PARAM1])
def test_endpoints_employee(client, endpoint3, param1):
    """Check employee in list"""
    endpoint = '/'.join([endpoint3, param1])
    response = client.do_get(endpoint)
    jsons = response.json()
    # check for several employee
    assert jsons['name'] == 'Yury'


@pytest.mark.parametrize('endpoint5', [ENDPOINT5])
@pytest.mark.parametrize('param2', [PARAM2])
def test_endpoints_by_division(client, endpoint5, param2):
    """Find employee dy division"""
    endpoint = '?'.join([endpoint5, param2])
    response = client.do_get(endpoint)
    jsons = response.json()
    assert jsons[0]['name'] != 'Maslov'


@pytest.mark.parametrize('endpoint3', [ENDPOINT3])
@pytest.mark.parametrize('param3', [PARAM3])
def test_endpoints_by_name(client, endpoint3, param3):
    """Find employee dy name"""
    endpoint = '?'.join([endpoint3, param3])
    response = client.do_get(endpoint)
    jsons = response.json()
    assert jsons[0]['name'] == 'Yury'


@pytest.mark.parametrize('endpoint4', [ENDPOINT4])
def test_endpoints_all_employees(client, endpoint4):
    """Find all employees"""
    response = client.do_get(endpoint4)
    jsons = response.json()
    assert jsons[0]['name'] != 'Maslov'
    assert jsons[0]['name'] == 'Yury'


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_status_code(client, endpoint):
    """Status Code"""
    response = client.do_get(endpoint)
    if endpoint == 'employees':
        assert response.status_code == 200
    else:
        assert response.status_code == 400


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_headers_content_type(client, endpoint):
    """Content type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-type'] == 'application/json;charset=UTF-8'


@pytest.mark.parametrize('endpoint', [ENDPOINT4])
def test_url(client, endpoint):
    """Check Url Json"""
    response = client.do_get(endpoint)
    assert response.json()


@pytest.mark.parametrize('data', [DATA])
@pytest.mark.parametrize('endpoint3', [ENDPOINT3])
def test_endpoints_post(client, endpoint3, data):
    """POST Status Code"""
    #разобраться с форматом данных
    response = client.do_post(endpoint3, data=data)
    assert response.status_code != 300
