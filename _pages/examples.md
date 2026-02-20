---
title: "Examples"
permalink: /examples/
toc: true
toc_sticky: true
---

## Python Calling Java (log4j)

Use Apache log4j logging library from Python:

```python
from metaffi import MetaFFIRuntime, MetaFFITypes
from metaffi.metaffi_types import new_metaffi_type_info

# Load JVM runtime
runtime = MetaFFIRuntime("openjdk")

# Load log4j JARs
module = runtime.load_module("log4j-api-2.21.1.jar;log4j-core-2.21.1.jar")

# Load LogManager.getLogger(String) -> Logger
getLogger = module.load_entity(
    "class=org.apache.logging.log4j.LogManager,callable=getLogger",
    [new_metaffi_type_info(MetaFFITypes.metaffi_string8_type)],
    [new_metaffi_type_info(MetaFFITypes.metaffi_handle_type,
                           "org.apache.logging.log4j.Logger")])

# Load Logger.error(String) — instance method
log_error = module.load_entity(
    "class=org.apache.logging.log4j.Logger,callable=error,instance_required",
    [new_metaffi_type_info(MetaFFITypes.metaffi_handle_type),
     new_metaffi_type_info(MetaFFITypes.metaffi_string8_type)],
    None)

# Use it
logger = getLogger("pylogger")
log_error(logger, "Logging error from Python!")

runtime.release_runtime_plugin()
```

## Java Calling Go (TestMap)

Use a Go struct with methods from Java. First, compile the Go module:

**Go module** (`TestMap.go`):

```go
package main

type TestMap struct {
    m    map[string]interface{}
    Name string
}

func NewTestMap() *TestMap {
    return &TestMap{
        m:    make(map[string]interface{}),
        Name: "TestMap Name",
    }
}

func (this *TestMap) Set(k string, v interface{}) {
    this.m[k] = v
}

func (this *TestMap) Get(k string) interface{} {
    return this.m[k]
}

func (this *TestMap) Contains(k string) bool {
    _, found := this.m[k]
    return found
}
```

Compile: `metaffi -c --idl TestMap.go -g go`

**Java host code:**

```java
import metaffi.*;

// Load Go runtime
MetaFFIRuntime runtime = new MetaFFIRuntime("go");
runtime.loadRuntimePlugin();

// Load the compiled Go module
MetaFFIModule module = runtime.loadModule("TestMap_MetaFFIGuest.dll");

// Load NewTestMap() -> handle
Caller newTestMap = module.load("callable=NewTestMap",
    null,
    new MetaFFITypeInfo[]{ new MetaFFITypeInfo(MetaFFITypes.MetaFFIHandle) });

// Load Set(instance, key, value)
Caller testMapSet = module.load("callable=TestMap.Set,instance_required",
    new MetaFFITypeInfo[]{
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIHandle),
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIString8),
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIAny)
    }, null);

// Load Contains(instance, key) -> bool
Caller testMapContains = module.load("callable=TestMap.Contains,instance_required",
    new MetaFFITypeInfo[]{
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIHandle),
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIString8)
    },
    new MetaFFITypeInfo[]{ new MetaFFITypeInfo(MetaFFITypes.MetaFFIBool) });

// Load Get(instance, key) -> any
Caller testMapGet = module.load("callable=TestMap.Get,instance_required",
    new MetaFFITypeInfo[]{
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIHandle),
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIString8)
    },
    new MetaFFITypeInfo[]{ new MetaFFITypeInfo(MetaFFITypes.MetaFFIAny) });

// Create a TestMap and use it
Object testMap = ((Object[]) newTestMap.call())[0];
testMapSet.call(testMap, "key", Arrays.asList("one", "two", "three"));
Object[] result = (Object[]) testMapGet.call(testMap, "key");
ArrayList<String> list = (ArrayList<String>) result[0];
// list = ["one", "two", "three"]
```

## Go Calling Java

Call a static Java method from Go:

```go
package main

import (
    "fmt"
    metaffi "github.com/MetaFFI/sdk/api/go"
    "github.com/MetaFFI/plugin-sdk/compiler/go/IDL"
)

func main() {
    // Load JVM runtime
    runtime := metaffi.NewMetaFFIRuntime("openjdk")
    runtime.LoadRuntimePlugin()
    defer runtime.ReleaseRuntimePlugin()

    // Load a Java class
    module, _ := runtime.LoadModule("mylib.jar")

    // Load a static method: String MyClass.greet(String)
    greet, _ := module.Load(
        "class=com.example.MyClass,callable=greet",
        []IDL.MetaFFIType{IDL.STRING8},
        []IDL.MetaFFIType{IDL.STRING8})

    // Call it
    result, _ := greet("World")
    fmt.Println(result[0]) // "Hello, World!"
}
```

## Python Calling Go

Call a compiled Go function from Python:

```go
// mathutil.go
package main

func Add(a, b int64) int64 {
    return a + b
}
```

Compile: `metaffi -c --idl mathutil.go -g go`

### Dynamic Loading

```python
from metaffi import MetaFFIRuntime, MetaFFITypes
from metaffi.metaffi_types import new_metaffi_type_info

runtime = MetaFFIRuntime("go")
module = runtime.load_module("mathutil_MetaFFIGuest")

add = module.load_entity(
    "callable=Add",
    [new_metaffi_type_info(MetaFFITypes.metaffi_int64_type),
     new_metaffi_type_info(MetaFFITypes.metaffi_int64_type)],
    [new_metaffi_type_info(MetaFFITypes.metaffi_int64_type)])

result = add(3, 4)
print(result)  # 7

runtime.release_runtime_plugin()
```

### With Generated Stubs

Generate typed Python stubs, then call directly:

```bash
metaffi -c --idl mathutil.go -h python3
```

```python
import mathutil_MetaFFIHost as mathutil

mathutil.bind_module_to_code("mathutil_MetaFFIGuest", "go")

result = mathutil.Add(3, 4)
print(result)  # 7
```

No entity paths. No type arrays. See the [Host Compiler](/host-compiler/) page for the full workflow.

## Java Calling Python

Call a Python function from Java:

```python
# calculator.py
def multiply(a, b):
    return a * b
```

```java
import metaffi.*;

MetaFFIRuntime runtime = new MetaFFIRuntime("python3");
runtime.loadRuntimePlugin();

MetaFFIModule module = runtime.loadModule("calculator");

Caller multiply = module.load("callable=multiply",
    new MetaFFITypeInfo[]{
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIFloat64),
        new MetaFFITypeInfo(MetaFFITypes.MetaFFIFloat64)
    },
    new MetaFFITypeInfo[]{ new MetaFFITypeInfo(MetaFFITypes.MetaFFIFloat64) });

Object[] result = (Object[]) multiply.call(3.0, 4.0);
System.out.println(result[0]); // 12.0
```

## Go Calling Python

Call a Python function from Go:

```python
# greeting.py
def greet(name):
    return f"Hello {name} from Python!"
```

```go
package main

import (
    "fmt"
    metaffi "github.com/MetaFFI/sdk/api/go"
    "github.com/MetaFFI/plugin-sdk/compiler/go/IDL"
)

func main() {
    runtime := metaffi.NewMetaFFIRuntime("python3")
    runtime.LoadRuntimePlugin()
    defer runtime.ReleaseRuntimePlugin()

    module, _ := runtime.LoadModule("greeting")

    greet, _ := module.Load(
        "callable=greet",
        []IDL.MetaFFIType{IDL.STRING8},
        []IDL.MetaFFIType{IDL.STRING8})

    result, _ := greet("Go")
    fmt.Println(result[0]) // "Hello Go from Python!"
}
```

## Passing Callbacks

You can pass a host-language function as a callback to a foreign module. Wrap it with the MetaFFI callable API:

```python
from metaffi import MetaFFIRuntime
from metaffi.metaffi_types import make_metaffi_callable

def my_callback(value):
    print(f"Callback received: {value}")

# Wrap for cross-language use
metaffi_callback = make_metaffi_callable(my_callback)

# Pass metaffi_callback to a foreign function that expects a callable parameter
```

## Working with Objects (`instance_required`)

When a foreign entity is an instance method or field, use the `instance_required` tag in the entity path. The object instance is passed as the first parameter:

```python
# Load constructor — returns a handle to the new object
constructor = module.load_entity(
    "class=com.example.MyClass,callable=<init>",
    None,
    [new_metaffi_type_info(MetaFFITypes.metaffi_handle_type)])

# Load instance method — first param is the object handle
get_name = module.load_entity(
    "class=com.example.MyClass,callable=getName,instance_required",
    [new_metaffi_type_info(MetaFFITypes.metaffi_handle_type)],
    [new_metaffi_type_info(MetaFFITypes.metaffi_string8_type)])

obj = constructor()
name = get_name(obj)
```

See the [Entity Path](/entity-path/) documentation for the full list of keys and tags for each language.
