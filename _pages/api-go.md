---
title: "Go API"
permalink: /api-reference/go/
toc: true
toc_sticky: true
---

## Installation

Add the Go API to your project:

```bash
go get github.com/MetaFFI/sdk/api/go
go get github.com/MetaFFI/plugin-sdk/compiler/go/IDL
```

## MetaFFIRuntime Struct

MetaFFIRuntime provides a simple FFI framework to connect Go with other languages. Pass the runtime plugin name to `NewMetaFFIRuntime` (e.g. `"python3"`, `"openjdk"`), and call `LoadRuntimePlugin` to load the runtime.

Once the runtime is loaded, use `LoadModule` to load a module and receive an instance of [MetaFFIModule](#metaffimodule-struct).

### Methods

#### `NewMetaFFIRuntime(runtimePlugin string) *MetaFFIRuntime`

Constructor specifying the requested runtime plugin to use.

**Parameters:**
- `runtimePlugin` — The name of the runtime plugin (e.g. `"python3"`, `"openjdk"`)

#### `(this *MetaFFIRuntime) LoadRuntimePlugin() error`

Loads the runtime of the plugin.

#### `(this *MetaFFIRuntime) ReleaseRuntimePlugin() error`

Releases the loaded runtime. After calling this function, any loaded entity **must not** be used.

#### `(this *MetaFFIRuntime) LoadModule(modulePath string) (*MetaFFIModule, error)`

Loads a foreign module from the given `modulePath`. Returns a `MetaFFIModule` object representing the foreign module.

The `modulePath` may contain multiple modules separated by semicolons (for cases like dependencies). Each runtime plugin specifies in its documentation what it expects.

**Parameters:**
- `modulePath` — Path to the module(s) to load

**Returns:** Instance of `*MetaFFIModule`

## MetaFFIModule Struct

Provides the `Load` method, which loads a foreign entity and returns it as a `func`.

The struct should not be created directly — use `MetaFFIRuntime.LoadModule` instead.

### Methods

#### `(this *MetaFFIModule) Load(entityPath string, paramsMetaFFITypes []MetaFFIType, retvalMetaFFITypes []MetaFFIType) (func(...interface{}) ([]interface{}, error), error)`

#### `(this *MetaFFIModule) LoadWithInfo(entityPath string, paramsMetaFFITypes []MetaFFITypeInfo, retvalMetaFFITypes []MetaFFITypeInfo) (func(...interface{}) ([]interface{}, error), error)`

Loads a foreign entity from the module and returns a `func` that invokes it.

If the entity is an instance method or field, the first parameter is the object instance (see [Entity Path](/entity-path/go/) for the `instance_required` tag).

`Load` accepts `[]MetaFFIType`. If alias is also required, use `LoadWithInfo` which accepts `[]MetaFFITypeInfo`.

**Parameters:**
- `entityPath` — [Entity path](/entity-path/go/) string locating the entity within the module
- `paramsMetaFFITypes` — Array of `MetaFFIType` (or `MetaFFITypeInfo`) specifying parameter types, or `nil`
- `retvalMetaFFITypes` — Array of `MetaFFIType` (or `MetaFFITypeInfo`) specifying return types, or `nil`

**Returns:** A `func(...interface{}) ([]interface{}, error)` that accepts the parameters defined in `paramsMetaFFITypes`. Returns an error on failure.

## MetaFFI Types in Go

| MetaFFI Type | Go Type |
|:-------------|:--------|
| `metaffi_float64_type` | `float64` |
| `metaffi_float32_type` | `float32` |
| `metaffi_int8_type` | `int8` |
| `metaffi_int16_type` | `int16` |
| `metaffi_int32_type` | `int32` |
| `metaffi_int64_type` | `int64` |
| `metaffi_uint8_type` | `uint8` |
| `metaffi_uint16_type` | `uint16` |
| `metaffi_uint32_type` | `uint32` |
| `metaffi_uint64_type` | `uint64` |
| `metaffi_bool_type` | `bool` |
| `metaffi_char8_type` | `uint8` |
| `metaffi_char16_type` | `uint16` |
| `metaffi_char32_type` | `rune` |
| `metaffi_string8_type` | `string` |
| `metaffi_string16_type` | `string` |
| `metaffi_string32_type` | `string` |
| `metaffi_handle_type` | `MetaFFIHandle` |
| `metaffi_any_type` | `interface{}` |
| `metaffi_null_type` | `nil` |
| `metaffi_callable_type` | `func` (not supported yet) |
| `metaffi_float64_array_type` | `[]float64` |
| `metaffi_float32_array_type` | `[]float32` |
| `metaffi_int8_array_type` | `[]int8` |
| `metaffi_int16_array_type` | `[]int16` |
| `metaffi_int32_array_type` | `[]int32` |
| `metaffi_int64_array_type` | `[]int64` |
| `metaffi_uint8_array_type` | `[]uint8` |
| `metaffi_uint16_array_type` | `[]uint16` |
| `metaffi_uint32_array_type` | `[]uint32` |
| `metaffi_uint64_array_type` | `[]uint64` |
| `metaffi_bool_array_type` | `[]bool` |
| `metaffi_char8_array_type` | `[]uint8` |
| `metaffi_string8_array_type` | `[]string` |
| `metaffi_string16_array_type` | `[]string` |
| `metaffi_string32_array_type` | `[]string` |
| `metaffi_any_array_type` | `[]interface{}` |
| `metaffi_handle_array_type` | `[]MetaFFIHandle` |
