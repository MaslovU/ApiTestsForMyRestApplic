import json

import pytest

ENDPOINT2 = 'division'
DATA = json.dumps({'text': 'QA'})
PARAM4 = '6'
PARAM5 = '21'
HEADERS = {'Content-type': 'application/json', 'Accept': 'application/json'}


@pytest.mark.parametrize('endpoint2', [ENDPOINT2])
def test_endpoints_encoding(client, endpoint2):
    """Encoding"""
    response = client.do_get(endpoint2)
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


@pytest.mark.parametrize('endpoint2', [ENDPOINT2])
@pytest.mark.parametrize('param5', [PARAM5])
def test_endpoints_division(client, endpoint2, param5):
    """Check employee in list"""
    endpoint2 = '/'.join([endpoint2, param5])
    response = client.do_get(endpoint2)
    jsons = response.json()
    assert jsons['text'] == 'Develop'


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA])
@pytest.mark.parametrize('param4', [PARAM4])
@pytest.mark.parametrize('endpoint2', [ENDPOINT2])
def test_url(client, endpoint2, data, param4, headers):
    """Check PUT Method Status Code"""
    endpoint = '/'.join([endpoint2, param4])
    response = client.do_put(endpoint, data=data, headers=headers)
    assert response.status_code == 500
