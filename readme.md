the first step is installatin which you can do quickly using pip 
```sh
pip install pydantic 
```
pydantic has some dependencis which are 
- pydantic-core
- typing-extensions
- annotated-types 
pydantic has an optional dependency which is email varidator which you can install using either of the following command 
```sh
pip install pydantic[email] # -> this dont work for me 
pip install email-varidator 
```
# CONCPET 
## MODELS 
on of the way to define your schema is using models which are simple class that inherit from pydantic.BaseModle
the attribute in the class are the data to be varidated 
example 
```py
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'

assert user.id == 123
assert isinstance(user.id, int)
# Note that '123' was coerced to an int and its value is 123

```

### MODEL METHODS AND PROPERTY 

- model_computed_fields (a dict of computed fields in the model instance )
- 


