# Пояснения к приложению
1\. Сама форма для записи доступна на :

    http://localhost/carshop/register/
    
   Приложение работает следующим оразом:
   - При GET запросе на  ```http://localhost/carshop/register/``` отдается форма для записи на диагностику
   - С этой же страницы отправляется POST запрос с заполненной формой, в теле запроса присутствует JSON следующего вида:
   ```
{
	    "surname": "Фамилия",
	    "name": "Имя",
	    "patronymic" : "Отчество",
	    "auto_mark": "Марка машины",
	    "date_time": "год-месяц-деньTчасы:минуты", # "%Y-%m-%dT%H:%M"
	    "master": "номер мастера" # от 1 до 3
}
``` 
 - Если POST запрос прошел удачно то происходит запись к мастеру на диагностику и возвращается JSON следующего вида:
 ```
{"response": "Success!"}
```
- Если POST запрос произошел неудачно(незаполенны поля формы, указан неверный номер мастера, 
указано неверные время и/или дата, указанная дата и/или время уже в прошлом, дата и/или время 
указаны в неправильном формате), то записи к мастеру не происходит и возвращается следующий json:
```
{
     "response": "warning",
     "message": "Сообщение об ошибке в запросе"
}
```
    

2\. Так как фронтенд приложения тестировался в браузере Chromium(Версия 65.0.3325.181 (Официальная сборка), 
Built on Ubuntu , running on Ubuntu 14.04 (64 бит)), то некоторое элементы фронтенда
(например ``` <input type="datetime-local">```) могут не работать в других браузерах, таких как  Firefox и т.д. 
Так же можно отправлять POST запросы с JSON через postman, для этого расскоментируйте 12 строку в файле 
```car_repair_shop/views.py```.
Формат JSON для POST запроса должен иметь следующий вид:


```
{
	"surname": "Фамилия",
	"name": "Имя",
	"patronymic" : "Отчество",
	"auto_mark": "Марка машины",
	"date_time": "год-месяц-деньTчасы:минуты", # "%Y-%m-%dT%H:%M"
	"master": "номер мастера" # от 1 до 3
}
```    

3\. На странице администратора можно посмотреть записи у любого мастера.Она доступна на:

    http://localhost/admin/
    
4\. Предполагается, что всего работает три мастера. И у каждого мастера очередь записей к нему представлена 
таблицой в базе данных.


# Запуск приложения
1\. Перед запуском установите свою временную зону в настройках django-проекта(```test_task/settings.py``` - строки 122-124)!!!
В текущей конфигурации указанна временная зона для Уфы.

1.1\. Необходимые зависимости, перечисленные в requirements.txt, устанавливаются самим Docker'ом(как указано в Dockerfile)

2\. Для того чтобы запустить приложение и установить все зависимости из requirements.txt 
необходимо запустить команду ```docker-compose up``` из корневой директории проекта(директория в которой находится 
```manage.py```),
 НО! перед этим прочитайте пункт 3.

3\. Перед тем как запускать ```docker-compose up``` измените владельца файлов(из репозитория) и группу к которой он относится, 
для этого:
   - запустите эту команду из корневой директории проекта
   (директория в которой находится manage.py): ```sudo chown -R $USER:$USER .```
   (согласно ```https://docs.docker.com/compose/django/``` раздел "Create a Django project")

4\. После запуска "docker-compose up" необходимо немного подождать, так как у PostgreSQL 
    достаточно долгая инициализация, в течении которой Django будет пытаться (безрезультатно) 
    подлючиться к PostgreSQL. Как только PostgreSQL завершит инициализацию, Django успешно 
    подключится к PostgreSQL, проведет миграции и запустит приложение на локальном 80 порту (localhost:80 или localhost)
    
5\. Для создания и применения миграций из приложения car_repair_shop необходимо запустить две команды:
  
    docker-compose exec web python manage.py makemigrations car_repair_shop
    docker-compose exec web python manage.py migrate

6\. Создайте суперпользователя(администратора) через команду:

    docker-compose exec web python manage.py createsuperuser
    
7\. Тесты запускаются так:

    docker-compose exec web python manage.py createsuperuser