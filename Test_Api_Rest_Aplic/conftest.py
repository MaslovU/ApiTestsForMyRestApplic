"""Conftest"""
import json
import pytest
import requests


class APIClient:
    """APIClient"""
    def __init__(self, address='http://localhost:9000'):
        self.address = address

    def do_get(self, endpoint):
        """Get-method"""
        url = '/'.join([self.address, endpoint])
        return requests.get(url)  # возможно надо удалить verify

    # def do_post(self, endpoint, data=None, verify_ssl=False):
    #     """POST-method"""
    #     url = '/'.join([endpoint])
    #     return requests.post(url, data, verify=verify_ssl)
    #
    # def do_json(self, endpoint, verify_ssl=False):
    #     """JSON-method"""
    #     url = '/'.join([endpoint])
    #     req = requests.get(url, verify=verify_ssl)
    #     return json.loads(req.text)


def pytest_addoption(parser):
    """parser"""
    parser.addoption('--address', action='store', default='http://localhost:8080')


@pytest.fixture(autouse=True)
def client(request):
    """client"""
    return APIClient()
