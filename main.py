from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'

user = User(id='123')
assert user.id == 123
assert isinstance(user.id, int)
# Note that '123' was coerced to an int and its value is 123
assert user.name == 'Jane Doe'
assert user.model_fields_set == {'id'}
assert user.model_dump() == {'id': 123, 'name': 'Jane Doe'}


print(user.model_computed_fields)
