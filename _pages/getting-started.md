---
title: "Getting Started"
permalink: /getting-started/
toc: true
toc_sticky: true
---

## Prerequisites

- **Windows 11** or **Ubuntu 22.04** (other versions may work but are not tested with installer)
- At least one supported language runtime installed:
  - **Go** v1.22+
  - **OpenJDK** 11, 21, or 22
  - **Python** 3.11+

## Install MetaFFI Core

Download and run the installer for your platform:

- [**Windows** (v0.3.0)](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0.exe)
- [**Ubuntu** (v0.3.0)](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0)

Use `-s` for silent mode with default installation directory.

### One-Liner Install

**Windows CMD:**
```cmd
curl -LO https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0.exe && metaffi-installer-0.3.0.exe -s
```

**Windows PowerShell:**
```powershell
Invoke-WebRequest -Uri https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0.exe -OutFile metaffi-installer.exe; Start-Process .\metaffi-installer.exe -ArgumentList '-s' -Wait
```

**Ubuntu:**
```bash
wget https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-installer-0.3.0 && chmod +x metaffi-installer-0.3.0 && ./metaffi-installer-0.3.0 -s
```

### What the Installer Does

**Windows:**
- Checks prerequisites and offers to install missing dependencies
- Copies MetaFFI files to the installation directory (default: `%USERPROFILE%\metaffi`)
- Adds the installation directory to `PATH`
- Sets `METAFFI_HOME` environment variable

**Linux:**
- Checks prerequisites and offers to install missing dependencies
- Copies MetaFFI files to the installation directory (default: `/usr/local/metaffi`)
- Sets `METAFFI_HOME` in `~/.profile`

## Install Language Plugins

Install the plugins for the languages you want to use:

| Language | Windows | Ubuntu |
|:---------|:--------|:-------|
| **Python 3** | [Download](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311.exe) | [Download](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311) |
| **Go** | [Download](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-go.exe) | [Download](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-go) |
| **OpenJDK** | [Download](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk.exe) | [Download](https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk) |

The Python3 API is also available via pip: `pip install metaffi-api`

### One-Liner Plugin Install (All Languages)

**Windows CMD:**
```cmd
curl -LO https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311.exe && metaffi-plugin-installer-0.3.0-python311.exe && curl -LO https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-go.exe && metaffi-plugin-installer-0.3.0-go.exe && curl -LO https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk.exe && metaffi-plugin-installer-0.3.0-openjdk.exe
```

**Ubuntu:**
```bash
wget https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-python311 -O python311 && chmod +x python311 && ./python311 && wget https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-go -O go && chmod +x go && ./go && wget https://github.com/MetaFFI/metaffi-root/releases/download/v0.3.0/metaffi-plugin-installer-0.3.0-openjdk -O openjdk && chmod +x openjdk && ./openjdk
```

## Your First Cross-Language Call

This example calls a Go function from Python.

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
# Ubuntu 22.04
docker pull tscs/metaffi-u2204:0.3.0

# Windows Server Core 2022
docker pull tscs/metaffi-win-core2022:0.3.0
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
