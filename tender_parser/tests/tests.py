from main import get_print_form
from requests.exceptions import Timeout


class ResponseFake:
    def __init__(self, status_code, text=""):
        self.status_code = status_code
        self.text = text


class RequestFake:
    def __init__(self, status_code, text=""):
        self.response = ResponseFake(status_code, text)

    def get(self, url, headers=None, timeout=5):
        return self.response


def test_get_print_form_success():
    request = RequestFake(status_code=200, text="Success")
    result = get_print_form(request, "http://example.com", {})
    assert result == "Success"


def test_get_print_form_error_status():
    request = RequestFake(status_code=404)
    result = get_print_form(request, "http://example.com", {})
    assert result is None


def test_get_print_form_exception_timeout():
    class RequestFakeError:
        def get(self, url, headers=None):
            raise Exception("Network error")

    request = RequestFakeError()
    result = get_print_form(request, "http://example.com", {})
    assert result is None


class RequestFakeTimeout:
    def get(self, url, headers=None, timeout=None):
        raise Timeout("Request timed out")


def test_get_print_form_timeout():
    request = RequestFakeTimeout()
    result = get_print_form(request, "http://example.com", {})
    assert result is None


def test_get_print_form_exception():
    class RequestFakeError:
        def get(self, url, headers=None):
            raise Exception("Network error")

    request = RequestFakeError()
    result = get_print_form(request, "http://example.com", {})
    assert result is None
