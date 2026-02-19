---
title: "JVM Entity Path"
permalink: /entity-path/jvm/
toc: true
toc_sticky: true
---

## `class=[full class name]`

Specifies the fully qualified class name, including packages.

- Logger class in log4j: `class=org.apache.logging.log4j.Logger`
- TestRuntime class in sanity package: `class=sanity.TestRuntime`

## `callable=[method]`

Specifies a method name. Use `<init>` for constructors.

```java
package sanity;

public class TestMap {
    // class=sanity.TestMap,callable=contains
    public boolean contains(String k) { ... }

    // class=sanity.TestMap,callable=<init>
    public TestMap() { ... }
}

public class TestRuntime {
    // class=sanity.TestRuntime,callable=joinStrings
    public static String joinStrings(String[] arr) { ... }
}
```

## `field=[field name]`

Specifies a field name.

```java
public class TestMap {
    public String name;  // class=sanity.TestMap,field=name
}

public class TestRuntime {
    // class=sanity.TestRuntime,field=fiveSeconds
    public static final int fiveSeconds = 5;
}
```

## `instance_required`

Tag for `callable` or `field` to indicate the entity is **not** static. The instance is passed as the first parameter.

```java
package sanity;

public class TestMap {
    // class=sanity.TestMap,callable=contains,instance_required
    public boolean contains(String k) { ... }

    // class=sanity.TestMap,field=name,instance_required
    public String name;
}
```

## `setter`

Tag for `field` to load a setter for the entity.

```java
package sanity;

public class TestMap {
    // class=sanity.TestMap,field=x,setter
    public static int x = 240;

    // class=sanity.TestMap,field=name,instance_required,setter
    public String name;
}
```

## `getter`

Tag for `field` to load a getter for the entity.

```java
package sanity;

public class TestRuntime {
    // class=sanity.TestRuntime,field=fiveSeconds,getter
    public static final int fiveSeconds = 5;
}

public class TestMap {
    // class=sanity.TestMap,field=name,instance_required,getter
    public String name;
}
```
