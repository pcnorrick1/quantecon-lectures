# Quick Install
Since I'm using VS Code from the beginning and have experience with Git and CLI, the quick way of getting set up will be:

- Open a Jupyter notebook

- Install the relevant packages in the Julia REPL with

    ```Julia
    using Pkg; Pkg.instantiate()
    ```
I'll also be working on Mac for these lectures

# Opening Julia
In the terminal just type
```bash
julia
```
To open the REPL (Read-Evaluate-Print-Loop)

## Package Mode
Enter package mode with
```julia
]
```
And you can add the `IJulia` package with
```julia
add IJulia
```
Alternatively (in a .jl file, for example), you can add packages with
```julia
using Pkg # loads the Pkg standard library. Like import pkg in Python

Pkg.add("IJulia") # Calls Pkg's add function
```
You can also do it in one line from the REPL:

```julia
using Pkg; Pkg.add("IJulia")
```
But if in the REPL package mode is more convenient.

Leave package mode with the `backspace/delete` key or with
```bash
ctrl + C
```

## Exiting Julia
You can exit julia from the REPL with either
```julia
exit()
```
or
```bash
ctrl + D
```
## Starting the REPL Inside VS Code
You can open an integrated terminal in VS Code with
```bash
ctrl + `
```
And enter the REPL as described above.

Alternatively you can open the Command Palette with
```bash
cmd + shift + P
```
And type
```bash
> Julia: Start REPL
```
The third and fastest way is the shortcut
```bash
option + J
option + O
```
