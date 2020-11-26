"""
app tests example

"""

from app import is_alive_host


def test_live():
    assert is_alive_host('semrush.com')
    assert is_alive_host('https://www.semrush.com/')
    assert is_alive_host('http://www.semrush.com/')
    assert is_alive_host('https://semrush.com/')
    assert is_alive_host('google.com')
    assert is_alive_host('google.com:80')
    assert is_alive_host('193.58.251.11')
    assert is_alive_host('vk.com')


def test_down():
    assert not is_alive_host('invalid.domain.son')[0]
    assert not is_alive_host('semrush')[0]
    assert not is_alive_host('test')[0]
    assert not is_alive_host('google')[0]
    assert not is_alive_host('1243')[0]
    assert not is_alive_host()[0]
    assert not is_alive_host('127.0.0.1:5000')[0] # but it may be available if the localhost application is active

test_live()
test_down()