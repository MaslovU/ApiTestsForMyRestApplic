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
        return requests.get(url)

    def do_post(self, endpoint, data, headers):
        """POST-method"""
        url = '/'.join([self.address, endpoint])
        return requests.post(url, data=data, headers=headers)

    def do_put(self, endpoint, data, headers):
        """POST-method"""
        url = '/'.join([self.address, endpoint])
        return requests.put(url, data=data, headers=headers)

    def do_delete(self, endpoint):
        """Delete-method"""
        url = '/'.join([self.address, endpoint])
        return requests.delete(url)

    def do_json(self, endpoint):
        """JSON-method"""
        url = '/'.join([endpoint])
        req = requests.get(url)
        return json.loads(req.text)


def pytest_addoption(parser):
    """parser"""
    parser.addoption('--address', action='store', default='http://localhost:8080')


@pytest.fixture(autouse=True)
def client(request):
    """client"""
    return APIClient()
