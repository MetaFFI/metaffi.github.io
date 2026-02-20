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
  **Just Call. Any Language Module from Any Language.**<br/>
  Like <code>dlopen</code> + <code>dlsym</code>, but for JARs, Python packages, and Go modules. Each language runs in its native runtime.

feature_row:
  - title: "Native Runtimes, Microsecond Calls"
    excerpt: "Each language runs in its own original runtime — no VMs, interpreters, or recompilation. Cross-language calls complete in microseconds."
  - title: "Two Ways to Call"
    excerpt: "Load and call dynamically at runtime, or generate typed stubs with the [host compiler](/host-compiler/) for IDE autocomplete and type safety. Your choice."
  - title: "No Bridge Code in Your App"
    excerpt: "No JNI wrappers, CPython embedding, or cgo in your application code. Write your host code in one language only."
---

{% include feature_row %}

## Quick Taste

Use Apache log4j from Python — no JVM bridge code, no compilation step:

{% include tabs.html %}

<div class="metaffi-tabs" role="tablist" aria-label="Usage mode">
<button class="metaffi-tab" role="tab" aria-selected="true" aria-controls="qt-dynamic" id="qt-tab-dynamic" tabindex="0">Dynamic Loading</button>
<button class="metaffi-tab" role="tab" aria-selected="false" aria-controls="qt-stubs" id="qt-tab-stubs" tabindex="-1">Generated Stubs (Host Compiler)</button>
</div>

<div class="metaffi-tabpanel" role="tabpanel" id="qt-dynamic" aria-labelledby="qt-tab-dynamic" markdown="1">

```python
from metaffi import MetaFFIRuntime, MetaFFITypes
from metaffi.metaffi_types import new_metaffi_type_info

runtime = MetaFFIRuntime("openjdk")
module = runtime.load_module("log4j-api-2.21.1.jar;log4j-core-2.21.1.jar")

getLogger = module.load_entity(
    "class=org.apache.logging.log4j.LogManager,callable=getLogger",
    [new_metaffi_type_info(MetaFFITypes.metaffi_string8_type)],
    [new_metaffi_type_info(MetaFFITypes.metaffi_handle_type)])

logger = getLogger("mylogger")
```

</div>

<div class="metaffi-tabpanel" role="tabpanel" id="qt-stubs" aria-labelledby="qt-tab-stubs" hidden markdown="1">

```bash
# One-time: generate typed Python stubs for the JAR
metaffi -c --idl log4j-api-2.21.1.jar -h python3
```

```python
import log4j_api_MetaFFIHost as log4j

log4j.bind_module_to_code(
    "log4j-api-2.21.1.jar;log4j-core-2.21.1.jar", "openjdk")

logger = log4j.getLogger("mylogger")
```

</div>

<noscript>

**Generated Stubs mode:** Run `metaffi -c --idl log4j-api-2.21.1.jar -h python3` to generate typed stubs, then import and call `log4j.getLogger("mylogger")` directly. See the [Host Compiler](/host-compiler/) page for details.

</noscript>

No bridge code. No rewrites. Just load and call — or generate stubs and call.

[See more examples](/examples/){: .btn .btn--primary}
[Host Compiler docs](/host-compiler/){: .btn .btn--info}

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

MetaFFI works like `dlopen`/`LoadLibrary` + `dlsym`/`GetProcAddress`, but for language modules instead of native binaries. It uses Foreign Function Interface (FFI) and embedding mechanisms to link language runtimes together through a C-based hub. Each language continues to run in its own original runtime — there is no virtual machine, interpreter, or recompilation involved.

The system uses an *entity path* string to locate functions, methods, fields, and constructors within foreign modules, and a capabilities-based *XCall* calling convention to marshal data between runtimes using Common Data Types.

**Two usage modes:** You can call foreign code dynamically using the MetaFFI API, or use the [host compiler](/host-compiler/) to generate typed stubs that wrap the API calls for you. Both modes use the same runtime — stubs change ergonomics, not performance.

[Read the paper](https://www.mdpi.com/2674-113X/4/3/21){: .btn .btn--info}
[Getting Started](/getting-started/){: .btn .btn--primary}
[Performance](/performance/){: .btn .btn--success}
