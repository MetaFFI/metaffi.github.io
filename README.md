# MetaFFI

Have you ever wanted to use different programming languages together? With MetaFFI, you can do just that. MetaFFI lets you access functions, methods, fields, and even pass callbacks from any language you want.

MetaFFI works similar to loading a C function from a library, but it lets you use that same concept to load entities in any other language.

How awesome is that?

There's no virtual machines of any sort. Each langauges runs in its own runtime, communicating via C.

## Installation

The installation is an all-in-one, cross-platform, Python3 script. Just download and run.

Latest version [`v0.1.1`](https://github.com/MetaFFI/metaffi-core/releases/download/v0.1.1/metaffi_installer.py)

Flags: <br>
**-s** - silent mode, uses default installation.<br>
**--skip-sanity** - skips all tests after installation<br>
**--include-extended-tests** - runs extended tests after installation. Installs several 3rd party libraries for tests (e.g. beautiful soup and others)<br/>
**--patched-go (windows only)** - Assume Go is patched and able to run Go -> OpenJDK tests (https://github.com/golang/go/issues/58542)

## GitHub Projects Links

[MetaFFI on GitHub](https://github.com/MetaFFI/)

[MetaFFI Core](https://github.com/MetaFFI/metaffi-core/)

[Python3 Plugin](https://github.com/MetaFFI/lang-plugin-python3)

[JVM Plugin](https://github.com/MetaFFI/lang-plugin-openjdk)

[Go Plugin](https://github.com/MetaFFI/lang-plugin-go)

## A Simple Example

`log4j` from Python3 ([link](https://github.com/MetaFFI/lang-plugin-python3/blob/main/api/tests/extended/openjdk/log4j/log4j_test.py)):

```python
# load JVM
runtime = metaffi.metaffi_runtime.MetaFFIRuntime('openjdk')

# load log4j
log4j_api_module = runtime.load_module('log4j-api-2.21.1.jar;log4j-core-2.21.1.jar')

# load getLogger() method to get a new logger
getLogger = log4j_api_module.load('class=org.apache.logging.log4j.LogManager,callable=getLogger', 
    [new_metaffi_type_with_alias(metaffi_string8_type)], 
    [new_metaffi_type_with_alias(metaffi_handle_type, 'org.apache.logging.log4j.Logger')])

# load error() method in logger
perror = log4j_api_module.load('class=org.apache.logging.log4j.Logger,callable=error,instance_required',
  [new_metaffi_type_with_alias(MetaFFITypes.metaffi_handle_type),
  new_metaffi_type_with_alias(MetaFFITypes.metaffi_string8_type)],
  None)

# create logger with getLogger()
logger = getLogger('pylogger')[0]
perror(logger, 'Logging error from python!')

runtime.release_runtime_plugin()

```

More examples from [Python3](https://github.com/MetaFFI/lang-plugin-python3/tree/main/api/tests), [Java](https://github.com/MetaFFI/lang-plugin-openjdk/tree/main/api/tests) and [Go](https://github.com/MetaFFI/lang-plugin-go/tree/main/api/tests).

## API Usage Details & Documentation

The API is a user-friendly wrapper to MetaFFI's XLLR (Cross-Language Link Runtime) C-interface.

Detailed usage and documentation of the APIs for each of the plugins:

[Python3](/usage/python3/), [Java Virtual Machine](/usage/jvm/), [Go](/usage/go/)

## Function Path

*Function path* refers to a string that represents the foreign entity within the loaded module.

For instance, in `C`, a module corresponds to a `.so/.dll/.dylib` file, and the function path corresponds to the name of the exported function.

However, in other languages or for other entities besides functions, a single name is insufficient. Hence, the function path consists of a list of key-value pairs or tags separated by commas: `key1=val1,tag1,...,...,tagN,keyN=valN`.

Each plugin requires different keys and tags. Although the keys and tags are similar across plugins, they are not identical.

The following links provide the list of each runtime plugin:

[Python3](/usage/function_path/python3/), [Java Virtual Machine](/usage/function_path/jvm/), [Go](/usage/function_path/go/)

## Compiler

Many runtimes enable the loading of entities from the "executable-code" of different runtimes. For example, the JVM can load entities from <span style="font-family:courier">.jar</span> or <span style="font-family:courier">.class</span> files, whereas the CPython can load entities from <span style="font-family:courier">.py</span> or <span style="font-family:courier">.pyc</span> files. Nevertheless, this functionality is not ubiquitous across all runtimes, and some runtimes necessitate the creation of entrypoints to access the entities (e.g. `Go`).

MetaFFI overcomes this constraint by offering a compiler that can automatically generate entrypoints to the foreign entities.

To compile and generate entrypoints, simply run:<br>
`metaffi -c --idl [path] -g`

<span style="font-family:courier">**-c**</span> - compile<br>
<span style="font-family:courier">**--idl**</span> - path to source code to extract foreign entities signatures<br>
<span style="font-family:courier">**-g**</span> - generate "guest code"

For example, to build guest module for TestRuntime.go:<br>
`metaffi -c --idl TestRuntime.go -g`

The command creates `TestRuntime_MetaFFIGuest.dll/.so/.dylib` (depends on the operating system) which the user can load a MetaFFI module and load the foreign entitity.

## Supported Langauges (for now)

|Language | Supported | Tested|
|:--------|:---------:|:-----:|
| Go | From v1.18 | v1.18 &rarr; v1.21.4 |
| JVM Languages | JNI supported JVM | OpenJDK11 x64<br>Microsoft OpenJDK11 Hotspot JVM
| Python3 | v3.11  | v3.11 |

* Note: Due to a [bug](https://github.com/golang/go/issues/58542) in Go, using Go &rarr; OpenJDK in **Windows**, causes the process to crash. Fix is expected in Go1.23. In the meantime, MetaFFI install provides a temporary patch to fix the issue.

* Lack of support is not due to system limitations, but time. If you like the project, consider to contribute [add a new language support](add-language-plugin) 😊

## Supported Operating Systems (for now)

| Operating System | Supported Versions | Tested |
|:---|:---:|:----:|
| Windows | From 7 | 10, 11 |
| Ubuntu | 22.04 | 22.04 |

* Lack of support is not due to system limitations, but time. If you like the project, consider to contribute and [add a new language support](add-language-plugin) 😊

## Technical Notes

**$METAFFI_HOME** - Environment variable is set to MetaFFI installation directory. In **Windows**, $METAFFI_HOME is added to PATH environment variable.

**$PYTHONHOME** must be set for Python3 support. Installer sets the environment variable.

**$JAVA_HOME** must be set for JVM support. Installer sets the evironment variable.

**$CGO_ENABLED** must be set to 1 and **\$CGO_CFLAGS** must add $METAFFI_HOME as include directory for Go support. Installer sets the environment variables.

## Technical Details (WIP)

[Terminology](/technical/terminology/)

[Background](/technical/background/)

[System Overview](/technical/system-overview/)

[Challenges of Making an XCall](/technical/making-a-call/)

[Cross-Language Link Runtime (XLLR) - Managing Runtimes](/technical/xllr/)

[Runtime Plugin Interface](/technical/runtime-plugin-interface/)

[Compiler Plugin Interface](/technical/compiler-plugin-interface/)

[IDL Plugin Interface](/technical/idl-plugin-interface/)

[Common Data Types (CDT)](/technical/cdt/)

[XCall Calling Convention](/technical/xcall/)

<a name="add-language-plugin"></a>[How to Support Another Language?](/technical/add-langauge-plugin/)
