# System Overview

MetaFFI is a multi-lingual, in-direct, pluggable interoperability system which satisfies the requirements of \emph{simple interoperability} as defined in \cite{empirical_multi_lingual}. Using the system, calling a foreign entity is similar to calling an entity in the host language and requires only writing host language code. The effort of adding additional language support is independent of the number of already existing supported languages due to the indirect design of the system. Moreover, adding the $(n+1)_{th}$ language to the system automatically binds it to all the already supported $n$ languages. Unlike VM solutions which require the language runtime to be in the VM's "executable" language (e.g. TruffleVM requires Bytecode \cite{trufflevm}, .NET framework requires CIL \cite{ms_cil}), MetaFFI makes no assumptions on the language runtime.

\subsection{Usage Example} \label{sec:example}
\begin{listing}
\begin{singlespace}
\begin{minted}[bgcolor=CodeBG,fontsize=\footnotesize,autogobble,tabsize=2,linenos]{python}
// GoDeque.go
package TestFuncs

func HelloWorld() {
	println("Hello World, From Go!")
}

type GoDeque struct{
	items []interface{}
	Name string
}

func NewGoDeque() *GoDeque{
	return &GoDeque{ 
		items: make(interface{}, 0),
	}
}

func (this *GoDeque) Push(v interface{}){
	this.items = append(this.items, v)
}

func (this *GoDeque) Pop() interface{}{
	if len(this.items) == 0 {
        return nil
    }
    item := this.items[0]
    this.items = this.items[1:]
    return item
}

# GoDeque.py
from GoDeque_MetaFFIHost import *
import collections
from datetime import datetime

if __name__ == '__main__':
	HelloWorld()

	d = GoDeque()
	d.Push(250)
	d.Push(['test', 'me'])

	deq = collections.deque()
	deq.append(600)
	d.Push(deq)

	print(d.Pop())
	print(d.Pop())
	print(d.Pop())

	d.SetName('GoDeque')
	print(d.GetName())
\end{minted}
\end{singlespace}
\caption{GoDeque.py: Python $\rightarrow$ Go Usage Example}
\label{code:metaffi_example}
\end{listing}
The code in listing \ref{code:metaffi_example} presents a Go code (lines 1-31) and Go code (lines 32-53). This demonstration shows how to use MetaFFI to call from Python to Go. In this use case the developer implemented \emph{GoDeque}, a queue implementation in Go. The code also implements \code{HelloWorld} function merely for the demonstration. The Python code calls \code{HelloWorld} (line 38), creates \code{GoDeque} (line 40) object, pushes into the Deque an integer (line 41), string array (line 42), creates a Python deque object with an integer within (lines 44-45) and pushes the Python object into the Go deque (line 46). Next, the Go deque items are popped and printed (lines 48-50). Last, Python code sets GoDeque's \code{Name} public field (line 10) and prints the field's value (line 53).\\
In order to build the interoperability code, the user executes the MetaFFI compiler:\\
\textbf{metaffi -c --idl GoDeque.go -g -h python3}
\begin{itemize}
    \item \textbf{\code{-c}} - compile
    \item \textbf{\code{--idl}} - file to extract IDL (\code{GoDeque.go})
    \item \textbf{\code{-g}} - build guest language code (Go stated in IDL)
    \item \textbf{\code{-h}} - build host language code (\code{Python3}) to interact with guest code
\end{itemize}
The Python code defining \code{HelloWorld} function and \code{GoDeque} object is generated to the file \code{GoDeque\_MetaFFIHost.py} (imported in line 33). Go executable code is generated to \code{GoDeque.so} in Linux (DLL in windows and dylib in MacOS). Finally, to execute the code, the user simply executes it as any other Python main file: \code{python3 GoDeque.py} which its output is presented in figure \ref{fig:godeque_output}.
\begin{figure}[H]
  \centering
  \includegraphics[scale=0.4]{figures/godeque_output.png}
  \caption{GoDeque.py output\protect\footnotemark }
  \label{fig:godeque_output}
\end{figure}
\footnotetext{Image edited to remove user name and host name for anonymity purposes}
In the example, calling to \code{HelloWorld} function is a shallow binding feature (line 38), while the creation of a foreign object (\code{GoDeque}), using its methods, public field, and even placing a Python object within a Go data structure (lines 40-53), shows MetaFFI deep-like binding behaviour by providing deep-binding features. The reason MetaFFI is deep-like binding is that it does not actually access the different languages' runtimes memory directly (as opposed to VM, where there is a common runtime). Also, the example shows Python can push different types to GoDeque (lines 41-46), as MetaFFI supports dynamic types.

Due to MetaFFI language-agnostic indirect design, Python is not aware it is calling specifically to Go and Go is not aware it is explicitly called by Python. Therefore, calling from Python (or any other language) to any language uses the same generated code. Similarly, when Go is called by any other language, it uses the same generated code. Using this design, the effort required to add additional language support is independent of the amount of already supported languages. Moreover, interoperating between $n$ languages requires $O(n)$ interoperability mechanisms, which is a significant advantage compared to any direct approach which requires $O(n^2)$ mechanisms.

An example of $3rd$ party library shows the usage of Pandas \cite{pandas}, a popular data analysis library implemented in Python.  Listing \ref{code:python_pandas} shows a simple usage of Pandas in Python and 
listings \ref{code:metaffi_go_pandas} and \ref{code:metaffi_java_pandas} show the same usage in Go and Java using MetaFFI system, respectively. The MetaFFI compile command is \textbf{metaffi -c --idl pandas --idl-plugin py -g -h go openjdk}, where \code{--idl-plugin} states the IDL is generated from Python code.

\begin{listing}[H]
\begin{singlespace}
\begin{minted}[bgcolor=CodeBG,fontsize=\footnotesize,autogobble,tabsize=2,linenos]{python}
# read input.csv into dataframe
df = pandas.read_csv('input.csv')
# get second line from input.csv
# [] operator is calling the Python method, __getitem__()
df_line_two = df.iloc[1] 
# turn data frame into string, and print to screen
print(df_line_two.to_string())
\end{minted}
\end{singlespace}
\caption{Pandas example - Python use case}
\label{code:python_pandas}
\end{listing}

\begin{listing}[H]
\begin{singlespace}
\begin{minted}[bgcolor=CodeBG,fontsize=\footnotesize,autogobble,tabsize=2,linenos]{java}
pandas.load("pandas_MetaFFIGuest"); // Load Pandas module
// read_csv dataframe
var df = new DataFrame(pandas.read_csv("input.csv"));
// get "iloc" from iloc property
var iloc = new _iLocIndexer((MetaFFIHandle)df.Getiloc());
// call __getitem__(), equivalent to [] in Python
var dfSecondRow = new DataFrame(iloc.__getitem__(1));
// get string and print it
System.out.println(dfSecondRow.to_string());
\end{minted}
\end{singlespace}
\caption{Pandas example - Java using MetaFFI}
\label{code:metaffi_java_pandas}
\end{listing}

\begin{listing}[H]
\begin{singlespace}
\begin{minted}[bgcolor=CodeBG,fontsize=\footnotesize,autogobble,tabsize=2,linenos]{go}
pandas.Load("pandas_MetaFFIGuest") // Load Pandas module
// calls read_csv()
dfHandle, _ := pandas.ReadCsv1("input.csv")
// creates returned data frame object
df := pandas.DataFrame{ H: dfHandle.(metaffi.Handle) }
// get "iloc" from iloc property
ilocHandle, _ := df.Getiloc()
// create iloc object
iloc := pandas_core_indexing.U_ILocIndexer{ 
    H: ilocHandle.(metaffi.Handle)
}
// call __getitem__(), equivalent to [] in Python
dfSecondRowHandle, _ = iloc.U_Getitem__(1)

// create second row data frame object
dfSecondRow := pandas.DataFrame{ 
    H: dfFirstRowHandle.(metaffi.Handle)
}
str, _ := dfSecondRow.ToString1() // get string
fmt.Println(str) // print
\end{minted}
\end{singlespace}
\caption{Pandas example - Go using MetaFFI}
\label{code:metaffi_go_pandas}
\end{listing}