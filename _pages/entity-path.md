---
title: "Entity Path"
permalink: /entity-path/
toc: true
toc_sticky: true
---

**Note:** Entity paths are used in **dynamic loading** mode. If you use the [host compiler](/host-compiler/) to generate typed stubs, entity paths are generated for you — you do not need to write them by hand.
{: .notice--info}

An *entity path* is a string that tells MetaFFI where to find a specific entity (function, method, field, constructor) within a loaded module.

The entity path consists of key-value pairs and tags separated by commas:

```
key1=val1,tag1,...,tagN,keyN=valN
```

Each language plugin uses different keys and tags. While they are similar across plugins, they are not identical.

## Language-Specific Documentation

| Language | Keys | Tags |
|:---------|:-----|:-----|
| [Python3](/entity-path/python3/) | `callable`, `attribute` | `instance_required`, `setter`, `getter`, `varargs`, `named_args` |
| [JVM](/entity-path/jvm/) | `class`, `callable`, `field` | `instance_required`, `setter`, `getter` |
| [Go](/entity-path/go/) | `callable`, `global`, `field` | `instance_required`, `setter`, `getter` |

## Common Tags

### `instance_required`

Used across all languages to indicate that an entity is an instance member (not static). When this tag is present, the first parameter passed to the callable must be the object instance.

### `setter` / `getter`

Used to load a setter or getter for a field, attribute, or global variable.

## Examples

```
callable=HelloWorld                              # Go function
callable=MyMap.Contains,instance_required        # Go instance method
class=com.example.MyClass,callable=greet         # Java static method
class=com.example.MyClass,callable=<init>        # Java constructor
callable=testmap.contains,instance_required      # Python instance method
attribute=five_seconds,getter                    # Python global getter
```
