---
title: "Python3 Entity Path"
permalink: /entity-path/python3/
toc: true
toc_sticky: true
---

## `callable=[callable name]`

Specifies a function, method, or property accessor to load.

- `Class.Method`
- `Function`
- `Property.fget`
- `Property.fset`

```python
def hello_world():       # callable=hello_world
    pass

class testmap:

    @property
    def name(self):      # callable=testmap.name.fget
        pass

    @name.setter
    def name(self, new_name):  # callable=testmap.name.fset
        pass

    def contains(self, k: str):  # callable=testmap.contains
        pass
```

## `attribute=[attribute name]`

Specifies a module-level variable or class attribute to load.

```python
five_seconds = 5               # attribute=five_seconds

class testmap:
    static_name = 'name'       # attribute=testmap.static_name

    def __init__(self):
        self.name = 'name1'    # attribute=testmap.name
```

## `instance_required`

Tag for `callable` or `attribute` to indicate the entity is not static. The instance is passed as the first parameter (i.e. `self`).

```python
class testmap:
    def __init__(self):           # callable=testmap.__init__,instance_required
        self.name = 'name1'      # attribute=testmap.name,instance_required
```

## `setter`

Tag for `attribute` to load a setter for the entity.

```python
# attribute=five_seconds,setter
five_seconds = 5

class testmap:
    def __init__(self):
        # attribute=testmap.name,instance_required,setter
        self.name = 'name1'
```

## `getter`

Tag for `attribute` to load a getter for the entity.

```python
# attribute=five_seconds,getter
five_seconds = 5

class testmap:
    def __init__(self):
        # attribute=testmap.name,instance_required,getter
        self.name = 'name1'
```

## `varargs`

Tag for `callable` to indicate the callable accepts `*args`.

```python
def f(self, value='default', *args):  # callable=f,varargs
    pass
```

## `named_args`

Tag for `callable` to indicate the callable accepts keyword-only parameters or `**kwargs`.

```python
def f(self, value='default', **named_args):  # callable=f,named_args
    pass

def g(self, *, named: str):                  # callable=g,named_args
    pass

def h(self, *args, **named_args):            # callable=h,named_args,varargs
    pass
```
