---
title: "Python3 API"
permalink: /api-reference/python3/
toc: true
toc_sticky: true
---

## Installation

The API is available via PyPI: `pip install metaffi-api`

## MetaFFIRuntime Class

MetaFFIRuntime provides a simple FFI framework to connect Python with other languages. Pass the runtime plugin name to the constructor (e.g. `"go"`, `"openjdk"`), and call `load_runtime_plugin` to load the runtime.

Once the runtime is loaded, use `load_module` to load a module and receive an instance of [MetaFFIModule](#metaffimodule-class).

### Methods

#### `__init__(runtime_plugin: str)`

Constructor specifying the requested runtime plugin to use.

**Parameters:**
- `runtime_plugin` — The name of the runtime plugin (e.g. `"go"`, `"openjdk"`)

#### `load_runtime_plugin()`

Loads the runtime of the plugin.

#### `release_runtime_plugin()`

Releases the loaded runtime. After calling this function, any loaded entity **must not** be used.

#### `load_module(module_path: str) -> MetaFFIModule`

Loads a foreign module from the given `module_path`. Returns a `MetaFFIModule` object representing the foreign module.

The `module_path` may contain multiple modules separated by semicolons (for cases like dependencies). Each runtime plugin specifies in its documentation what it expects.

**Parameters:**
- `module_path` — Path to the module(s) to load

**Returns:** Instance of `MetaFFIModule`

## MetaFFIModule Class

Provides the `load_entity` method, which loads a foreign entity and returns it as a `Callable`.

The class should not be created directly — use `MetaFFIRuntime.load_module` instead.

### Methods

#### `load_entity(entity_path: str, params_metaffi_types: List[metaffi_type_info], retval_metaffi_types: List[metaffi_type_info]) -> Callable`

Loads a foreign entity from the module and returns a `Callable` that invokes it.

If the entity is an instance method or field, the first parameter is the object instance (see [Entity Path](/entity-path/python3/) for the `instance_required` tag).

**Parameters:**
- `entity_path` — [Entity path](/entity-path/python3/) string locating the entity within the module
- `params_metaffi_types` — List of `metaffi_type_info` objects specifying parameter types, or `None`
- `retval_metaffi_types` — List of `metaffi_type_info` objects specifying return types, or `None`

**Returns:** A `Callable` that accepts the parameters defined in `params_metaffi_types` and returns corresponding values. Raises an exception on error.

## Callback

### `make_metaffi_callable(f: Callable) -> Callable`

Wraps the given callable `f` and returns a cross-language callable. The returned callable can be passed to other languages.

**Parameters:**
- `f` — A Python callable

**Returns:** MetaFFI-enabled `Callable`

## MetaFFI Types in Python3

| MetaFFI Type | Python3 Type |
|:-------------|:-------------|
| `metaffi_float64_type` | `float` |
| `metaffi_float32_type` | `float` |
| `metaffi_int8_type` | `int` |
| `metaffi_int16_type` | `int` |
| `metaffi_int32_type` | `int` |
| `metaffi_int64_type` | `int` |
| `metaffi_uint8_type` | `int` |
| `metaffi_uint16_type` | `int` |
| `metaffi_uint32_type` | `int` |
| `metaffi_uint64_type` | `int` |
| `metaffi_bool_type` | `bool` |
| `metaffi_char8_type` | `bytes` |
| `metaffi_char16_type` | `bytes` |
| `metaffi_char32_type` | `bytes` |
| `metaffi_string8_type` | `str` |
| `metaffi_string16_type` | `str` |
| `metaffi_string32_type` | `str` |
| `metaffi_handle_type` | `metaffi_handle` |
| `metaffi_any_type` | `Any` |
| `metaffi_null_type` | `None` |
| `metaffi_callable_type` | `Callable` (via `make_metaffi_callable`) |
| `metaffi_float64_array_type` | `list` |
| `metaffi_float32_array_type` | `list` |
| `metaffi_int8_array_type` | `list` |
| `metaffi_int16_array_type` | `list` |
| `metaffi_int32_array_type` | `list` |
| `metaffi_int64_array_type` | `list` |
| `metaffi_uint8_array_type` | `list` |
| `metaffi_uint16_array_type` | `list` |
| `metaffi_uint32_array_type` | `list` |
| `metaffi_uint64_array_type` | `list` |
| `metaffi_bool_array_type` | `list` |
| `metaffi_char8_array_type` | `list` |
| `metaffi_string8_array_type` | `list` |
| `metaffi_string16_array_type` | `list` |
| `metaffi_string32_array_type` | `list` |
| `metaffi_any_array_type` | `list` |
| `metaffi_handle_array_type` | `list` |
| `metaffi_size_array_type` | `list` |
