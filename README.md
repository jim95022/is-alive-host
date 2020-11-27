<h1>Решение</h1>
<ul>
  <li>api/app.py - функция is_alive_host проверяет, что запрашиваемый хост возвращает http status 100 - 399 и  возвращает True/False</li>
  <li>api/test.py - представлено тестирование функции is_alive_host</li>
  <li>api/app.py - api сервис который работает на fastapi</li>
  <p>пример использования</p>
<code>

>> curl https://isalivehost.herokuapp.com/
<pre>
{
    "info":"You need to specify https://isalivehost.herokuapp.com/healthz?hostname='<'place here the hostname you are interested in'>'"
}
</pre>

>> curl https://isalivehost.herokuapp.com/healthz?hostname=semrush.com
<pre>
{ 
    "status": "up"
}
</pre>
</code>

<li>Добавил небольшую <a href=https://isalivehostflask.herokuapp.com/>страницу</a> на FLASK для демонстрации использования API</li>
<li>C помощью Dockergile можно собрать докер образ и запустить его</li>
</ul>  

<hr>
<h1>Задание</h1>

# python_intern
---

## requirements

- python 3.9
- В изначальном коде менять можно *всё*, вплоть до структуры файлов. 
- Использовать можно всё что угодно. 
- Таски со звёздочкой можно пропускать (или делать часть из них)
- Решение выложить через fork/копию/etc репозитория на github


## TODO

- реализовать функцию [is_alive_host](./app.py)

- покрыть функцию [тестами](./tests.py)

- развернуть вокруг функции веб сервис c помощью [fastapi](https://fastapi.tiangolo.com/)
```
>> curl your_service.loc:8001/healthz?hostname=semrush.com
{status: [up|down]}
```

- задача со *звёздочкой*: завернуть приложение в docker
- задача на *две звёздочки*: выложить куда-либо (heroku/DigitalOcean/etc) с помощью github-actions/gitlab/jenkins/etc
