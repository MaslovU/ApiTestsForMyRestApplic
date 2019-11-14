"""Test for Employee Table"""

import pytest
from Test_Api_Rest_Aplic.consts import HEADERS, ENDPOINT3, ENDPOINT4, ENDPOINT5, ENDPOINTS, \
    PARAM_EMPLOYEE_1, PARAM_EMPLOYEE_2, PARAM_EMPLOYEE_3, DATA_EMPLOYEE


@pytest.mark.parametrize('endpoint', [ENDPOINT3])
@pytest.mark.parametrize('param_id', [PARAM_EMPLOYEE_1])
def test_endpoints_employee(client, endpoint, param_id):
    """Check employee in list"""
    new_endpoint = '/'.join([endpoint, param_id])
    response = client.do_get(new_endpoint)
    jsons = response.json()
    assert jsons['name'] == 'Yury'


@pytest.mark.parametrize('endpoint', [ENDPOINT5])
@pytest.mark.parametrize('param_division', [PARAM_EMPLOYEE_2])
def test_endpoints_by_division(client, endpoint, param_division):
    """Find employee dy division"""
    new_endpoint = '?'.join([endpoint, param_division])
    response = client.do_get(new_endpoint)
    jsons = response.json()
    assert jsons[0]['name'] != 'Maslov'


@pytest.mark.parametrize('endpoint', [ENDPOINT3])
@pytest.mark.parametrize('param_name', [PARAM_EMPLOYEE_3])
def test_endpoints_by_name(client, endpoint, param_name):
    """Find employee dy name"""
    new_endpoint = '?'.join([endpoint, param_name])
    response = client.do_get(new_endpoint)
    jsons = response.json()
    assert jsons[0]['name'] == 'Yury'


@pytest.mark.parametrize('endpoint', [ENDPOINT4])
def test_endpoints_all_employees(client, endpoint):
    """Find all employees"""
    response = client.do_get(endpoint)
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


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA_EMPLOYEE])
@pytest.mark.parametrize('endpoint', [ENDPOINT3])
def test_endpoints_post(client, endpoint, data, headers):
    """POST Status Code"""
    response = client.do_post(endpoint, data, headers=headers)
    assert response.status_code != 300
