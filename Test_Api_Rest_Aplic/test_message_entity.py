import pytest

ENDPOINT1 = 'message'


@pytest.mark.parametrize('endpoint1', [ENDPOINT1])
def test_endpoints_encoding(client, endpoint1):
    """Encoding"""
    response = client.do_get(endpoint1)
    jsons = response.json()
    assert jsons[0]['text'] == 'First message'
