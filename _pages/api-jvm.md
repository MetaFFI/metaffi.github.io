---
title: "JVM API"
permalink: /api-reference/jvm/
toc: true
toc_sticky: true
---

## Installation

The file `metaffi.api.jar` is deployed in the MetaFFI installation directory.

## MetaFFIRuntime Class

MetaFFIRuntime provides a simple FFI framework to connect JVM-based languages with other languages. Pass the runtime plugin name to the constructor (e.g. `"go"`, `"python3"`), and call `loadRuntimePlugin` to load the runtime.

Once the runtime is loaded, use `loadModule` to load a module and receive an instance of [MetaFFIModule](#metaffimodule-class).

### Methods

#### `MetaFFIRuntime(String runtimePlugin)`

Constructor specifying the requested runtime plugin to use.

**Parameters:**
- `runtimePlugin` — The name of the runtime plugin (e.g. `"go"`, `"python3"`)

#### `void loadRuntimePlugin()`

Loads the runtime of the plugin.

#### `void releaseRuntimePlugin()`

Releases the loaded runtime. After calling this function, any loaded entity **must not** be used.

#### `MetaFFIModule loadModule(String modulePath)`

Loads a foreign module from the given `modulePath`. Returns a `MetaFFIModule` object representing the foreign module.

The `modulePath` may contain multiple modules separated by semicolons (for cases like dependencies). Each runtime plugin specifies in its documentation what it expects.

**Parameters:**
- `modulePath` — Path to the module(s) to load

**Returns:** Instance of `MetaFFIModule`

#### `static Caller makeMetaffiCallable(Method m)`

Wraps the given Java `Method` and returns a cross-language `Caller`. The returned `Caller` instance can be passed to other languages.

**Parameters:**
- `m` — A Java `Method`

**Returns:** `Caller` instance wrapping the given method

## MetaFFIModule Class

Provides the `load` method, which loads a foreign entity and returns it as a `Caller` object.

The class should not be created directly — use `MetaFFIRuntime.loadModule` instead.

### Methods

#### `MetaFFIModule(MetaFFIRuntime runtime, String modulePath)`

Constructor for the MetaFFIModule class.

**Parameters:**
- `runtime` — A `MetaFFIRuntime` object specifying the runtime plugin
- `modulePath` — Path to the module file

#### `Caller load(String entityPath, MetaFFITypeWithAlias[] parametersTypes, MetaFFITypeWithAlias[] retvalsTypes)`

#### `Caller load(String entityPath, MetaFFIType[] parametersTypes, MetaFFIType[] retvalsTypes)`

Loads a foreign entity from the module and returns a `Caller` that invokes it.

If the entity is an instance method or field, the first parameter is the object instance (see [Entity Path](/entity-path/jvm/) for the `instance_required` tag).

**Parameters:**
- `entityPath` — [Entity path](/entity-path/jvm/) string locating the entity within the module
- `parametersTypes` — Array of `MetaFFITypeWithAlias` (or `MetaFFIType`) specifying parameter types, or `null`
- `retvalsTypes` — Array of `MetaFFITypeWithAlias` (or `MetaFFIType`) specifying return types, or `null`

**Returns:** A `Caller` object with method `Object[] call(Object... parameters)` that accepts the parameters defined in `parametersTypes`. Throws `MetaFFIException` on error.

## MetaFFI Types in JVM

| MetaFFI Type | JVM Type |
|:-------------|:---------|
| `metaffi_float64_type` | `double` |
| `metaffi_float32_type` | `float` |
| `metaffi_int8_type` | `byte` |
| `metaffi_int16_type` | `short` |
| `metaffi_int32_type` | `int` |
| `metaffi_int64_type` | `long` |
| `metaffi_uint8_type` | `byte` |
| `metaffi_uint16_type` | `short` |
| `metaffi_uint32_type` | `int` |
| `metaffi_uint64_type` | `long` |
| `metaffi_bool_type` | `boolean` |
| `metaffi_char8_type` | `byte` |
| `metaffi_char16_type` | `Character` |
| `metaffi_char32_type` | `int` |
| `metaffi_string8_type` | `String` |
| `metaffi_string16_type` | `String` |
| `metaffi_string32_type` | `String` |
| `metaffi_handle_type` | `MetaFFIHandle` |
| `metaffi_any_type` | `Object` |
| `metaffi_null_type` | `null` |
| `metaffi_callable_type` | `Method` (via `makeMetaffiCallable`) |
| `metaffi_float64_array_type` | `double[]` |
| `metaffi_float32_array_type` | `float[]` |
| `metaffi_int8_array_type` | `byte[]` |
| `metaffi_int16_array_type` | `short[]` |
| `metaffi_int32_array_type` | `int[]` |
| `metaffi_int64_array_type` | `long[]` |
| `metaffi_uint8_array_type` | `byte[]` |
| `metaffi_uint16_array_type` | `short[]` |
| `metaffi_uint32_array_type` | `int[]` |
| `metaffi_uint64_array_type` | `long[]` |
| `metaffi_bool_array_type` | `boolean[]` |
| `metaffi_char8_array_type` | `byte[]` |
| `metaffi_string8_array_type` | `String[]` |
| `metaffi_string16_array_type` | `String[]` |
| `metaffi_string32_array_type` | `String[]` |
| `metaffi_any_array_type` | `Object[]` |
| `metaffi_handle_array_type` | `MetaFFIHandle[]` |
