# httpOperation
Http Operations Libraries for Python

## import package example


```python
from httpOperation import HttpOperation
```

## using example
```python
url = "https://petstore.swagger.io/v2/swagger.json"
op = HttpOperation()
print(op.fetch(url=url))


## or using example
url = "https://petstore.swagger.io/v2/swagger.json"
op = HttpOperation(url=url)
print(op.fetch())


## close log 
from environment import Environment
Environment.Shared().online()

##on terminal excute
python lib/test_http.py

#builder with json parsing
op = HttpOperation()
jsonData = op.request(url=url).jsonParse()

op3 = HttpOperation()
responseString = op3.fetch(url=url)
```


## python3 example

```python
from httpOperation3 import HttpOperation3
```

```python
url = "https://petstore.swagger.io/v2/swagger.json"
op = HttpOperation3()
print(op.fetch(url=url))
```


```python
op4 = HttpOperation3(url=url)
print(op4.fetch())

op5 = HttpOperation3()
print(op5.fetch(url=url))

print(jsonData["swagger"])
```