# Java Virtual Machine API

## Installation

The file `metaffi.api.jar` is deployed in the MetaFFI installation directory.

## MetaFFIRuntime Class

MetaFFIRuntime is a class that provides a simple and easy FFI framework to connect JVM-based languages with other languages. Pass to the `constructor` the runtime plugin you wish to load into the process (e.g. `go`, `python3`), and call `loadRuntimePlugin` to load the runtime.

Once the runtime is loaded, use `loadModule` to load the module and receive and instance of [`MetaFFIModule`](#metaffimodule-class).  

### Methods

#### `MetaFFIRuntime(String runtimePlugin)`

Constructor specifies the requested runtime plugin to use

Parameters:

- `runtimePlugin`: The name of the runtime plugin to use

#### `void loadRuntimePlugin()`

Loads the runtime of the plugin.

#### `void releaseRuntimePlugin()`

Releases the loaded runtime. After calling this function, and loaded entity **must** not be used.

#### `MetaFFIModule loadModule(String modulePath)`

Loads a foreign module from a given. It returns a `MetaFFIModule` object that represents the foreign module.

The modulePath might contain multiple modules (for cases like dependencies). A runtime plugin **specifies** in its documentation what it expects.

Parameters:

- `modulePath` - Path to the module(s) to load

Return:

- Instance of MetaFFIModule representing the foreign module

#### `static Caller makeMetaffiCallable(Method m)`

The method wraps the given method `m`, and returns a cross-language Call. The returned `Caller` instance can be passed to other languages.

Parameter:

- `f`: a Python3 callable

Return:

- `Caller` instance wrapping the given method

## MetaFFIModule Class

The MetaFFIModule class provides the `load` method, which loads a [foreign entity](/technical/terminology/) and returns it as a `Caller` object.

The class usually should not be created directly, but using the `MetaFFIRuntime.loadModule` function.

### Methods

#### `MetaFFIModule(MetaFFIRuntime runtime, String modulePath)`

The constructor method for the MetaFFIModule class. It initializes the instance with the given attributes.

Parameters:

- `runtime`: A MetaFFIRuntime object that specifies the runtime plugin for the module.
- `modulePath`: A string that contains the path to the module file.

#### `Caller load(String functionPath, MetaFFITypeWithAlias[] parametersTypes, MetaFFITypeWithAlias[] retvalsTypes)`

#### `Caller load(String functionPath, MetaFFIType[] parametersTypes, MetaFFIType[] retvalsTypes)`

The load method for the MetaFFIModule class loads a foreign entity from the module and returns a `Caller` that can be used to invoke the foreign entity from another language. If the `Caller` calls a Method or a Field of an object, the $1^{st}$ parameter is an instance of the object.

The `load` method receives a [function path](/README.md#function-path) telling the runtime plugin the location of the entity inside the module.

The method should also pass a list of [MetaFFI Types](/usage/metaffi_types/), specifying the type of the parameters and return values.

In case there are no parameters or return values, pass `null` or empty arrays.

Parameters:

- `functionPath`: A string that contains the path to the function within the module.
- `parametersTypes`: MetaFFITypeWithAlias[] array that specify the parameter types for the function.
- `retvalsTypes`: MetaFFITypeWithAlias[] array that specify the return value types for the function.

Returns:

- A `Caller` object, with the `Object[] call(Object... parameters)` method which accepts the number of parameters defiend in parametersTypes and their expected corresponding types.
    The method returns the number of expected return values and their corresponding types.

    In case of an error during the call, or an error in the foreign entity, the `call` method throws `MetaFFIException` containing the error message.

## MetaFFI Types In JVM

| MetaFFI Type | JVM |
| :------------ | :------------: |
| <span style="font-family: courier;">metaffi_float64_type</span> | <span style="font-family: courier;">double</span> |
| <span style="font-family: courier;">metaffi_float32_type</span> | <span style="font-family: courier;">float</span> |
| <span style="font-family: courier;">metaffi_int8_type</span> | <span style="font-family: courier;">byte</span> |
| <span style="font-family: courier;">metaffi_int16_type</span> | <span style="font-family: courier;">short</span> |
| <span style="font-family: courier;">metaffi_int32_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_int64_type</span> | <span style="font-family: courier;">long</span> |
| <span style="font-family: courier;">metaffi_uint8_type</span> | <span style="font-family: courier;">byte</span> |
| <span style="font-family: courier;">metaffi_uint16_type</span> | <span style="font-family: courier;">short</span> |
| <span style="font-family: courier;">metaffi_uint32_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_uint64_type</span> | <span style="font-family: courier;">long</span> |
| <span style="font-family: courier;">metaffi_bool_type</span> | <span style="font-family: courier;">boolean</span> |
| <span style="font-family: courier;">metaffi_char8_type</span> | <span style="font-family: courier;">byte</span> |
| <span style="font-family: courier;">metaffi_char16_type</span> | <span style="font-family: courier;">Character</span> |
| <span style="font-family: courier;">metaffi_char32_type</span> | <span style="font-family: courier;">int</span> |
| <span style="font-family: courier;">metaffi_string8_type</span> | <span style="font-family: courier;">String</span> |
| <span style="font-family: courier;">metaffi_string16_type</span> | <span style="font-family: courier;">String</span> |
| <span style="font-family: courier;">metaffi_string32_type</span> | <span style="font-family: courier;">String</span> |
| <span style="font-family: courier;">metaffi_handle_type</span> | <span style="font-family: courier;">MetaFFIHandle</span> |
| <span style="font-family: courier;">metaffi_any_type</span> | <span style="font-family: courier;">Object</span> |
| <span style="font-family: courier;">metaffi_null_type</span> | <span style="font-family: courier;">null</span> |
| <span style="font-family: courier;">metaffi_callable_type</span> | <span style="font-family: courier;">Method</span><BR>(returned by `MakeCallable`) |
| <span style="font-family: courier;">metaffi_float64_array_type</span> | <span style="font-family: courier;">[]double</span> |
| <span style="font-family: courier;">metaffi_float32_array_type</span> | <span style="font-family: courier;">[]float</span> |
| <span style="font-family: courier;">metaffi_int8_array_type</span> |<span style="font-family: courier;">byte[]</span> |
| <span style="font-family: courier;">metaffi_int16_array_type</span> | <span style="font-family: courier;">short[]</span> |
| <span style="font-family: courier;">metaffi_int32_array_type</span> | <span style="font-family: courier;">int[]</span> |
| <span style="font-family: courier;">metaffi_int64_array_type</span> | <span style="font-family: courier;">long[]</span> |
| <span style="font-family: courier;">metaffi_uint8_array_type</span> | <span style="font-family: courier;">byte[]</span> |
| <span style="font-family: courier;">metaffi_uint16_array_type</span> | <span style="font-family: courier;">short[]</span> |
| <span style="font-family: courier;">metaffi_uint32_array_type</span> | <span style="font-family: courier;">int[]</span> |
| <span style="font-family: courier;">metaffi_uint64_array_type</span> | <span style="font-family: courier;">long[]</span> |
| <span style="font-family: courier;">metaffi_bool_array_type</span> | <span style="font-family: courier;">boolean[]</span> |
| <span style="font-family: courier;">metaffi_char8_array_type</span> | <span style="font-family: courier;">byte[]</span> |
| <span style="font-family: courier;">metaffi_string8_array_type</span> | <span style="font-family: courier;">String[]</span> |
| <span style="font-family: courier;">metaffi_string16_array_type</span> | <span style="font-family: courier;">String[]</span> |
| <span style="font-family: courier;">metaffi_string32_array_type</span> | <span style="font-family: courier;">String[]</span> |
| <span style="font-family: courier;">metaffi_any_array_type</span> | <span style="font-family: courier;">Object[]</span> |
| <span style="font-family: courier;">metaffi_handle_array_type | <span style="font-family: courier;">MetaFFIHandle[]</span> |
