<h1 align="center">
  <img alt="KenzieHub" title="KenzieHub" src="https://kenzie.com.br/_next/image?url=%2Fimages%2Flogo.png&w=640&q=75" width="100px" />
</h1>

<h1 align="center">
  BiblioteKa - API
</h1>

<p align = "center">
Este é o backend da aplicação BiblioteKa -  Esta API é projetada para simular o backend de uma biblioteca, permitindo a gestão de livros, empréstimos e devoluções. Com esta API, você pode adicionar, visualizar, atualizar e excluir informações sobre os livros disponíveis na biblioteca. Além disso, você pode gerenciar os empréstimos e devoluções de livros, permitindo que seus usuários vejam quais livros estão atualmente emprestados e quando eles devem ser devolvidos.
</p>

## **Insomnia**

<p> Para importar o JSON no Insomnia é só clicar no botão "Run in Insomnia". Depois é só seguir os passos que ele irá importar todos os endpoints em seu insomnia.
</p>

<a href="https://insomnia.rest/run/?label=BiblioteKA&uri=https%3A%2F%2Fgithub.com%2Fnbadilho%2Fm5-grupo32-BibliotecaKA%2Fblob%2Fmain%2FInsomnia.json" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>

<br style="margin-top: 20px;">

A url base da API é https://biblioteka-2bav.onrender.com/api/

<br style="margin-top: 20px;">

## **<h2 align="center" >Endpoints</h2>**

<br style="margin-top: 20px;">

<p align="center">
<a href="#books">books</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

<p align="center">
<a href="#users">users</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

<p align="center">
<a href="#bookloan">bookloan</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>
<p align="center">
<a href="#following">following</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

=========================================================================================================================

## **<h2  align="center" id="users">USERS</h2>**

# **<h4>Rotas que não necessitam de token</h4>**

`POST /users/ - FORMATO DA RESPOSTA - STATUS 201`

**<p>Exemplo do corpo da requisição</p>**

```json
{
  "username": "teste",
  "first_name": "teste",
  "last_name": "teste",
  "birthdate": "1990-01-01",
  "password": 1234,
  "email": "teste@gmail.com"
}
```

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "id": "245707db-79cc-4ca9-a4c1-41a930d06b04",
  "username": "teste",
  "email": "teste@gmail.com",
  "first_name": "teste",
  "last_name": "teste",
  "is_employee": false
}
```

<br style="margin-top: 20px;">

`POST /users/login/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo do corpo da requisição</p>**

```json
{
  "username": "teste",
  "password": 1234
}
```

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzkwMDcxNSwiaWF0IjoxNjgzNjQxNTE1LCJqdGkiOiIyY2E1M2E3NTVhNmM0MzNjYjYwMGI0Y2RmZDRjNWI3ZCIsInVzZXJfaWQiOiIyN2MzZTMwZi0zYzgzLTRiNDUtODc0OC1mNTg5YzQzOGFiN2QifQ.Nt1tmNEz20U7l08G0Nxd8RW0M8_yvKzZ6urq5sMk4-k",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNzI3OTE1LCJpYXQiOjE2ODM2NDE1MTUsImp0aSI6IjEzZTQzNmZmNDIyZjQ2NDI5ZjMyY2M5ZDFhZjJlMDY2IiwidXNlcl9pZCI6IjI3YzNlMzBmLTNjODMtNGI0NS04NzQ4LWY1ODljNDM4YWI3ZCJ9.qKdTt1Nu1p7-RExZ9wEQZTwcXAPHOstSv5oxhtI8BFo"
}
```

<br style="margin-top: 20px;">

# **<h4>Rotas que necessitam de token</h4>**

`PATCH /users/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo do corpo da requisição</p>**

```json
{
  "last_name": "teste atualizado"
}
```

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "id": "245707db-79cc-4ca9-a4c1-41a930d06b04",
  "username": "teste",
  "email": "teste@gmail.com",
  "first_name": "teste",
  "last_name": "teste atualizado",
  "is_employee": false
}
```

<br style="margin-top: 20px;">

`DELETE /users/delete/userID/ - FORMATO DA RESPOSTA - STATUS 204`

**<p>Exemplo de resposta da requisição</p>**

```json

   204 No Content

```

<br style="margin-top: 20px;">

# **<h4>Rotas que necessitam de token do administrador</h4>**

<br style="margin-top: 20px;">

`GET /users/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "count": 7,
  "next": "https://biblioteka-2bav.onrender.com/api/users/?page=2",
  "previous": null,
  "results": [
    {
      "id": "1439cb79-3467-465c-9a58-58e611635dd7",
      "username": "teste2",
      "email": "test@mail.com",
      "first_name": "teste",
      "last_name": "testando",
      "is_employee": false
    },
    {
      "id": "245707db-79cc-4ca9-a4c1-41a930d06b04",
      "username": "teste",
      "email": "teste@gmail.com",
      "first_name": "teste",
      "last_name": "teste",
      "is_employee": false
    },
    {
      "id": "27c3e30f-3c83-4b45-8748-f589c438ab7d",
      "username": "hugao",
      "email": "hugo@gmail.com",
      "first_name": "Hugo",
      "last_name": "Raphael",
      "is_employee": true
    },
    {
      "id": "3b275572-6825-4a43-ad89-f097958d4803",
      "username": "tesas",
      "email": "testsse2@gmail.com",
      "first_name": "teste",
      "last_name": "teste",
      "is_employee": false
    },
    {
      "id": "56dc96db-24d0-4e76-bee9-199c9408a072",
      "username": "teste3",
      "email": "teste3@gmail.com",
      "first_name": "teste",
      "last_name": "teste",
      "is_employee": true
    }
  ]
}
```

<br style="margin-top: 20px;">

`GET /users/userID/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "id": "27c3e30f-3c83-4b45-8748-f589c438ab7d",
  "email": "hugo@gmail.com",
  "first_name": "Hugo",
  "last_name": "Raphael",
  "is_allowed_lending": true,
  "date_block": null
}
```

=========================================================================================================================

<br style="margin-top: 20px;">

## **<h2 align="center" id="books">BOOKS</h2>**

<br style="margin-top: 20px;">

# **<h4>Rotas que não necessitam de token</h4>**

<br style="margin-top: 20px;">

`GET /books/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "count": 6,
  "next": "https://biblioteka-2bav.onrender.com/api/books/?page=2",
  "previous": null,
  "results": [
    {
      "id": "4083cd1f-2da5-4f69-adec-5019dfaf5b75",
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
      "published_date": "1951-07-16",
      "publishing_company": "Little, Brown and Company",
      "language": "English",
      "days_to_borrow": 14,
      "genres": [
        {
          "id": "66675986-b810-4618-a064-3f97e6912fea",
          "name": "Fiction"
        },
        {
          "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
          "name": "Coming of Age"
        }
      ],
      "quantity": 10
    },
    {
      "id": "5d3e06b0-f27e-4745-8cc7-1c293f07ce23",
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
      "published_date": "1951-07-16",
      "publishing_company": "Little, Brown and Company",
      "language": "English",
      "days_to_borrow": 14,
      "genres": [
        {
          "id": "66675986-b810-4618-a064-3f97e6912fea",
          "name": "Fiction"
        },
        {
          "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
          "name": "Coming of Age"
        }
      ],
      "quantity": 10
    },
    {
      "id": "0131d126-18c0-4b67-accd-19bc144d016e",
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
      "published_date": "1951-07-16",
      "publishing_company": "Little, Brown and Company",
      "language": "English",
      "days_to_borrow": 14,
      "genres": [
        {
          "id": "66675986-b810-4618-a064-3f97e6912fea",
          "name": "Fiction"
        },
        {
          "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
          "name": "Coming of Age"
        }
      ],
      "quantity": 10
    },
    {
      "id": "5943a8fe-591b-49b7-be47-9077ba80ca52",
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
      "published_date": "1951-07-16",
      "publishing_company": "Little, Brown and Company",
      "language": "English",
      "days_to_borrow": 4,
      "genres": [
        {
          "id": "66675986-b810-4618-a064-3f97e6912fea",
          "name": "Fiction"
        },
        {
          "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
          "name": "Coming of Age"
        }
      ],
      "quantity": 10
    },
    {
      "id": "8381ed24-b2fd-4a09-978c-b22e6e28d841",
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
      "published_date": "1951-07-16",
      "publishing_company": "Little, Brown and Company",
      "language": "English",
      "days_to_borrow": 3,
      "genres": [
        {
          "id": "66675986-b810-4618-a064-3f97e6912fea",
          "name": "Fiction"
        },
        {
          "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
          "name": "Coming of Age"
        }
      ],
      "quantity": 10
    }
  ]
}
```

<br style="margin-top: 50px;">

`GET /books/bookId/ - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": "4083cd1f-2da5-4f69-adec-5019dfaf5b75",
  "title": "The Catcher in the Rye",
  "author": "J.D. Salinger",
  "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
  "published_date": "1951-07-16",
  "publishing_company": "Little, Brown and Company",
  "language": "English",
  "days_to_borrow": 14,
  "genres": [
    {
      "id": "66675986-b810-4618-a064-3f97e6912fea",
      "name": "Fiction"
    },
    {
      "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
      "name": "Coming of Age"
    }
  ],
  "quantity": 10
}
```

<br style="margin-top: 20px;">

# **<h4>Rotas que necessitam de token do administrador</h4>**

`POST /books/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo de corpo da requisição</p>**

```json
{
  "title": "The Catcher in the Rye",
  "author": "J.D. Salinger",
  "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
  "published_date": "1951-07-16",
  "publishing_company": "Little, Brown and Company",
  "language": "English",
  "quantity": 10,
  "genres": [
    {
      "name": "Fiction"
    },
    {
      "name": "Coming of Age"
    }
  ]
}
```

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "id": "4083cd1f-2da5-4f69-adec-5019dfaf5b75",
  "title": "The Catcher in the Rye",
  "author": "J.D. Salinger",
  "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
  "published_date": "1951-07-16",
  "publishing_company": "Little, Brown and Company",
  "language": "English",
  "days_to_borrow": 14,
  "genres": [
    {
      "id": "66675986-b810-4618-a064-3f97e6912fea",
      "name": "Fiction"
    },
    {
      "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
      "name": "Coming of Age"
    }
  ],
  "quantity": 10
}
```

<br style="margin-top: 20px;">

`DELETE /books/bookID/ - FORMATO DA RESPOSTA - STATUS 204`

**<p>Exemplo de resposta da requisição</p>**

```json

   204 No Content

```

=========================================================================================================================

## **<h2 align="center" id="bookloan">Book loan</h2>**

<br style="margin-top: 20px;">

# **<h4>Rotas que necessitam de token do administrador</h4>**

<br style="margin-top: 20px;">

`POST /bookloan/bookID/ - FORMATO DA RESPOSTA - STATUS 201`

**<p>Exemplo de corpo da requisição</p>**

```json
{
  "user_id": "07476751-d145-4d35-9449-4aea0832fce5"
}
```

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "id": "d6ef4c89-27d7-4bd1-9b7a-fd695d786a5f",
  "book_copy": "0f0a86e7-cfc8-42da-866b-4bd82f97bec8",
  "user": "27c3e30f-3c83-4b45-8748-f589c438ab7d",
  "loan_date": "2023-05-08T21:58:37.887708Z",
  "max_return_date": "2023-05-22",
  "returned_date": null
}
```

<br style="margin-top: 20px;">

`PATCH /bookloan/bookloanID/ - FORMATO DA RESPOSTA - STATUS 201`

**<p>Exemplo de corpo da requisição</p>**

```json
{
  "user_id": "07476751-d145-4d35-9449-4aea0832fce5"
}
```

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "id": "dba6695f-af74-402b-aae6-5d84e2bbd0a3",
  "book_copy": {
    "id": "132eca61-2546-4163-9878-462f258e25df",
    "title_book": "The Catcher in the Rye"
  },
  "user": {
    "id": "07476751-d145-4d35-9449-4aea0832fce5",
    "username": "teste"
  },
  "loan_date": "2023-05-08T22:38:06.300865Z",
  "max_return_date": "2023-05-22T00:00:00Z",
  "returned_date": "2023-05-08"
}
```

<br style="margin-top: 20px;">

`GET /bookloan/bookloanID/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "id": "dba6695f-af74-402b-aae6-5d84e2bbd0a3",
  "book_copy": {
    "id": "132eca61-2546-4163-9878-462f258e25df",
    "title_book": "The Catcher in the Rye"
  },
  "user": {
    "id": "07476751-d145-4d35-9449-4aea0832fce5",
    "username": "teste"
  },
  "loan_date": "2023-05-08T22:38:06.300865Z",
  "max_return_date": "2023-05-22T00:00:00Z",
  "returned_date": "2023-05-08"
}
```

=========================================================================================================================

## **<h2 align="center" id="following">USER FOLLOWING</h2>**

<br style="margin-top: 20px;">

# **<h4>Rotas que necessitam de token</h4>**

`GET /users/following/user/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "57d5292f-9f69-4b0a-b0ac-f71260ec9690",
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
      "published_date": "1951-07-16",
      "publishing_company": "Little, Brown and Company",
      "language": "English",
      "days_to_borrow": 5,
      "genres": [
        {
          "id": "66675986-b810-4618-a064-3f97e6912fea",
          "name": "Fiction"
        },
        {
          "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
          "name": "Coming of Age"
        }
      ],
      "quantity": 10
    },
    {
      "id": "4083cd1f-2da5-4f69-adec-5019dfaf5b75",
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "synopsis": "A teenage boy struggles with the complexities of growing up and the hypocrisy of the adult world.",
      "published_date": "1951-07-16",
      "publishing_company": "Little, Brown and Company",
      "language": "English",
      "days_to_borrow": 14,
      "genres": [
        {
          "id": "66675986-b810-4618-a064-3f97e6912fea",
          "name": "Fiction"
        },
        {
          "id": "2efe3c0e-9742-42c7-9110-2a23676cf5b8",
          "name": "Coming of Age"
        }
      ],
      "quantity": 10
    }
  ]
}
```

`POST users/following/bookId/ - FORMATO DA RESPOSTA - STATUS 201`

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "id": "53856a05-60b6-4f4a-8ee9-a6103436432e",
  "user": {
    "id": "245707db-79cc-4ca9-a4c1-41a930d06b04",
    "username": "teste"
  },
  "book": {
    "id": "4083cd1f-2da5-4f69-adec-5019dfaf5b75",
    "title": "The Catcher in the Rye"
  }
}
```

`DELETE /users/following/delete/bookId/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo de resposta da requisição</p>**

```json

   204 No Content

```

`GET /users/following/bookId/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "5c08c8e2-a86e-4bbf-82c8-df3c4fc61465",
      "user": {
        "id": "245707db-79cc-4ca9-a4c1-41a930d06b04",
        "username": "teste"
      },
      "book": {
        "id": "57d5292f-9f69-4b0a-b0ac-f71260ec9690",
        "title": "The Catcher in the Rye"
      }
    },
    {
      "id": "53856a05-60b6-4f4a-8ee9-a6103436432e",
      "user": {
        "id": "245707db-79cc-4ca9-a4c1-41a930d06b04",
        "username": "teste"
      },
      "book": {
        "id": "4083cd1f-2da5-4f69-adec-5019dfaf5b75",
        "title": "The Catcher in the Rye"
      }
    }
  ]
}
```

# **<h4>Rotas que necessitam de token do administrador</h4>**

`GET users/following/book/bookId/ - FORMATO DA RESPOSTA - STATUS 200`

**<p>Exemplo de resposta da requisição</p>**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "245707db-79cc-4ca9-a4c1-41a930d06b04",
      "username": "teste",
      "email": "teste@gmail.com",
      "first_name": "teste",
      "last_name": "teste",
      "is_employee": false
    }
  ]
}
```

<br style="margin-top: 20px;">

=========================================================================================================================
