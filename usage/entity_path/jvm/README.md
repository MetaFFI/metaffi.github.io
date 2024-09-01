# JVM Plugin - Function Path

## <span style="font-family: courier;">class=[full class name]</span>

* Full class name, including the packages

Logger class in log4j - `class=org.apache.logging.log4j.Logger`

TestRuntime class in sanity package - `class=sanity.TestRuntime`

## <span style="font-family: courier;">callable=[method]</span>

* Method name

```java
package sanity;

public class TestMap
{ 
    // class=sanity.TestMap,callable=contains
    public boolean contains(String k){...}
    
    // class=sanity.TestMap,callable=<init>
    public TestMap(){...}
}

public class TestRuntime
{
    // class=sanity.TestRuntime,callable=joinStrings
    public static String joinStrings(String[] arr){...}
}
```

## <span style="font-family: courier;">field=[field name]</span>

* Field name

```java
public class TestMap
{
    public String name; // class=sanity.TestMap,field=name
}

public class TestRuntime
{
    // class=sanity.TestRuntime,field=fiveSeconds
    public static final int fiveSeconds = 5;
}
```

## <span style="font-family: courier;">instance_required</span>

* Tag for *callable* or *field* to indicate the entity is **not** static. The instance is passed in the $1^{st}$ parameter.

```java
package sanity;

public class TestMap
{ 
    // class=sanity.TestMap,callable=contains,instance_required
    public boolean contains(String k){...}

    // class=sanity.TestMap,field=name,instance_required
    public String name;
}
```

## <span style="font-family: courier;">setter</span>

* Tag for *field* to load a setter for the entity

```java
package sanity;

public class TestMap
{ 
    // class=sanity.TestMap,callable=contains,setter
    public static int x = 240;

    // class=sanity.TestMap,field=name,instance_required,setter
    public String name;
}
```

## <span style="font-family: courier;">getter</span>

* Tag for *field* to load a getter for the entity

```java
package sanity;

public class TestRuntime
{
    // class=sanity.TestRuntime,field=fiveSeconds,getter
    public static final int fiveSeconds = 5;
}

public class TestMap
{ 
    // class=sanity.TestMap,field=name,instance_required,getter
    public String name;
}
```
