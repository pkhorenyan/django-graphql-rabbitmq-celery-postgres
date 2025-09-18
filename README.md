Бэкенд для работы с приложением React, которое позволяет  пользователю зарегистрироваться и загрузить файл на сервер для обработки. После асинхронной обработки (подсчет количества строк) пользователь сможет посмотреть информацию о своем файле.

Приложение React общается с бэкендом по GraphQL.

## Технологии

Фреймворк: Django<br>
Файловое хранилище: локально<br>
Реляционная БД: PostgreSQL<br>
Кэширование: Redis <br>
Регистрация пользователей: Email<br>
Авторизация пользователей: Токены(JWT)<br>
Брокер сообщений и очередь: RabbitMQ/Redis+Celery

## Запуск

```bash
docker compose up --build
```
Заглушка:
http://localhost:8000/<br>
RabbitMQ: http://localhost:15672/<br>

## Тестирование

Эндпоинт для GraphQL запросов:<br>
http://localhost:8000/graphql/

### Регистрация пользователя

```
mutation {
  register(username: "testuser", password: "password123", email: "test@example.com") {
    success
  }
}
```

### Получение JWT токена

```
mutation {
  tokenAuth(username: "testuser", password: "password123") {
    token
    refreshToken
    refreshExpiresIn
  }
}
```

### Логин
В запросе надо также указать JWT токен

```
query {
  me {
    id
    username
    email
  }
}
```

### Загрузка файла
В запросе надо также указать JWT токен

<b>Body (form-data):</b>
* `operations`
```
{
  "query": "mutation UploadFile($file: Upload!, $name: String!) { uploadFile(file: $file, name: $name) { file { id name lineCount uploadedAt} } }",
  "variables": {
    "file": null,
    "name": "file_01.txt"
  }
}
```
* `map`
```
{ "0": ["variables.file"] }
```
* `0`<br>
Выберите файл (например, file_01.txt) из вашего компьютера

Файл загружается локально в папку `media`


### Просмотр загруженных файлов
В запросе надо также указать JWT токен и userid

```
query {
  userFiles(userId: "1") {
    id
    name
    user {
      id
      username
    }
    lineCount
    uploadedAt
  }
}
```

### Логаут
В запросе надо указать refreshToken

```
mutation {
  revokeToken(refreshToken: "632d1578a83662ceb0a5d2b4a7e7d773214ced9c") {
    revoked
  }
}
```
