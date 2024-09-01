# Go API

## Installation

To use the API, add the Go API to your project:

* `go get github.com/MetaFFI/lang-plugin-go/api` - The API
* `go get github.com/MetaFFI/plugin-sdk/compiler/go/IDL` - MetaFFIType

## MetaFFIRuntime Struct

MetaFFIRuntime is a struct that provides a simple and easy FFI framework to connect Go with other languages. Pass to `NewMetaFFIRuntime` the runtime plugin you wish to load into the process (e.g. `python3`, `openjdk`), and call `LoadRuntimePlugin` to load the runtime.

Once the runtime is loaded, use `LoadModule` to load the module and receive and instance of [`MetaFFIModule`](#metaffimodule-class).  

### Methods

#### `NewMetaFFIRuntime(runtimePlugin string) *MetaFFIRuntime`

"Constructor" specifies the requested runtime plugin to use

Parameters:

* `runtimePlugin`: The name of the runtime plugin to use

#### `(this *MetaFFIRuntime) LoadRuntimePlugin() error`

Loads the runtime of the plugin.

#### `(this *MetaFFIRuntime) ReleaseRuntimePlugin() error`

Releases the loaded runtime. After calling this function, and loaded entity **must** not be used.

#### `(this *MetaFFIRuntime) LoadModule(modulePath string) (*MetaFFIModule, error)`

Loads a foreign module from the given `modulePath`. It returns a `MetaFFIModule` object that represents the foreign module.

The modulePath might contain multiple modules (for cases like dependencies). A runtime plugin **specifies** in its documentation what it expects.

Parameters:

* `modulePath` - Path to the module(s) to load

Return:

* Instance of MetaFFIModule representing the foreign module

## MetaFFIModule Struct

The MetaFFIModule struct provides the `Load` method, which loads a *foreign entity* and returns it as a `func`.

The struct should not be created directly, but using the `MetaFFIRuntime.LoadModule` function.

### Methods

#### `(this *MetaFFIModule) Load(entityPath string, paramsMetaFFITypes []MetaFFIType, retvalMetaFFITypes []MetaFFIType) (ff func(...interface{}) ([]interface{}, error), err error)`

#### `(this *MetaFFIModule) LoadWithInfo(entityPath string, paramsMetaFFITypes []MetaFFITypeInfo, retvalMetaFFITypes []MetaFFITypeInfo) (ff func(...interface{}) ([]interface{}, error), err error)`

The Load method in the MetaFFIModule struct loads a foreign entity from the module and returns a `func` that can be used to invoke the foreign entity in another language. If it `func` calls a Method or a Field of an object, the $1^{st}$ parameter is an instance of the object.

The `Load` method receives a [entity path](/README.md#entity-path) telling the runtime plugin the location of the entity inside the module.

The method should also pass a list of [MetaFFI Types](/usage/metaffi_types/), specifying the type of the parameters and return values. `Load` accepts `[]MetaFFIType`, if alias is also required, use  `LoadWithInfo` which accepts `[]MetaFFITypeInfo`.

In case there are no parameters or return values, pass `nil` or empty array.

Parameters:

* `entityPath`: A string that contains the path to the function within the module.
* `paramsMetaFFITypes`: An array of `MetaFFIType` (or `MetaFFITypeInfo`) objects that specify the parameter types for the function.
* `retvalMetaFFITypes`: An array of `MetaFFIType` (or `MetaFFITypeInfo`) objects that specify the return value types for the function.

Returns:

* A `func(...interface{}) ([]interface{}, error)` that accepts the number of parameters defiend in paramsMetaFFITypes and their expected corresponding types.
The function returns the number of expected return values and their corresponding types.

    In case of an error during the call, or an error in the foreign entity, the `func` returns an error.

## MetaFFI Types In Go

| MetaFFI Type | Go |
| :------------ | :------------: |
| <span style="font-family: courier;">metaffi_float64_type</span> | <span style="font-family: courier;">float64</span> |
| <span style="font-family: courier;">metaffi_float32_type</span> | <span style="font-family: courier;">float32</span> |
| <span style="font-family: courier;">metaffi_int8_type</span> | <span style="font-family: courier;">int8</span> |
| <span style="font-family: courier;">metaffi_int16_type</span> | <span style="font-family: courier;">int16</span> |
| <span style="font-family: courier;">metaffi_int32_type</span> | <span style="font-family: courier;">int32</span> |
| <span style="font-family: courier;">metaffi_int64_type</span> | <span style="font-family: courier;">int64</span> |
| <span style="font-family: courier;">metaffi_uint8_type</span> | <span style="font-family: courier;">uint8</span> |
| <span style="font-family: courier;">metaffi_uint16_type</span> | <span style="font-family: courier;">uint16</span> |
| <span style="font-family: courier;">metaffi_uint32_type</span> | <span style="font-family: courier;">uint32</span> |
| <span style="font-family: courier;">metaffi_uint64_type</span> | <span style="font-family: courier;">uint64</span> |
| <span style="font-family: courier;">metaffi_bool_type</span> | <span style="font-family: courier;">bool</span> |
| <span style="font-family: courier;">metaffi_char8_type</span> | <span style="font-family: courier;">uint8</span> |
| <span style="font-family: courier;">metaffi_char16_type</span> | <span style="font-family: courier;">uint16</span> |
| <span style="font-family: courier;">metaffi_char32_type</span> | <span style="font-family: courier;">rune</span> |
| <span style="font-family: courier;">metaffi_string8_type</span> | <span style="font-family: courier;">string</span> |
| <span style="font-family: courier;">metaffi_string16_type</span> | <span style="font-family: courier;">string</span> |
| <span style="font-family: courier;"> metaffi_string32_type</span> | <span style="font-family: courier;">string</span> |
| <span style="font-family: courier;">metaffi_handle_type</span> | <span style="font-family: courier;">MetaFFIHandle</span> |
| <span style="font-family: courier;">metaffi_any_type</span> | <span style="font-family: courier;">interface{}</span> |
| <span style="font-family: courier;">metaffi_null_type</span> | <span style="font-family: courier;">nil</span> |
| <span style="font-family: courier;">metaffi_callable_type</span> | <span style="font-family: courier;">func</span><BR>(not supported yet)</span> |
| <span style="font-family: courier;">metaffi_float64_array_type</span> | <span style="font-family: courier;">[]float64</span> |
| <span style="font-family: courier;">metaffi_float32_array_type</span> | <span style="font-family: courier;">[]float32</span> |
| <span style="font-family: courier;">metaffi_int8_array_type</span> | <span style="font-family: courier;">[]int8</span> |
| <span style="font-family: courier;">metaffi_int16_array_type</span> | <span style="font-family: courier;">[]int16</span> |
| <span style="font-family: courier;">metaffi_int32_array_type</span> | <span style="font-family: courier;">[]int32</span> |
| <span style="font-family: courier;">metaffi_int64_array_type</span> | <span style="font-family: courier;">[]int64</span> |
| <span style="font-family: courier;">metaffi_uint8_array_type</span> | <span style="font-family: courier;">[]uint8</span> |
| <span style="font-family: courier;">metaffi_uint16_array_type</span> | <span style="font-family: courier;">[]uint16</span> |
| <span style="font-family: courier;">metaffi_uint32_array_type</span> | <span style="font-family: courier;">[]uint32</span> |
| <span style="font-family: courier;">metaffi_uint64_array_type</span> | <span style="font-family: courier;">uint64</span> |
| <span style="font-family: courier;">metaffi_bool_array_type</span> | <span style="font-family: courier;">[]bool</span> |
| <span style="font-family: courier;">metaffi_char8_array_type</span> | <span style="font-family: courier;">[]uint8</span> |
| <span style="font-family: courier;">metaffi_string8_array_type</span> | <span style="font-family: courier;">[]string</span> |
| <span style="font-family: courier;">metaffi_string16_array_type</span> | <span style="font-family: courier;">[]string</span> |
| <span style="font-family: courier;">metaffi_string32_array_type</span> | <span style="font-family: courier;">[]string</span> |
| <span style="font-family: courier;">metaffi_any_array_type</span> | <span style="font-family: courier;">[]interface{}</span> |
| <span style="font-family: courier;">metaffi_handle_array_type</span> | <span style="font-family: courier;">[]MetaFFIHandle</span> |
