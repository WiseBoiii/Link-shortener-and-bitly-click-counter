# Обрезка ссылок с помощью Битли

**ClickCounter** может превращать Ваши длинные ссылки в короткие и удобные [***bitly***](https://bitly.com/) ссылки, а также по этим же [***bitly***](https://bitly.com/) ссылкам выводить кол-во кликов по ним.

### Как установить

С установкой все просто. Вам достаточно склонировать себе репозиторий с кодом и можно начинать работу, однако перед этим стоит убедиться, что:

+ Python 3.9 должен быть уже установлен. 
+ Установлен ```requirements.txt```:
	Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
	```
	pip install -r requirements.txt
	```
	
+ У вас есть ссылка, с которой Вы будете работать. О токене для [***bitly***](https://bitly.com/) не беспокойтесь, он уже предоставлен для Вас.
+ Вы создали файл ```.env``` в папке репозитория со своим токеном [***bitly***](https://bitly.com/), вот пример заполнения файла ```.env``` :
![alt text](https://github.com/WiseBoiii/Link-shortener-and-bitly-click-counter/blob/main/pictures/envsample.png)

### Нужные вам команды
 ```cd C:\(Path to repository)```
 ```

**! Важно !**
Перед установкой ```requirements.txt``` обязательно используйте (virtualvenv/venv) для изоляции проекта и корректной работы кода
Вот пример запуска и работы скрипта:

![alt text](https://github.com/WiseBoiii/Link-shortener-and-bitly-click-counter/blob/main/pictures/Code.png)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
