---
title: "Paper"
permalink: /paper/
toc: true
toc_sticky: true
---

## MetaFFI: A Multi-Lingual Indirect Interoperability System

The MetaFFI paper, published in the MDPI *Software* journal, discusses the research, design, and internals of the system. It covers the architecture, the XCall calling convention, Common Data Types, and the plugin system.

Sections for academic audience or technical audience are explicitly marked, as explained at the end of the introduction section.

[Read the paper](https://www.mdpi.com/2674-113X/4/3/21){: .btn .btn--primary .btn--large}

For practical usage, see the [Getting Started](/getting-started/) guide, [Examples](/examples/), and [Host Compiler](/host-compiler/) documentation.

## XCall: Capabilities-Based Calling Convention

The XCall is the mechanism MetaFFI uses to facilitate cross-language calls. MetaFFI's agnostic approach ensures that each language remains unaware of the others, allowing for independent plugin development.

XCall is a runtime-independent calling convention that uses Common Data Types (inspired by Microsoft's Variant and GTK gObject) to enable languages to call and use entities in other languages, even if they lack certain features.

While the generic calling convention supports a wide range of cross-language calls, it can affect performance. Therefore, XCall determines the calling convention used at runtime, based on the required capabilities. This allows MetaFFI to:

- Use the full-featured calling convention when necessary
- Use a subset of capabilities to improve performance
- Revert completely to a direct function call when possible (like x64 calling convention)

This results in efficient cross-language interactions.

**Note:** The current version of MetaFFI always uses the generic calling convention due to the differences between the initial languages implemented.

## GitHub Projects

The [MetaFFI Organization](https://github.com/MetaFFI/) on GitHub contains:

| Repository | Description |
|:-----------|:------------|
| [metaffi-root](https://github.com/MetaFFI/metaffi-root) | CMake build system root, VSCode workspace, dev containers |
| [metaffi-core](https://github.com/MetaFFI/metaffi-core/) | CLI tool, XLLR, XCall implementation, Common Data Types |
| [lang-plugin-python3](https://github.com/MetaFFI/lang-plugin-python3) | Python3 support via CPython API |
| [lang-plugin-openjdk](https://github.com/MetaFFI/lang-plugin-openjdk) | JVM support via JNI |
| [lang-plugin-go](https://github.com/MetaFFI/lang-plugin-go) | Go support via cgo |
| [metaffi-installer](https://github.com/MetaFFI/metaffi-installer) | Python-based installer |
| [containers](https://github.com/MetaFFI/containers) | Dockerfiles for pre-installed containers |

## Report a Bug

Found a bug? [Open an issue](https://github.com/MetaFFI/metaffi-root/issues/new) on the metaffi-root repository.
