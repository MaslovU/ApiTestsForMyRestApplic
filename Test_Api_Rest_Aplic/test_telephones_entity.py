import json

import pytest

ENDPOINT6 = 'telephone'
DATA = json.dumps({'text': '177771'})
DATA2 = json.dumps({'text': '3433656565'})
PARAM4 = '4'
PARAM6 = '2'
PARAM7 = '13'
HEADERS = {'Content-type': 'application/json', 'Accept': 'application/json'}


@pytest.mark.parametrize('endpoint6', [ENDPOINT6])
def test_endpoints_encoding(client, endpoint6):
    """Encoding"""
    response = client.do_get(endpoint6)
    jsons = response.json()
    assert jsons[0]['text'] != '133'


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_status_code(client, endpoint):
    """Status Code"""
    response = client.do_get(endpoint)
    assert response.status_code == 200


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url(client, endpoint):
    """Check Json"""
    response = client.do_get(endpoint)
    assert response.json()


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url(client, endpoint):
    """Check Content-Type"""
    response = client.do_get(endpoint)
    assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url(client, endpoint):
    """Check Transfer-Encoding"""
    response = client.do_get(endpoint)
    assert response.headers['Transfer-Encoding'] == 'chunked'


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
def test_url(client, endpoint):
    """Check redirect"""
    response = client.do_get(endpoint)
    assert not response.is_redirect


@pytest.mark.parametrize('endpoint', [ENDPOINT6])
@pytest.mark.parametrize('param', [PARAM6])
def test_endpoints_division(client, endpoint, param):
    """Check employee in list"""
    endpoint2 = '/'.join([endpoint, param])
    response = client.do_get(endpoint2)
    jsons = response.json()
    assert jsons['text'] == '123546'


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA])
@pytest.mark.parametrize('param4', [PARAM4])
@pytest.mark.parametrize('endpoint6', [ENDPOINT6])
def test_url_code(client, endpoint6, data, param4, headers):
    """Check PUT Method Status Code"""
    endpoint = '/'.join([endpoint6, param4])
    response = client.do_put(endpoint, data=data, headers=headers)
    assert response.status_code == 200


@pytest.mark.parametrize('headers', [HEADERS])
@pytest.mark.parametrize('data', [DATA2])
@pytest.mark.parametrize('param4', [PARAM7])
@pytest.mark.parametrize('endpoint6', [ENDPOINT6])
def test_url_text(client, endpoint6, data, param4, headers):
    """Check PUT Method Status Code"""
    endpoint = '/'.join([endpoint6, param4])
    response = client.do_put(endpoint, data=data, headers=headers)
    assert response.text == '{"id":13,"text":"3433656565"}'
