---
title: "Go Entity Path"
permalink: /entity-path/go/
toc: true
toc_sticky: true
---

## `callable=[function or method]`

Specifies a function or struct method.

```go
func HelloWorld()                              // callable=HelloWorld
func (this *MyMap) Contains(k string) bool     // callable=MyMap.Contains
```

## `global=[global variable/const name]`

Specifies a package-level variable or constant.

```go
const FiveSeconds = time.Second * 5   // global=FiveSeconds
var SomeNumber int                    // global=SomeNumber
```

## `field=[field name]`

Specifies a struct field using `Struct.Field` notation.

```go
type Student struct {
    Name string   // field=Student.Name
}
```

## `instance_required`

Tag for `callable` or `field` to indicate the entity requires an instance of an object. The instance is passed as the first parameter.

```go
// callable=MyMap.Contains,instance_required
func (this *MyMap) Contains(k string) bool

type Student struct {
    Name string   // field=Student.Name,instance_required
}
```

## `setter`

Tag for `global` or `field` to load a setter for the entity.

```go
// global=SomeNumber,setter — loads a setter for SomeNumber
var SomeNumber int

// field=Student.Name,instance_required,setter — loads a setter for the field
type Student struct {
    Name string
}
```

## `getter`

Tag for `global` or `field` to load a getter for the entity.

```go
// global=FiveSeconds,getter — loads a getter for FiveSeconds
const FiveSeconds = time.Second * 5

// global=SomeNumber,getter — loads a getter for SomeNumber
var SomeNumber int

// field=Student.Name,instance_required,getter — loads a getter for the field
type Student struct {
    Name string
}
```
