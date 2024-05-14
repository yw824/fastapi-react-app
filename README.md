## FastAPI-React-App : 
- Windows 10
- python 3.9 : venv(env)
- FastAPI / Uvicorn / SqlAlchemy

#### Base Reference 
- https://lsjsj92.tistory.com/650
- https://www.youtube.com/watch?v=0zb2kohYZIM&t=480s
- https://rumbarum.oopy.io/post/examine-fastapi-handling-request-line-by-line-with-comment

#### virtual env 
```
> python -m venv env
> env\Scripts\activate
(env) > pip install fastapi uvicorn sqlalchemy
```

#### RUN Server : 
```
(env) > cd FastAPI 
(env) > uvicorn main:app --reload
```

#### DB : SQLite
```
URL_DATABASE = 'sqlite:///./finance.db'
```

#### Transactions Request Body : json
docs : 127.0.0.1:8000/docs : swagger 내부 지원
```
{
  "amount": 0,
  "category": "Learning",
  "description": "Online Course",
  "is_income": false,
  "date": "2024-05-01"
}
```