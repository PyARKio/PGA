<!DOCTYPE html>
<html>
<head>
    <title>Hello world</title>
</head>
<body>
<p>
   Список пользователей
</p><ul>
    %for user in users:
    <li>Имя:{{user['name']}} Возраст:{{user['age']}}</li>
    %end
</ul>
<form action="/submit" method="POST">
   Добавить нового пользователя<br>
    <input type="text" name="name" size=40 value=""><br>
    <input type="text" name="age" size=40 value=""><br>
    <input type="submit" value="submit">

</form>

</body>
</html>