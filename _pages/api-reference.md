---
title: "API Reference"
permalink: /api-reference/
toc: true
toc_sticky: true
---

MetaFFI provides language-specific APIs that share the same structure across all supported languages:

1. **`MetaFFIRuntime`** — Load a foreign language runtime into the process
2. **`MetaFFIModule`** — Load a foreign module (JAR, `.py` file, compiled `.dll`/`.so`)
3. **`load` / `load_entity`** — Load a specific entity (function, method, field) and get back a callable

## Language APIs

| Language | API | Install |
|:---------|:----|:--------|
| [Python3](/api-reference/python3/) | `MetaFFIRuntime`, `MetaFFIModule` | `pip install metaffi-api` |
| [JVM](/api-reference/jvm/) | `MetaFFIRuntime`, `MetaFFIModule`, `Caller` | `metaffi.api.jar` (ships with installer) |
| [Go](/api-reference/go/) | `MetaFFIRuntime`, `MetaFFIModule` | `go get github.com/MetaFFI/sdk/api/go` |

## Common Pattern

All three APIs follow the same pattern:

```
1. Create runtime  →  MetaFFIRuntime("openjdk")
2. Load module     →  runtime.load_module("mylib.jar")
3. Load entity     →  module.load_entity("class=...,callable=...", params, retvals)
4. Call it          →  result = entity(args...)
5. Release         →  runtime.release_runtime_plugin()
```

The [Entity Path](/entity-path/) documentation describes how to specify the location of entities within each language's modules.

## Two Usage Modes

MetaFFI offers two ways to call foreign code:

### Dynamic API Calls

Use the API directly — load a runtime, load a module, load an entity by its [entity path](/entity-path/), and call it. This is the pattern shown above and throughout the [Examples](/examples/) page.

Best for: exploration, quick scripts, prototyping.

### Generated Wrappers (Host Compiler)

Use the [host compiler](/host-compiler/) to generate typed wrappers that call the API for you. The generated module exposes normal typed functions — no entity paths or type arrays in your application code.

```bash
metaffi -c --idl hello.go -h python3
```

```python
import hello_MetaFFIHost as hello
hello.bind_module_to_code("hello_MetaFFIGuest", "go")
result = hello.SayHello("Python")
```

Best for: production codebases, large projects, CI.

Generated wrappers do not change runtime overhead — they wrap the same API calls shown above. See the [Host Compiler](/host-compiler/) page for details.
