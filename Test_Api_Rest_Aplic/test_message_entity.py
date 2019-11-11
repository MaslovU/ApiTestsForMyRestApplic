import pytest

ENDPOINT1 = 'message'
PARAM = '1'
PARAM2 = '5'


@pytest.mark.parametrize('endpoint1', [ENDPOINT1])
def test_endpoints_get_text(client, endpoint1):
    """Get text"""
    response = client.do_get(endpoint1)
    jsons = response.json()
    assert jsons[0]['text'] == 'Optional'


@pytest.mark.parametrize('param', [PARAM])
@pytest.mark.parametrize('endpoint1', [ENDPOINT1])
def test_endpoint_delete(client, endpoint1, param):
    endpoint = '/'.join([endpoint1, param])
    response = client.do_delete(endpoint)
    resp = client.do_get(endpoint)
    assert resp.text == 'null'
    assert response.status_code == 500
