from app import is_alive_host


def test_live():
    assert is_alive_host('semrush.com')
    assert is_alive_host('https://www.semrush.com/')
    assert is_alive_host('http://www.semrush.com/')
    assert is_alive_host('http://www.semrush.com/somepage/')
    assert is_alive_host('https://semrush.com')
    assert is_alive_host('google.com')
    assert is_alive_host('google.com:80')
    assert is_alive_host('193.58.251.11')
    assert is_alive_host('vk.com')


def test_down():
    assert not is_alive_host('invalid.domain.son')
    assert not is_alive_host('http')
    assert not is_alive_host('semrush')
    assert not is_alive_host('test')
    assert not is_alive_host('google')
    assert not is_alive_host('1243')
    assert not is_alive_host()
    assert not is_alive_host('127.0.0.1:5000') # but it may be available if the localhost application is active

test_live()
test_down()