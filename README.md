<h1>Решение</h1>
<ul>
  <li>api/app.py - функция <b>is_alive_host</b> проверяет, что запрашиваемый хост возвращает http status 100 - 399 и  возвращает True/False</li>
  <li>api/test.py - представлено тестирование функции <b>is_alive_host</b></li>
  <li>api/app.py - API сервис который работает на <b>fastapi</b></li>
  <li>Загрузил сервис на <a href='https://isalivehost.herokuapp.com/'>хероку</a></li>
  <li>Завернул приложение в docker</li>
  <li>Добавил небольшую <a href=https://isalivehostflask.herokuapp.com/>страницу</a> на <b>FLASK</b> для демонстрации использования API</li>
</ul>  

<h2>пример использования:</h2>

<code>$ curl https://isalivehost.herokuapp.com/ </code> 

<pre>
{
    "info":"You need to specify /healthz?hostname=&lt;place here the hostname you are interested in&gt;"
}
</pre>

<code>$ curl https://isalivehost.herokuapp.com/healthz?hostname=google.com</code> 
<pre>
{ 
    "status": "up"
}
</pre>

<p>Для <b>semrush.com</b> при отправки GET запроса с heroku возвращает статус 503, соответственно {"status": "down"}. Возможно стоит блокировка запросов с хероку. При запуске программы локально или через другой сервер (не хероку) возвращается {"status": "up"}. Также чтобы это обойти можно использовать PROXY</p>
<p>Можно добавить логирование. Я люблю это делать с помощью <b>loguru</b> и отслеживать в логах номера статусов и исключения.</p>

<h2>Запуск локально</h2>

<p>Установка и активация виртуального окружения</p>

<code> $ virtualenv venv --python=3.9 </code>

<code> $ . venv/bin/activate </code>

<p>Установка необходимых зависимостей</p>

<code> $ pip install -r requirements.txt </code>
<p>Запуск приложения</p>

<code> $ uvicorn api.api:app </code>


<h2>Docker</h2>

<p>Пример, чтобы собрать Docker образ</p>

<code> $ sudo docker build -t jim95022/ishostaliveapp:1.0 .</code>

<p>Чтобы загрузить готовый образ</p>

<code> $ sudo docker pull jim95022/ishostaliveapp:1.0</code>

<p>Чтобы запустить Docker образ</p>

<code> $ sudo docker run -d -p 8000:80 jim95022/ishostaliveapp:1.0</code>

<p>после чего приложение будет доступно по адресу http://localhost:8000/</p>

<hr>
<h1>Задание</h1>


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
