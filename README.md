# MetaFFI - Multi-Lingual Interoperability System

Have you ever wanted to use different programming languages together? With MetaFFI, you can do just that. MetaFFI lets you access functions, methods, fields, and even pass callbacks from any language you want.

MetaFFI works similar to loading a C function from a library, but it lets you use that same concept to load entities in any other language.

How cool is that?

For large libraries, MetaFFI provides a compiler that generates the code in your programming language, taking all the boring repetitive work of loading the entities.

There's no virtual machines of any sort. Each langauges runs in its own runtime.

## A few simple examples

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

## Installation

The installation is an all-in-one, cross-platform, Python3 script. Just download and run.

Latest version [`v0.1.0`](https://github.com/MetaFFI/metaffi-core/releases/download/v0.1.0/metaffi_installer.py)

Flags: <br>
**/s** - silent mode, uses default installation.<br>
**--skip-sanity** - skips all tests after installation<br>
**--include-extended-tests** - runs extended tests after installation. Installs several 3rd party libraries for tests (e.g. beautiful soup and others)

## Supported Langauges (for now)

|Language | Supported | Tested|
|:--------|:---------:|:-----:|
| Go | From v1.18 | v1.18 &rarr; v1.21.4 |
| JVM Languages | Any JNI supported JVM | OpenJDK11 x64<br>Microsoft OpenJDK11 Hotspot JVM
| Python3 | v3.11  | v3.11

* Note: Due to a [bug](https://github.com/golang/go/issues/58542) in Go, using Go &rarr; OpenJDK in **Windows**, causes the process to crash. Fix is expected in Go1.23. In the meantime, MetaFFI install provides a temporary patch to fix the issue.

* Lack of support is not due to system limitations, but time. If you like the project, consider to contribute 😊

## Supported Operating Systems (for now)

| Operating System | Supported Versions | Tested |
|:---|:---:|:----:|
| Windows | From 7 | 10, 11 |
| Ubuntu | 22.04 | 22.04 |

* Lack of support is not due to system limitations, but time. If you like the project, consider to contribute 😊

## Technical Notes

**$METAFFI_HOME** - Environment variable is set to MetaFFI installation directory. In **Windows**, $METAFFI_HOME is added to PATH environment variable.

**$PYTHONHOME** must be set for Python3 support. Installer sets the environment variable.

**$JAVA_HOME** must be set for JVM support. Installer sets the evironment variable.

**$CGO_ENABLED** must be set to `1` and **\$CGO_CFLAGS** must add $METAFFI_HOME as include directory for Go support. Installer sets the environment variables.

## Technical Details
