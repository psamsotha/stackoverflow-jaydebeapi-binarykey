# Storing MySQL `binary(16)` with JayDeBeApi

## Problem

When trying to store `uuid.uuid().bytes` with `jaydebeapi` in MySQL
as `binary(16)`, the conversion is not done correctly. When using
one parameter

```python
curs.execute('INSERT INTO `user` (userId) VALUES (?)',
             (uuid.uuid4().bytes))
```

there is the following error:

```
Parameter index out of range (2 > number of parameters, which is 1).
```

When using two parameters

```python
curs.execute('INSERT INTO `user` (userId,username) VALUES (?, ?)',
             (uuid.uuid4().bytes, 'some_user'))
```

The data doesn't get stored correctly

```
mysql> select * from user;
+------------------------------------+-----------+
| userId                             | username  |
+------------------------------------+-----------+
| 0x00000000000000000000000000000000 | some_user |
+------------------------------------+-----------+
```


## Setup MySQL

You can start MYySQL with Docker Compose

```
$ docker-compose up
```

## Set up Python environment

```
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```


## Run Python script

```
(.venv) $ python main.py
```