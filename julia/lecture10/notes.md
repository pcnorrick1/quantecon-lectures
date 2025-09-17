Note: I am skipping straight to Lecture 10 from Lecture 1 because I want to use VS Code and .jl files for lectures 2-9 instead of relying exclusively on the Jupyter Notebooks

# VS Code #
Maybe I'll switch to Vim or Neovim at some point, but VS Code with Vim Motions seems good enough for now

[Modern Julia Workflows](https://modernjuliaworkflows.org/) has alternative approaches

The [Julia VS Code Documentation](https://www.julia-vscode.org/docs/dev/gettingstarted/#Installation-and-Configuration-1) should be read through

Also the general [VS Code Documentation](https://code.visualstudio.com/docs/getstarted/userinterface)

# Julia in VS Code #
This section is for working through the [Julia VS Code Documentation](https://www.julia-vscode.org/docs/dev/gettingstarted/#Installation-and-Configuration-1). More advanced features are at the YouTube video [Package Development in VSCode](https://www.youtube.com/watch?v=F1R3ETaRQXY)

# Hello World #
We make a new file with
```bash
touch hello.jl
```

Adding the code

```julia
f(x) = x + 1
```
And hitting `Shift + Enter` automatically creates a new REPL and runs the line in it

Like in `R-Studio` we can now access our function $f$ in the .jl file or directly from the REPL

Adding
```julia
f(2)
```
And hitting `Shift + Enter` sends the line to the REPL and prints
```bash
3
```

## Packages ##
VS Code typically activates the current project. You can see this by entering package mode in the integrated terminal:
```julia
]
```
will give

`(julia) pkg>`

If not, you can activate the project with

```julia
] activate .
```
And check the current package location and details with
```julia
] st
```
To add the `Plots` package, in the REPL we need
```julia
] add Plots
```
You can update a package with, for example
```julia
] up Plots
```
Or just update all packages in the current project with
```julia
] up
```
You can make a plot by sending the following lines to the REPL:
```julia
using Plots, Random
plot(1:5, rand(5))
```
The plot will open in a new pane. Alternatively, with those lines in `hello.jl` we can run the entire file in the REPL with

```julia
julia> include("hello.jl")
```

We can also do this directly in the terminal from any directory as long as we include the path to `hello.jl`. In fact we will have to do that here since `hello.jl` is in our `lecture 10` subdirectory:
```julia
julia> include("./lecture10/hello.jl")
```
Which will generate the plot in a new pane

## File Organization ##
We generally want files organized around functions rather than scripts. We'll put this into `hello_refactored.jl`:
```julia
using Plots, Random
f(x) = x + 1
function plot_results()
    x = 1:5
    y = f.(x)
    plot(x,y)
    print(y)
end

# execute main function
plot_results()
```
Organizing our code in functions lets the compiler avoid global variables and optimize the results

Some good rules to avoid poor scoping behavior:
- Never use loops outside of a function when writing a .jl file
- If you ever use the `global` keyword, assume something is wrong and you should put something in a function

## Executing a .jl file ##
In addition to the methods mentioned above, you can run a file directly from the terminal with
```bash
julia --threads auto --project hello.jl
```
Or provide the full path to `hello.jl` if it isn't in your current working directory

## Debugging in VS Code ##
Debug in VS Code by creating a breakpoint and

`Command + Shift + D`

To open the run and debug tab. VS Code has a pretty nice interface for debugging.

A quicker way to debug, assuming we've sent `hello-refactored.jl` to the REPL, is to enter

```julia
julia > @run plot_results()
```
Into the REPL

## The REPL and Package Environments ##
Read the [Julia Documentation](https://docs.julialang.org/en/v1/) for more details on the REPL and usages.

But if starting the REPL outside of VS Code within a terminal by typing `julia` in the command line, you'll want to use the `--project` option to either activate an existing project or start a new one if none exists.

If you are in the REPL and *haven't* activated a project, you can do so with either

```julia
] activate .
```
Or
```julia
using Pkg; Pkg.activate()
```
We can avoid this by either using VS Code or adding the `--project` flag when entering the REPL:

```bash
julia --threads auto --project
```

If you are reproducing an existing project, say one cloned from GitHub, you need to make sure you have all the necessary packages installed from the existing `Project.toml` and `Manifest.toml` files.

You do this with either

```julia
] instantiate
```

Or
```julia
using Pkg; Pkg.instantiate()
```
You can always add packages as you go. To add the `Expectations` package to the existing project,

```julia
] add Expectations
```

And you can remove it with

```
] rm Expectations
```

# VS Code Settings #
I changed the font to [Cascadia Code](https://github.com/microsoft/cascadia-code?tab=readme-ov-file) with ligatures following [these instructions](https://techstacker.com/change-vscode-code-font/)
