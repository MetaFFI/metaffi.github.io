# Python3 API

## Installation

The API is available via pypi: [`pip install metaffi`](https://pypi.org/project/metaffi-api/)

## MetaFFIRuntime Class

MetaFFIRuntime is a class that provides a simple and easy FFI framework to connect Python with other languages. Pass to the `constructor` the runtime plugin you wish to load into the process (e.g. `go`, `openjdk`), and call `load_runtime_plugin` to load the runtime.

Once the runtime is loaded, use `load_module` to load the module and receive and instance of [`MetaFFIModule`](#metaffimodule-class).  

### Methods

#### `__init__(runtime_plugin: str)`

Constructor specifies the requested runtime plugin to use

Parameters:

- `runtime_plugin`: The name of the runtime plugin to use

#### `load_runtime_plugin()`

Loads the runtime of the plugin.

#### `release_runtime_plugin()`

Releases the loaded runtime. After calling this function, and loaded entity **must** not be used.

#### `load_module(module_path: str)->MetaFFIModule`

Loads a foreign module from a given. It returns a `MetaFFIModule` object that represents the foreign module.

The modulePath might contain multiple modules (for cases like dependencies). A runtime plugin **specifies** in its documentation what it expects.

Parameters:

- `module_path` - Path to the module(s) to load

Return:

- Instance of MetaFFIModule representing the foreign module

## MetaFFIModule Class

The MetaFFIModule class provides the `load` method, which loads a [foreign entity](/technical/terminology/) and returns it as a `Callable`.

The class should not be created directly, but using the `MetaFFIRuntime.load_module` function.

### Methods

#### `__init__(runtime, xllr, module_path)`

The constructor method for the MetaFFIModule class. It initializes the instance with the given attributes.

Parameters:

- `runtime`: A MetaFFIRuntime object that specifies the runtime plugin for the module.
- `xllr`: An XllrWrapper object that provides the interface to [XLLR](/technical/xllr/) (Cross-Language Link Runtime).
- `module_path`: A string that contains the path to the module file.

#### `load_entity(entity_path: str, params_metaffi_types: List[metaffi_type_info], retval_metaffi_types: List[metaffi_type_info]) -> Callable[..., Tuple[Any, ...]]`

The load method for the MetaFFIModule class loads a foreign entity from the module and returns a `Callable` that can be used to invoke the foreign entity from another language. If it `Callable` calls a Method or a Field of an object, the $1^{st}$ parameter is an instance of the object.

The `load` method receives a [entity path](/README.md#entity-path) telling the runtime plugin the location of the entity inside the module.

The method should also pass a list of [MetaFFI Types](#metaffi-types-in-python3), specifying the type of the parameters and return values. `metaffi_type_info` type is created by `new_metaffi_type_info` function.

In case there are no parameters or return values, pass `None` or empty `list`.

Parameters:

- `entity_path`: A string that contains the path to the function within the module.
- `params_metaffi_types`: A list of metaffi_type_info objects that specify the parameter types for the function.
- `retval_metaffi_types`: A list of metaffi_type_info objects that specify the return value types for the function.

Returns:

- A `Callable` that accepts the number of parameters defiend in         params_metaffi_types and their expected corresponding types.
    The function returns the number of expected return values and their corresponding types.

    In case of an error during the call, or an error in the foreign entity, the callable raises an exception containing the error message.

## Callback

### `make_metaffi_callable(f: Callable) -> Callable`

The function wraps the given callable `f`, and returns a cross-language Callable. The returned Callable can be passed to other languages.

Parameter:

- `f`: a Python3 callable

Return:

- MetaFFI-enabled `Callable`

## MetaFFI Types In Python3

| MetaFFI Type | Python3 |
| :------------ | :------------: |
| <span style="font-family: courier;">metaffi_float64_type</span> | <span style="font-family: courier;">float</span> |
| <span style="font-family: courier;">metaffi_float32_type</span> | <span style="font-family: courier;">float</span> |
| <span style="font-family: courier;">metaffi_int8_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_int16_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_int32_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_int64_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_uint8_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_uint16_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_uint32_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_uint64_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_bool_type</span> | <span style="font-family: courier;">bool</span> |
| <span style="font-family: courier;">metaffi_char8_type</span> | <span style="font-family: courier;">bytes</span> |
| <span style="font-family: courier;">metaffi_char16_type</span> | <span style="font-family: courier;">bytes</span> |
| <span style="font-family: courier;">metaffi_char32_type</span> | <span style="font-family: courier;">bytes</span> |
| <span style="font-family: courier;">metaffi_string8_type</span> | <span style="font-family: courier;">str</span> |
| <span style="font-family: courier;">metaffi_string16_type</span> | <span style="font-family: courier;">str</span> |
| <span style="font-family: courier;">metaffi_string32_type</span> | <span style="font-family: courier;">str</span> |
| <span style="font-family: courier;">metaffi_handle_type</span> | <span style="font-family: courier;">metaffi_handle</span> |
| <span style="font-family: courier;">metaffi_any_type</span> | <span style="font-family: courier;">Any</span> |
| <span style="font-family: courier;">metaffi_null_type</span> | <span style="font-family: courier;">None</span> |
| <span style="font-family: courier;">metaffi_callable_type</span> | <span style="font-family: courier;">Callable</span><BR>(returned by `make_callable`) |
| <span style="font-family: courier;">metaffi_float64_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_float32_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_int8_array_type</span> |<span style="font-family: courier;"> list</span> |
| <span style="font-family: courier;">metaffi_int16_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_int32_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_int64_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_uint8_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_uint16_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_uint32_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_uint64_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_bool_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_char8_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_string8_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_string16_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_string32_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_any_array_type</span> | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_handle_array_type | <span style="font-family: courier;">list</span> |
| <span style="font-family: courier;">metaffi_size_array_type</span> | <span style="font-family: courier;">list</span> |
