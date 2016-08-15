###### Dev установка 
Установка пакетного менеджера:

(установка nodejs: `sudo apt-get install nodejs`)

(установка npm: `sudo apt-get install npm`)

(установка bower: `sudo npm install -g bower`)
> NOTE: возможна ошибка, связанная с конфликтом между node и nodejs, установите: `sudo apt-get install nodejs-legacy`

Установка виртуальной среды
```
virtualenv ~/envs/lenta
source ~/envs/lenta/bin/activate
```

Настройка приложения (settings.py)
```
sudo -i -u postgres
createdb lenta
```

Изменить настройки подключения DATABASES.

Указать настройки SMTP в секции "Email".

Установка приложения
```
python setup.py bower_install install
lenta migrate
DJANGO_SETTINGS_MODULE=lenta.settings architect partition --module lenta.digest.models
```

Запуск приложения
```
lenta celery worker --queue=normal,high --loglevel=info
lenta celery worker --queue=high --loglevel=info
lenta celery beat --loglevel=info
lenta runserver
```
