# MetaFFI

MetaFFI stands for Multilingual Indirect Interoperability System. It’s a clever solution to a common problem: how do we make different programming languages play nicely together? Each language has its strengths, and sometimes we need to harness those strengths in harmony. But—here comes the challenge—how do we get these languages to talk to each other seamlessly?

MetaFFI employs a similar concept to loading libraries in C/C++, but it provides a layer that doesn't restrict to a specific runtime or binary, but any runtime. Once a module is loaded you can load entities from that module, weather it is a function, class, field and more. MetaFFI also allows you to pass callback functions of one language to other languages.

How awesome is that?

There is no virtual machine envolved, and each langauges runs in its own original runtime. The system leverages existing Foregin Function Interface (FFI) and embedding mechanisms to link the runtimes together.


## Installation


Installer is available at:

[`v0.3.0 - Windows`](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0.exe)
[`v0.3.0 - Ubuntu`](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0)

**-s**: To install in silent mode with default installation directory.<br>

To uninstall, execute _uninstall_ executable in the installation directory.

Installers tested on: Windows 11, Windows Server 2022, Ubuntu 22.04

Windows CMD: `curl -LO https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0.exe && metaffi-installer-0.3.0.exe -s`

Windows PowerShell: `Invoke-WebRequest -Uri https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0.exe -OutFile metaffi-installer.exe; Start-Process .\metaffi-installer.exe -ArgumentList '-s' -Wait`

Ubuntu bash: `wget https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0 && chmod +x metaffi-installer-0.3.0 && ./metaffi-installer-0.3.0 -s`


### Plugin installers (Python3 installers):
* Python 3 - [Windows](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311.exe), [Ubuntu](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311)
	* PIP package is available at `pip3 install metaffi-api`
	* Tested with Python 3.11
    * Should work with Python >=3.11, but not tested with installer
    * Should work with Python <3.10, but not tested
* Go - [Windows](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311.exe), [Ubuntu](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311)
  * Currently, supports Go 1.23.1 - will be support any go version in near future
* OpenJDK - [Windows](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk.exe), [Ubuntu](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk)
	* JAR ships with the installer
    * Tested with OpenJDK 21
    * Tested with OpenJDK 11 without testing installer

Windows CMD: `curl -LO https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311.exe && metaffi-plugin-installer-0.3.0-python311.exe && curl -LO https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk.exe && metaffi-plugin-installer-0.3.0-openjdk.exe`

Windows PowerShell: `Invoke-WebRequest https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311.exe -OutFile python311.exe; Start-Process .\python311.exe -Wait; Invoke-WebRequest https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk.exe -OutFile openjdk.exe; Start-Process .\openjdk.exe -Wait`

Ubuntu bash: `wget https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311 -O python311 && chmod +x python311 && ./python311 && wget https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk -O openjdk && chmod +x openjdk && ./openjdk`

### What does the MetaFFI installer do?
#### Windows
* Checks for prerequisites for current programming languages support
	* Installer offers to install missing dependencies if somehthing is missing (automatic in silent mode)
* Copies the MetaFFI files to installation directory (default is `%USERPROFILE%\metaffi`)
* Add installation directory to PATH environment variables
* Adds `METAFFI_HOME` environment variable pointing at the installation directory

#### Linux
* Checks for prerequisites for current programming languages support
	* Installer offers to install missing dependencies if somehthing is missing (automatic in silent mode)
* Copies the MetaFFI files to installation directory (default is `/usr/local/metaffi`)
* Adds `METAFFI_HOME` environment variable to `~/.profile` pointing at the installation directory 

## Pre-Installed Docker Container
Ubuntu 22.04: `docker pull tscs/metaffi-u2204:0.3.0`
Windows server core 2022: `docker pull tscs/metaffi-win-core2022:0.3.0`

## Distribute Binaries
You can distribute MetaFFI binaries with your application (under the license terms). To use MetaFFI on the target machine, you can either install MetaFFI using the installer, or place the MetaFFI directory (without the executable) within your application directory.

Make sure to set `METAFFI_HOME` environment variable. You can set it in your application before your code uses MetaFFI. On windows, also add to `PATH` environment variable.

## (Currently) Supported Programming Langauges

|Language |     Supported     |              Fully Tested With Installer               |
|:--------|:-----------------:|:------------------------------------------------------:|
| Go |   From v1.22.7    |                   v1.18 &rarr; v1.23                   |
| JVM Languages | JNI supported JVM | OpenJDK11/21 x64<br>Microsoft OpenJDK11/21 Hotspot JVM 
| Python3 |       v3.x        |                         v3.11                          |

* Note: Due to a [bug](https://github.com/golang/go/issues/58542) in Go, using Go &rarr; OpenJDK in **Windows**, causes the process to crash. Fix is expected in Go1.23. In the meantime, MetaFFI install provides a temporary patch to fix the issue.

* Lack of support is not due to system limitations, but time. If you like the project, consider to contribute [add a new language support](add-language-plugin) 😊

## (Currently) Supported Operating Systems

| Operating System | Supported Versions | Tested with installer |
|:---|:------------------:|:---------------------:|
| Windows |         >7         |          11           |
| Ubuntu |       >20.04       |         22.04         |

* Lack of support is not due to system limitations, but time. If you like the project, consider to contribute and [add a new language support](add-language-plugin) 😊

## Build From Source
MetaFFI uses `CMake` build system and `vcpkg` for dependency management.
The build system is cross-platform and should work on any platform supported by CMake.

Author uses CLion IDE for the core development, but you can use any IDE that supports CMake.

1. Install CMake and VCPKG
2. Pull https://github.com/MetaFFI/metaffi-root
3. Run the CMake configuration and build
4. CMake script will pull the required dependencies

The GitHub project contains:
* MetaFFI Core
* Python3 Plugin
* JVM Plugin
* Go Plugin

## MetaFFI Paper
The paper ([link](https://arxiv.org/abs/2408.14175)) discusses the research and internals of MetaFFI. Sections for academic audiance or technical audiance are explicitly marked, as explained in the end of the introduction section.

## Documentation

The following provide documentation and explaination about the following MetaFFI APIs:
* GO [API](usage/go/) documentation and [Entity Path](usage/entity_path/go/) documentation
* JVM [API](usage/jvm/) documentation and [Entity Path](usage/entity_path/jvm/) documentation
* Python3 [API](usage/python3/) documentation and [Entity Path](usage/entity_path/python3/) documentation

## Two Usage Examples

`log4j` from Python3 ([link](https://github.com/MetaFFI/lang-plugin-python3/blob/main/api/tests/extended/openjdk/log4j/log4j_test.py)):

```python
# load JVM
runtime = metaffi.metaffi_runtime.MetaFFIRuntime('openjdk')

# load log4j
log4j_api_module = runtime.load_module('log4j-api-2.21.1.jar;log4j-core-2.21.1.jar')

# load getLogger() method to get a new logger
getLogger = log4j_api_module.load_entity('class=org.apache.logging.log4j.LogManager,callable=getLogger', 
		[new_metaffi_type_info(metaffi_string8_type)], 
		[new_metaffi_type_info(metaffi_handle_type, 'org.apache.logging.log4j.Logger')])

# load error() method in logger
perror = log4j_api_module.load_entity('class=org.apache.logging.log4j.Logger,callable=error,instance_required',
	[new_metaffi_type_info(MetaFFITypes.metaffi_handle_type),
	new_metaffi_type_info(MetaFFITypes.metaffi_string8_type)],
	None)

# create logger with getLogger()
logger = getLogger('pylogger')
perror(logger, 'Logging error from python!')

runtime.release_runtime_plugin()
```

More examples from [Python3](https://github.com/MetaFFI/lang-plugin-python3/tree/v0.2.0/api/tests), [Java](https://github.com/MetaFFI/lang-plugin-openjdk/tree/v0.2.0/api/tests) and [Go](https://github.com/MetaFFI/lang-plugin-go/tree/v0.2.0/api/tests).


### Example using a compiler
Some programming languages, like Go, need some help from MetaFFI to build a module available to other programming languages. For that, MetaFFI also provides a compiler to build a MetaFFI enabled module.

For example, assume <span style="font-family:courier">TestMap.go</span>:
```go
func NewTestMap() *TestMap{
	return &TestMap{ 
		m: make(map[string]interface{}),
		Name: "TestMap Name",
	}
}

func (this *TestMap) Set(k string, v interface{}){
	this.m[k] = v
}

func (this *TestMap) Get(k string) interface{}{
	v := this.m[k]
	return v
}

func (this *TestMap) Contains(k string) bool{
	_, found := this.m[k]
	return found
}
```

To use it from other languages using MetaFFI, execute the MetaFFI compiler:

`metaffi -c --idl TestMap.go -g`

This creates a dynamic library for TestMap (i.e. `.so` or `.dll`).
To use it, simply load the dynamic library using MetaFFI. Here's an example in Java using JVM MetaFFI API:
```java

// Load Go runtime
MetaFFIRuntime runtime = new MetaFFIRuntime("go");
runtime.loadRuntimePlugin();

// Load the compiled module (in this case, .dll in windows)
MetaFFIModule module = runtime.loadModule("TestMap_MetaFFIGuest.dll");

// Load a function that creates an instance of TestMap
metaffi.Caller newTestMap = module.load("callable=NewTestMap",
		null,
		new MetaFFITypeInfo[]{
			// returns MetaFFI Handle (i.e. handle to the object)
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIHandle)
		});

// Load Set() method
metaffi.Caller testMapSet = module.load("callable=TestMap.Set,instance_required",
		new MetaFFITypeInfo[]{
			// 1st parameter is an instance of the object
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIHandle),
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIString8), // key
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIAny) // // value
		},
		null); // no return values

// Load Contains() method
metaffi.Caller testMapContains = module.load("callable=TestMap.Contains,instance_required",
		new MetaFFITypeInfo[]{ 
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIHandle),
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIString8) // key
		},
		new MetaFFITypeInfo[]{ 
			// boolean return value
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIBool)
		});

// Load Get() method
metaffi.Caller testMapGet = module.load("callable=TestMap.Get,instance_required",
		new MetaFFITypeInfo[]{
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIHandle),
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIString8) // key
		},
		new MetaFFITypeInfo[]{
			new MetaFFITypeInfo(MetaFFITypes.MetaFFIAny) // returned value
		});

// Create new TestMap
// call() method in the API returns Object[], as other languages
// can return multiple return values. We will update the API for a more convenient usage.
var testMap = ((Object[])newTestMap.call())[0];

// set into the map an array of strings:
testMapSet.call(testMap, "key", new ArrayList<>(Arrays.asList("one", "two", "three")));

// get the array list from the map:
var arr = testMapGet.call(testMap, "key");
ArrayList<String> list = (ArrayList<String>)arr[0];
```

## Finding a foreign entity - Entity Path

*Entity path* refers to a string that represents the foreign entity within the loaded module.

For instance, in `C`, a module corresponds to a `.so/.dll` file, and the function path corresponds to the name of the exported function.

However, in other languages or for other entities besides functions, a single name is insufficient. Hence, the function path consists of a list of key-value pairs or tags separated by commas: `key1=val1,tag1,...,...,tagN,keyN=valN`.

Each plugin requires different keys and tags. Although the keys and tags are similar across plugins, they are not identical.

The following links provide the list of each runtime plugin:

[Python3](/usage/entity_path/python3/), [Java Virtual Machine](/usage/entity_path/jvm/), [Go](/usage/entity_path/go/)


## Bridging Language Boundaries - MetaFFI *XCall* and Capabilities-based calling convension
The XCall is the mechanism MetaFFI uses to facilitate cross-language calls. MetaFFI's agnostic approach ensures that each language remains unaware of the others, allowing for independent plugin development.

XCall is a runtime-independent calling convention that uses Common Data Types (inspired by Microsoft's Variant and GTK gObject) to enable languages to call and use entities in other languages, even if they lack certain features. While the generic calling convention supports a wide range of cross-language calls, it can affect the performance. </br>Therefore, XCall determines the calling convention used at runtime, based on the required capabilities. This allows MetaFFI to use the full-featured calling convention when necessary, a subset of the capabilities to improve performance, or revert completely to a direct function call when possible (like x64 calling convension), resulting in efficient cross-language interactions.

For more details, please refer to the MetaFFI paper.

Note: The current version of MetaFFI always chooses the generic calling convention due to the differences between the initial languages implemented.

## Report a bug

Found a bug? You can report it [here](https://github.com/MetaFFI/metaffi-root/issues/new).


## GitHub Projects

The [MetaFFI Project](https://github.com/MetaFFI/) on GitHub.com contains several repositories:
* [MetaFFI Root](https://github.com/MetaFFI/metaffi-root) contains the SCons build system root (SConstruct), VSCode workspace file and the dev containers `devcontainer.json` files. To build from source, clone this.
* [MetaFFI Core](https://github.com/MetaFFI/metaffi-core/) contains MetaFFI CLI tool, XLLR (Cross-Language Link Runtime), implementation of XCall (cross-call) and CDTs (Common Data Types)
* [Python3 Plugin](https://github.com/MetaFFI/lang-plugin-python3) implements MetaFFI support for Python3 using *CTypes* and *CPython API*
* [JVM Plugin](https://github.com/MetaFFI/lang-plugin-openjdk) implements support for OpenJDK using *JNI*
* [Go Plugin](https://github.com/MetaFFI/lang-plugin-go) implements support for Go using *CGo*
* [Installer](https://github.com/MetaFFI/metaffi-installer) implements the MetaFFI Python installer
* [Containers](https://github.com/MetaFFI/containers) contain the Dockerfiles for the pre-installed containers
* [metaffi.github.io](https://github.com/MetaFFI/metaffi.github.io) contains this GitHub pages website


## Environment variable

**METAFFI_HOME** environment variable is set to MetaFFI installation directory. On Windows, also set METAFFI_HOME to the PATH environment variable.

