"""Tests for Division's Entity"""

import pytest
from Test_Api_Rest_Aplic.consts import ENDPOINT2, HEADERS, DATA_DIVISION, PARAM_DIV_1, PARAM_DIV_2


@pytest.mark.parametrize('endpoint', [ENDPOINT2])
def test_endpoints_encoding(client, endpoint):
    """Encoding"""
    response = client.do_get(endpoint)
    jsons = response.json()
    assert jsons[0]['text'] != 'QA'


@pytest.mark.parametrize('endpoint', [ENDPOINT2])
def test_status_code(client, endpoint):
    """Status Code"""
    response = client.do_get(endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint', [ENDPOINT2])
def test_url(client, endpoint):
    """Check Json"""
    response = client.do_get(endpoint)
    assert response.json()


@pytest.mark.parametrize('endpoint', [ENDPOINT2])
def test_url(client, endpoint):
    """Check Content-Type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'


@pytest.mark.parametrize('endpoint', [ENDPOINT2])
def test_url(client, endpoint):
    """Check Transfer-Encoding"""
    response = client.do_get(endpoint)
    assert response.headers['Transfer-Encoding'] == 'chunked'


@pytest.mark.parametrize('endpoint', [ENDPOINT2])
def test_url(client, endpoint):
    """Check redirect"""
    response = client.do_get(endpoint)
    assert not response.is_redirect


@pytest.mark.parametrize('endpoint', [ENDPOINT2])
@pytest.mark.parametrize('param_id', [PARAM_DIV_2])
def test_endpoints_division(client, endpoint, param_id):
    """Check employee in list"""
    new_endpoint = '/'.join([endpoint, param_id])
    response = client.do_get(new_endpoint)
    jsons = response.json()
    assert jsons['text'] == 'Durk'


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA_DIVISION])
@pytest.mark.parametrize('param_id', [PARAM_DIV_1])
@pytest.mark.parametrize('endpoint', [ENDPOINT2])
def test_url_put_method(client, endpoint, data, param_id, headers):
    """Check PUT Method Status Code"""
    new_endpoint = '/'.join([endpoint, param_id])
    response = client.do_put(new_endpoint, data=data, headers=headers)
    assert response.status_code == 500
