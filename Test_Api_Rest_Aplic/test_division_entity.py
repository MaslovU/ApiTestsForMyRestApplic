import pytest

ENDPOINT2 = 'division'


@pytest.mark.parametrize('endpoint2', [ENDPOINT2])
def test_endpoints_encoding(client, endpoint2):
    """Encoding"""
    response = client.do_get(endpoint2)
    jsons = response.json()
    assert jsons[0]['text'] == 'QA'
