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

**Note:** There is already articles and users in the database for testing and viewing purposes.
<br>
<br>
**username:** user
<br>
**password:** user

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

### HomePage
<img width="1728" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/5860e21a-ad46-4942-aeb1-8b0ae22728ca">

<img width="1728" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/cd6ff4a1-d045-4eb6-b81a-a17b5d727db6">

### About
<img width="1728" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/d96fc9f3-c5fc-48ae-954f-8d700c591e97">

### Contact
<img width="1725" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/1d030d10-a980-4171-ad9a-ef4024b70c70">

### Sign-In
<img width="1728" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/c992391e-3e0e-4a59-b66c-5a55a3accbdf">

### Create an Article
<img width="1728" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/4977e572-408f-4b68-bc3e-e0a76da250e2">

### Read an Article
<img width="1728" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/d2774aaa-e0b2-4864-bbba-06329d7cf886">

### Update an Article
<img width="1728" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/4c5b1749-bd1e-41c3-85da-ebf80dcd5a4b">

### Responsiveness
<img width="799" alt="image" src="https://github.com/joaoyp/20231114_Assessment_Joao_Yp/assets/49701898/858f74c0-58c6-43a4-973a-7772869b9e3e">


## Tech Stack

Flask, HTML, CSS

## Links

- [Github](https://www.github.com/joaoyp)
- [LinkedIn](https://www.linkedin.com/in/joao-yp/)
