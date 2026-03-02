---
title: "Getting Started"
permalink: /getting-started/
toc: true
toc_sticky: true
---

## Prerequisites

- **Windows 11** or **Ubuntu 24.04** (other versions may work but are not tested with the installer)
- At least one supported language runtime installed:
  - **Go** v1.22+
  - **OpenJDK** 11, 21, or 22
  - **Python** 3.11+

## Install MetaFFI Core

Download and run the installer for your platform:

- [**Windows** (v0.3.1)](https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-installer-0.3.1-Debug-windows.exe)
- [**Ubuntu** (v0.3.1)](https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-installer-0.3.1-Debug-ubuntu)

Use `-s` for silent mode with the default installation directory.

### One-Liner Install

**Windows CMD:**
```cmd
curl -LO https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-installer-0.3.1-Debug-windows.exe && metaffi-installer-0.3.1-Debug-windows.exe -s
```

**Windows PowerShell:**
```powershell
Invoke-WebRequest -Uri https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-installer-0.3.1-Debug-windows.exe -OutFile metaffi-installer.exe; Start-Process .\metaffi-installer.exe -ArgumentList '-s' -Wait
```

**Ubuntu:**
```bash
wget https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-installer-0.3.1-Debug-ubuntu && chmod +x metaffi-installer-0.3.1-Debug-ubuntu && sudo ./metaffi-installer-0.3.1-Debug-ubuntu -s
```

### What the Installer Does

**Windows:**
- Checks prerequisites and offers to install missing dependencies
- Copies MetaFFI files to the installation directory (default: `%USERPROFILE%\metaffi`)
- Adds the installation directory to `PATH`
- Sets `METAFFI_HOME` environment variable

**Ubuntu:**
- Checks prerequisites and offers to install missing dependencies
- Copies MetaFFI files to the installation directory (default: `/usr/local/metaffi`)
- Sets `METAFFI_HOME` in `~/.profile`

## Install Language Plugins

Plugins are distributed as `.zip` archives and installed with the `metaffi` CLI.

| Language | Windows | Ubuntu |
|:---------|:--------|:-------|
| **Python 3** | [Download](https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-python3-0.3.1-Debug-windows.zip) | [Download](https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-python3-0.3.1-Debug-ubuntu.zip) |
| **Go** | [Download](https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-go-0.3.1-Debug-windows.zip) | [Download](https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-go-0.3.1-Debug-ubuntu.zip) |
| **JVM** | [Download](https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-jvm-0.3.1-Debug-windows.zip) | [Download](https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-jvm-0.3.1-Debug-ubuntu.zip) |

After downloading, install each plugin with:

```bash
metaffi --plugin --install <path-to-plugin.zip>
```

### One-Liner Plugin Install (All Languages)

**Windows CMD:**
```cmd
metaffi --plugin --install https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-python3-0.3.1-Debug-windows.zip && metaffi --plugin --install https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-go-0.3.1-Debug-windows.zip && metaffi --plugin --install https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-jvm-0.3.1-Debug-windows.zip
```

**Ubuntu:**
```bash
metaffi --plugin --install https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-python3-0.3.1-Debug-ubuntu.zip && metaffi --plugin --install https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-go-0.3.1-Debug-ubuntu.zip && metaffi --plugin --install https://github.com/MetaFFI/metaffi-installer/releases/download/v0.3.1/metaffi-plugin-jvm-0.3.1-Debug-ubuntu.zip
```

The Python3 API is also available via pip: `pip install metaffi-api`

## Choose Your Workflow

MetaFFI supports two ways to call foreign code:

| | Dynamic Loading | Generated Stubs (Host Compiler) |
|:---|:----------------|:-------------------------------|
| **How** | Load modules and entities at runtime using the MetaFFI API | Generate typed wrappers with `metaffi -c --idl <file> -h <lang>` |
| **Best for** | Exploration, quick scripts, prototyping | Production codebases, large projects, CI |
| **Entity paths** | Written by hand | Generated for you |

The tutorial below uses **dynamic loading**. For the generated stubs workflow, see the [Host Compiler](/host-compiler/) page.

## Your First Cross-Language Call

This example calls a Go function from Python using dynamic loading.

### 1. Create the Go module

Create `hello.go`:

```go
package main

import "fmt"

func SayHello(name string) string {
    return fmt.Sprintf("Hello, %s! Greetings from Go.", name)
}
```

### 2. Compile with MetaFFI

```bash
metaffi -c --idl hello.go -g
```

This produces a MetaFFI-enabled dynamic library (`hello_MetaFFIGuest.dll` on Windows, `.so` on Linux).

### Optional: Generate Typed Stubs

Instead of writing entity paths and type arrays by hand, you can generate typed Python stubs:

```bash
metaffi -c --idl hello.go -h python3
```

This produces `hello_MetaFFIHost.py` — a typed Python module you can import and call directly. See the [Host Compiler](/host-compiler/) page for details.

### 3. Call from Python

Create `main.py`:

```python
from metaffi import MetaFFIRuntime, MetaFFITypes
from metaffi.metaffi_types import new_metaffi_type_info

# Load Go runtime
runtime = MetaFFIRuntime("go")

# Load the compiled Go module
module = runtime.load_module("hello_MetaFFIGuest")

# Load the SayHello function
say_hello = module.load_entity(
    "callable=SayHello",
    [new_metaffi_type_info(MetaFFITypes.metaffi_string8_type)],
    [new_metaffi_type_info(MetaFFITypes.metaffi_string8_type)])

# Call it!
result = say_hello("Python")
print(result)  # "Hello, Python! Greetings from Go."

runtime.release_runtime_plugin()
```

## Docker Containers

Pre-installed Docker containers are available:

```bash
# Ubuntu 24.04
docker pull tscs/metaffi-u2404:0.3.1

# Windows Server Core 2022
docker pull tscs/metaffi-win-core2022:0.3.1
```

## Build from Source

MetaFFI uses **CMake** and **vcpkg** for dependency management.

1. Install CMake and vcpkg
2. Clone [metaffi-root](https://github.com/MetaFFI/metaffi-root)
3. Run CMake configuration and build
4. CMake will pull the required dependencies

The repository includes MetaFFI Core, Python3 Plugin, JVM Plugin, and Go Plugin.

## Distributing Binaries

You can distribute MetaFFI binaries with your application (under the [license](https://github.com/MetaFFI/metaffi.github.io/blob/main/LICENSE) terms). Place the MetaFFI directory within your application directory and set `METAFFI_HOME`. On Windows, also add it to `PATH`.

## Environment Variables

| Variable | Description |
|:---------|:------------|
| `METAFFI_HOME` | Points to MetaFFI installation directory. **Required.** |
| `PATH` (Windows) | Must include `METAFFI_HOME`. |
