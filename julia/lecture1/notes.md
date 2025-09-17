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
# Jupyter
Jupyter can be started from any directory with
```bash
jupyter lab
```
For this I'm using my `quantecon` conda environment, which will also be used for the python lectures, though VS Code has built in Jupyter support via an extension which doesn't require conda for use with Julia.

Note that if you update Julia (via `juliaup update`) you will need to rebuild your IJulia kernel:
```bash
conda activate quantecon # So using the right jupyter

julia --project=.
using Pkg
Pkg.build("IJulia")
```
This regenerates the Jupyter kernel config to point at the **current Julia symlink** (`~/.julia/juliaup/bin/julia`)

You can verify the kernel with
```bash
jupyter kernel speclist
```
after exiting the REPL

You should se something like
```bash
julia-1.11  /Users/patrick/Library/Jupyter/kernels/julia-1.11
python3     /Users/patrick/miniconda3/envs/quantecon/share/jupyter/kernels/python3
```
Relaunch the JupyterLab and select **Julia 1.11** as the kernel.

## Modes ##
Jupyter uses a modal editing system

`Esc` takes you from Edit mode to Command mode

`Enter` takes you from Command mode to Edit mode

## Running Julia in Jupyter ##
`Shift + Enter` runs the current cell

## Help ##
To get help with a Julia function like `repeat`, enter
```julia
? repeat
```
## Other Content ##
You can enter LaTeX as well:

```LaTeX
$$ \exp(i \pi) = -1 $$
```
To run this cell:
```bash
Esc # Enter command mode
m # Tell Jupyter that we're writing Markdown
Shift + Enter # Run the cell block
```
And unicode:

```julia
\alpha

using LinearAlgebra
x \cdot y
```
Shell commands can be executed by prepending `;`

```julia
; ls
```

And for package operations prepend `]`
```julia
] st # gives the status of installed packages in the current environment
```
# Using Jupyter in VS Code ##
You can create or open a `.ipynb` file in VS Code directly as long as you have the Jupyter and Julia extensions.

You will need to select the `Julia` kernel. You can just use the UI or by keyboard:

```bash
Cmd + Shift + P # Open Command Palette
Jupyter: Select Kernel
```
And then use the arrow keys to chose the Julia 1.11 (or 1.xx) kernel from the list
