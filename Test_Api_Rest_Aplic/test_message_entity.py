"""Tests for Message's entity"""

import pytest
from Test_Api_Rest_Aplic.consts import ENDPOINT1, HEADERS, DATA_MESSAGE_1, DATA_MESSAGE_2, \
    PARAM_MESSAGE_1, PARAM_MESSAGE_2


@pytest.mark.parametrize('endpoint', [ENDPOINT1])
def test_endpoints_get_text(client, endpoint):
    """Get text"""
    response = client.do_get(endpoint)
    jsons = response.json()
    assert jsons[0]['text'] == 'Optional'


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA_MESSAGE_2])
@pytest.mark.parametrize('endpoint', [ENDPOINT1])
def test_endpoints_post(client, endpoint, data, headers):
    """POST Status Code"""
    response = client.do_post(endpoint, data, headers=headers)
    checking = client.do_get(endpoint).json()
    assert response.status_code == 200
    assert checking[len(checking)-1]['text'] == "Added from Autotests"


@pytest.mark.parametrize('param', [PARAM_MESSAGE_1])
@pytest.mark.parametrize('endpoint', [ENDPOINT1])
def test_endpoint_delete(client, endpoint, param):
    new_endpoint = '/'.join([endpoint, param])
    response = client.do_delete(new_endpoint)
    resp = client.do_get(new_endpoint)
    assert resp.text == 'null'
    assert response.status_code == 500


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA_MESSAGE_1])
@pytest.mark.parametrize('param', [PARAM_MESSAGE_2])
@pytest.mark.parametrize('endpoint', [ENDPOINT1])
def test_url_text(client, endpoint, data, param, headers):
    """Check PUT Method Status Code"""
    new_endpoint = '/'.join([endpoint, param])
    response = client.do_put(new_endpoint, data=data, headers=headers)
    assert response.text == '{"id":7,"text":"For test","creationDate":null}'
