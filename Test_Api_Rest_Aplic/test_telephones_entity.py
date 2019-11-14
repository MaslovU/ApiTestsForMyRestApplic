"""Tests for Telephone's entity"""

import pytest
from Test_Api_Rest_Aplic.consts import ENDPOINT6, HEADERS, DATA_TELEPHONE_1, DATA_TELEPHONE_2, PARAM_TELEPHONE_4, \
    PARAM_TELEPHONE_6, PARAM_TELEPHONE_7


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_endpoints_encoding(client, endpoint):
    """Encoding"""
    response = client.do_get(endpoint)
    jsons = response.json()
    assert jsons[0]['text'] != '133'


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_status_code(client, endpoint):
    """Status Code"""
    response = client.do_get(endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url_json(client, endpoint):
    """Check Json"""
    response = client.do_get(endpoint)
    assert response.json()


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url_content_type(client, endpoint):
    """Check Content-Type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url_encoding(client, endpoint):
    """Check Transfer-Encoding"""
    response = client.do_get(endpoint)
    assert response.headers['Transfer-Encoding'] == 'chunked'


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url_redirect(client, endpoint):
    """Check redirect"""
    response = client.do_get(endpoint)
    assert not response.is_redirect


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
@pytest.mark.parametrize('param', [PARAM_TELEPHONE_6])
def test_endpoints_division(client, endpoint, param):
    """Check employee in list"""
    endpoint2 = '/'.join([endpoint, param])
    response = client.do_get(endpoint2)
    jsons = response.json()
    assert jsons['text'] == '123546'


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA_TELEPHONE_1])
@pytest.mark.parametrize('param', [PARAM_TELEPHONE_4])
@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url_code(client, endpoint, data, param, headers):
    """Check PUT Method Status Code"""
    new_endpoint = '/'.join([endpoint, param])
    response = client.do_put(new_endpoint, data=data, headers=headers)
    assert response.status_code == 200


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA_TELEPHONE_2])
@pytest.mark.parametrize('param', [PARAM_TELEPHONE_7])
@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url_text(client, endpoint, data, param, headers):
    """Check PUT Method Status Code"""
    new_endpoint = '/'.join([endpoint, param])
    response = client.do_put(new_endpoint, data=data, headers=headers)
    assert response.text == '{"id":13,"text":"3433656565"}'
