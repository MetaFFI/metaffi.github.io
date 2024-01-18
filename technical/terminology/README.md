# Terminology

* **Language** - Pair of `(Syntax, Runtime)` (e.g., Python $\neq$ Jython).
* **Programming Language** - a Language used to write the logic layer of a program
* **Host Language** - Language initiating a call to a different language
* **Guest Language** - Language implementing the called code
* **Foreign Entity** – Function, method, field (etc.) in the guest language
* **Shallow Interoperability Binding** – Basic accessibility to guest Language (e.g. calling function)
* **Deep Interoperability Binding** – Broad accessibility to guest language (direct access to objects/types)
* **Foreign Function Interface (FFI)** – A shallow binding mechanism that provides the ability to call a function from a single Host to a single Guest (one way)
* **C-FFI** - An FFI mechanism binding with C
* **Interoperability mechanisms** - Mechanisms allowing to use multiple languages in the same operating system process (e.g. FFI, runtime embedding)
* **Language Port** - A new language with the same syntax as the porting language with another runtime environment (e.g. Jython\cite{jython}, IronPython\cite{ironpython}, JRuby\cite{jruby})
