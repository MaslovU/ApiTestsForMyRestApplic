import pytest

ENDPOINT3 = 'employee'
ENDPOINT4 = 'employees'
ENDPOINT5 = 'employeeFromDiv'
ENDPOINTS = [ENDPOINT3, ENDPOINT4, ENDPOINT5]
PARAM1 = '1'
PARAM2 = 'text=QA'
PARAM3 = 'name=Maslov'
DATA = {"name": "Test"}


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
    """Find employee dy name"""
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


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_status_code(client, endpoint):
    """Status Code"""
    response = client.do_get(endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_headers_content_type(client, endpoint):
    """Content type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-type'] == 'application/json'


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_cookies(client, endpoint):
    """Check Cookies"""
    response = client.do_get(endpoint)
    assert response.cookies


@pytest.mark.parametrize('endpoint', ENDPOINTS)
def test_url(client, endpoint):
    """Check Url"""
    response = client.do_get(endpoint)
    assert response.url


@pytest.mark.parametrize('endpoints', ENDPOINTS)
def test_endpoint_json(client, endpoints):
    """Json"""
    j_s = client.do_json(endpoints)
    assert j_s['status'] == 'success'


@pytest.mark.parametrize('endpoint', ENDPOINTS)
@pytest.mark.parametrize('data', DATA)
def test_endpoints_post(client, endpoint, data):
    """POST Status Code"""
    response = client.do_post(endpoint, data)
    assert response.status_code != 300
