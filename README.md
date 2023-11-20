# 20231114_Assessment_Joao_Yp

## Installation

Install Dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python3 app.py
```

## Features

- CRUD of articles
- Depending on the header it returns an article in JSON or HTML (the page of the article)<br />
  &nbsp; **Note:** See [API Reference](#api-reference) for more information
- Pagination of articles
- RichText Box when creating or updating an article for a more costumized article.
- Sign-In, Sign-Up and Logout
- Create, Update and Delete only for users signed-in

## API Reference

#### Get Article by ID

```http
GET /articles/${id}
```

| Header Key | Header Value       | Description                       |
| :--------- | :----------------- | :-------------------------------- |
| `Accept`   | `application/json` | `Returns an article in JSON`      |
| `Accept`   | `text/html`        | `Returns the page of the article` |

#### Get All Articles

```http
GET /
```

```http
GET /?page=${page_number}
```

| Header Key | Header Value       | Description                                                      |
| :--------- | :----------------- | :--------------------------------------------------------------- |
| `Accept`   | `application/json` | `Returns all articles in JSON`                                   |
| `Accept`   | `text/html`        | `Returns the index page showing all articles (using pagination)` |

#### Create Article

```http
GET /articles/create
```

```http
POST /articles/create
```

| Methods | Description                                       |
| :------ | :------------------------------------------------ |
| `GET`   | `Returns the page with form to create an article` |
| `POST`  | `Used by the form to create an article`           |

#### Update Article by ID

```http
GET /articles/update/${id}
```

```http
POST /articles/update/${id}
```

| Methods | Description                                             |
| :------ | :------------------------------------------------------ |
| `GET`   | `Returns the page with form to update an article by ID` |
| `POST`  | `Used by the form to update an article by ID`           |

#### Delete Article by ID

```http
POST /articles/delete/${id}
```

| Methods | Description                |
| :------ | :------------------------- |
| `POST`  | `Deletes an article by ID` |

## Screenshots

## Tech Stack

Flask, HTML, CSS

## Links

- [Github](https://www.github.com/joaoyp)
- [LinkedIn](https://www.linkedin.com/in/joao-yp/)
