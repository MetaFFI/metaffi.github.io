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
