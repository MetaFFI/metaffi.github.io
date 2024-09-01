# Go Plugin - Function Path

## <span style="font-family: courier;">callable=[function or method]</span>

* Function
* Struct.Method

```go
func HelloWorld() // callable=HelloWorld
func (this *MyMap) Contains(k string) bool // callable=MyMap.Contains
```

## <span style="font-family: courier;">global=[global variable/const name]</span>

* Global variable name

```go
const FiveSeconds = time.Second*5 // global=FiveSeconds
var SomeNumber int // global=SomeNumber
```

## <span style="font-family: courier;">field=[field name]</span>

* Struct.Field

```go
type Student struct{
 Name string // field=Student.Name
}
```

## <span style="font-family: courier;">instance_required</span>

* Tag for *callable* or *field* to state the entity requires an instance of an object. The instance is passed in the $1^{st}$ parameter.

```go
// callable=MyMap.Contains,instance_required
func (this *MyMap) Contains(k string) bool 

type Student struct{
 Name string // field=Student.Name,instance_required
}
```

## <span style="font-family: courier;">setter</span>

* Tag for *global* or *field* to load a setter for the entity

```go
// global=SomeNumber,setter - loads a setter for SomeNumber
var SomeNumber int 

// field=Student.Name,instance_required,setter loads a setter for the field
type Student struct{
 Name string
}
```

## <span style="font-family: courier;">getter</span>

* Tag for *global* or *field* to load a getter for the entity

```go
// global=FiveSeconds,getter - loads a getter for FiveSeconds
const FiveSeconds = time.Second*5

// global=SomeNumber,getter - loads a getter for SomeNumber
var SomeNumber int 

// field=Student.Name,instance_required,getter loads a getter for the field
type Student struct{
 Name string
}
```
