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

Parameters:

- `module_path` - Path to the module to load

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

#### `load(function_path: str, params_metaffi_types: List[metaffi_type_with_alias], retval_metaffi_types: List[metaffi_type_with_alias]) -> Callable[..., Tuple[Any, ...]]`

The load method for the MetaFFIModule class loads a foreign entity from the module and returns a `Callable` that can be used to invoke the foreign entity from another language.

The `load` method receives a [function path](/usage/function_path/) telling the runtime plugin the location of the entity inside the module.

The method should also pass a list of [MetaFFI Types](/usage/metaffi_types), specifying the type of the parameters and return values. `metaffi_type_with_alias` type is created by `new_metaffi_type_with_alias` function.

In case there are no parameters or return values, pass `None` or empty `list`.

Parameters:

- `function_path`: A string that contains the path to the function within the module.
- `params_metaffi_types`: A list of metaffi_type_with_alias objects that specify the parameter types for the function.
- `retval_metaffi_types`: A list of metaffi_type_with_alias objects that specify the return value types for the function.

Returns:

- A `Callable` that accepts the number of parameters defiend in         params_metaffi_types and their expected corresponding types.
    The function returns the number of expected return values and their corresponding types.

    In case of an error during the call, or an error in the foreign entity, the callable raises an exception containing the error message.

## MetaFFI Types In Python3

| MetaFFI Type | Python3 |
| :------------ | :------------: |
| metaffi_float64_type | float |
| metaffi_float32_type | float |
| metaffi_int8_type | int |
| metaffi_int16_type | int |
| metaffi_int32_type | int |
| metaffi_int64_type | int |
| metaffi_uint8_type | int |
| metaffi_uint16_type | int |
| metaffi_uint32_type | int |
| metaffi_uint64_type | int |
| metaffi_bool_type | bool |
| metaffi_char8_type | bytes |
| metaffi_char16_type | bytes |
| metaffi_char32_type | bytes |
| metaffi_string8_type | str |
| metaffi_string16_type | str |
| metaffi_string32_type | str |
| metaffi_handle_type | metaffi_handle |
| metaffi_array_type | list |
| metaffi_size_type | int |
| metaffi_any_type | Any |
| metaffi_null_type | None |
| metaffi_callable_type | Callable<BR>(returned by `make_callable`) |
| metaffi_float64_array_type | list |
| metaffi_float32_array_type | list |
| metaffi_int8_array_type | list |
| metaffi_int16_array_type | list |
| metaffi_int32_array_type | list |
| metaffi_int64_array_type | list |
| metaffi_uint8_array_type | list |
| metaffi_uint16_array_type | list |
| metaffi_uint32_array_type | list |
| metaffi_uint64_array_type | list |
| metaffi_bool_array_type | list |
| metaffi_char8_array_type | list |
| metaffi_string8_array_type | list |
| metaffi_string16_array_type | list |
| metaffi_string32_array_type | list |
| metaffi_any_array_type | list |
| metaffi_handle_array_type | list |
| metaffi_size_array_type | list |
