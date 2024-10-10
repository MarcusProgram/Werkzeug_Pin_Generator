# Werkzeug_Pin_Generator
[![Python 3.12](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)<br>
Это пример эксплуатации от LFI до RCE, если на сервере стоит Werkzeug c debug=true
___

## Screenshots
<img src='https://github.com/MarcusProgram/'/>
<img src='https://github.com/MarcusProgram/' widht="200px" height="300px"/>

## Installation

Клонируем гит с помощью `git clone`:
```bash
git clone https://github.com/MarcusProgram/Werkzeug_Pin_Generator.git
```

Потом перейдите в папку с файлом с помощью `cd`:
```bash
cd Werkzeug_Pin_Generator/Exploit
```

Далее, установите все необходимые Python зависимости из файла `requirements.txt`:

```bash
sudo pip install -r requirements.txt
```

А дальше наслаждаетесь скриптом:

```bash
sudo python3 main.py
```

## Up Flask Server
Это сервер для проверки этого эксплоита

Переходим в папку с файлом с помощью `cd`:
```bash
cd Werkzeug_Pin_Generator/Flask
```

Далее, установите все необходимые Python зависимости из файла `requirements.txt`:

```bash
sudo pip install -r requirements.txt
```

А дальше запускаем Python файл и переходим на сервер который нам любезно выдали:

```bash
sudo python3 main.py
```
