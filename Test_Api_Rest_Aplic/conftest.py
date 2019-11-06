"""Conftest"""
import json
import pytest
import requests


class APIClient:
    """APIClient"""
    def __init__(self, address='http://localhost:8080/'):
        self.address = address

    def do_get(self, endpoint, verify_ssl=False):
        """Get-method"""
        url = '/'.join([self.address, endpoint])
        return requests.get(url, verify=verify_ssl)  # возможно надо удалить verify

    def do_post(self, endpoint, data=None, verify_ssl=False):
        """POST-method"""
        url = '/'.join([self.address, endpoint])
        return requests.post(url, data, verify=verify_ssl)

    def do_json(self, endpoint, verify_ssl=False):
        """JSON-method"""
        url = '/'.join([self.address, endpoint])
        req = requests.get(url, verify=verify_ssl)
        return json.loads(req.text)


def pytest_addoption(parser):
    """parser"""
    parser.addoption('--address', action='store')


@pytest.fixture
def client(request):
    """client"""
    return APIClient(request.config.getoption('--address'))
