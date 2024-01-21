# Python3 Plugin - Function Path

## <span style="font-family: courier;">callable=[callable name]</span>

* Class.Method
* Function
* Property.fget
* Property.fset

```python
def hello_world() # callable=hello_world

class testmap:

     @property
    def name(self) # callable=testmap.name.fget

    @name.setter
    def name(self, new_name) # callable=testmap.name.fset

    def contains(self, k: str) # callable=testmap.contains
```

## <span style="font-family: courier;">attribute=[attribute name]</span>

* Attribute name

```python
five_seconds = 5   # attribute=five_seconds

class testmap:
    static_name = 'name'    # attribute=testmap.static_name
    def __init__(self):
        self.name = 'name1'    # attribute=testmap.name
```

## <span style="font-family: courier;">instance_required</span>

* Tag for *callable* or *attribute* to indicate the entity is not static. The instance is passed in the $1^{st}$ parameter (i.e. `self`).

```python
class testmap:
    def __init__(self): # callable=testmap.__init__,instance_required
        self.name = 'name1' # attribute=testmap.name,instance_required
```

## <span style="font-family: courier;">setter</span>

* Tag for *attribute* to load a setter for the entity

```python
# attribute=five_seconds,setter
five_seconds = 5

class testmap:
    def __init__(self):
        # attribute=testmap.name,instance_required,setter
        self.name = 'name1' 
```

## <span style="font-family: courier;">getter</span>

* Tag for *attribute* to load a getter for the entity

```python
# attribute=five_seconds,getter
five_seconds = 5

class testmap:
    def __init__(self):
        # attribute=testmap.name,instance_required,getter
        self.name = 'name1' 
```

## <span style="font-family: courier;">varargs</span>

* Tag for *callable* to indicate the callable accepts *args argument

```python
def f(self, value='default', *args) # callable=f,varargs
```

## <span style="font-family: courier;">named_args</span>

* Tag for *callable* to indicate the callable accepts *name only* parameters or **kwargs argument

```python
def f(self, value='default', **named_args) # callable=f,named_args
def g(self, *, named: str) # callable=g,named_args
def h(self, *args, **named_args) # callable=h,named_args,varargs
```
