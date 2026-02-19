---
title: "MetaFFI"
layout: splash
permalink: /
header:
  overlay_color: "#1a1a2e"
  overlay_filter: "0.4"
  actions:
    - label: "Get Started"
      url: /getting-started/
    - label: "View on GitHub"
      url: https://github.com/MetaFFI/
excerpt: >
  **Use Any Language Module from Any Language.**<br/>
  No serialization. No network hop. No code generation. Each language runs in its own original runtime.

feature_row:
  - title: "Native Runtime, Zero Overhead"
    excerpt: "Each language runs in its own original runtime — no VMs, interpreters, or recompilation. MetaFFI bridges runtimes using FFI and embedding, preserving native performance."
  - title: "5-15x Faster than gRPC"
    excerpt: "In-process calls eliminate network overhead, serialization, and server management. Cross-language calls complete in microseconds, not milliseconds."
  - title: "Single-Language Development"
    excerpt: "Write your host code in one language. No `.proto` files, no generated stubs, no multi-language build systems. Just load and call."
---

{% include feature_row %}

## Quick Taste

Load a Java library from Python in 6 lines:

```python
from metaffi import MetaFFIRuntime

runtime = MetaFFIRuntime("openjdk")
module = runtime.load_module("log4j-api-2.21.1.jar;log4j-core-2.21.1.jar")

getLogger = module.load_entity(
    "class=org.apache.logging.log4j.LogManager,callable=getLogger",
    [metaffi_string8_type], [metaffi_handle_type])

logger = getLogger("mylogger")
```

No gRPC server. No protobuf. No code generation. Just load and call.

[See more examples](/examples/){: .btn .btn--primary}

## Supported Languages

| Language | Runtime | Status |
|:---------|:--------|:-------|
| **Go** | Go runtime via cgo | v1.22+ |
| **JVM** | OpenJDK via JNI | JDK 11, 21, 22 |
| **Python 3** | CPython via CPython API | v3.11+ |

## Supported Operating Systems

| OS | Tested |
|:---|:-------|
| **Windows** | Windows 11, Server 2022 |
| **Ubuntu** | 22.04 |

## How It Works

MetaFFI uses Foreign Function Interface (FFI) and embedding mechanisms to link language runtimes together through a C-based hub. Each language continues to run in its own original runtime — there is no virtual machine, interpreter, or recompilation involved.

The system uses an *entity path* string to locate functions, methods, fields, and constructors within foreign modules, and a capabilities-based *XCall* calling convention to marshal data between runtimes using Common Data Types.

[Read the paper](https://arxiv.org/abs/2408.14175){: .btn .btn--info}
[Getting Started](/getting-started/){: .btn .btn--primary}
[Performance](/performance/){: .btn .btn--success}
