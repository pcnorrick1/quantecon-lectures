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
## Using Jupyter in VS Code ##
You can create or open a `.ipynb` file in VS Code directly as long as you have the Jupyter and Julia extensions.

You will need to select the `Julia` kernel. You can just use the UI or by keyboard:

```bash
Cmd + Shift + P # Open Command Palette
Jupyter: Select Kernel
```
And then use the arrow keys to chose the Julia 1.11 (or 1.xx) kernel from the list

# Julia in Neovim #
I have set up `neovim` to integrate with `tmux` and `vim-slime` to provide an IDE-like environment. If you're curious you can look at my [dotfiles repo](https://github.com/pcnorrick1/dotfiles/tree/main/nvim)

## Starting a REPL ##

1) Launch a tmux session
```bash
tmux new -s test-session
```
Inside tmux:
Split a narrow right column (this will hold the REPL)

```
ctrl-b |
```
(Optional): make left pane ~70% width:
```css
ctrl-b L (repeat a few times) # capital L resizes right; capital H resizes left
```
2) Create or cd into your project in the left pane and open nvim

```bash
cd ~/academia/projects/example-project

nvim .
```

3) Create files in neovim:

`example.jl`
```julia
using Statistics
vals = [1,4,9,16]
out = sqrt.(vals)
println("jl ok: ", out, " | mean=", mean(out))
```

4) Start REPL

Move to the right pane (`ctrl-l`) and create the appropriate REPL:

```bash
julia
```

5) Wire Neovim -> REPL with vim-slime

Vim-slime is already set to target tmux in my config. First time only, tell slime which pane to send it to.

In **Neovim**:

```lua
:SlimeConfig
```
Follow the prompts:
 - **Socket name**: Usually press `Enter` (default).
 - **tmux target**: e.g., `:2.1` (window 2, pane 1) or similar -- slime shows hints in the prompt.
 (A quick way to see pane numbers: in any tmux pane run `tmux display -p `#S:#I.#P'.)

To **send code**: select lines in Visual mode or place the cursor on a line and press `ctrl-c ctrl-c`

You can send the whole file with:

```
ggVG (select all)
ctrl-c ctrl-c
```
Alternatively I've set up some shortcuts:
```lua
<leader>ss -- sends current line to REPL
<leader>sp -- sends selection to REPL
<leader>sf -- sends file to REPL
```
Once a pane is pinned with `:SlimeConfig`, slime remembers it for that buffer. You can also `:SlimeConfig` again if you rearrange panes

## Package Management ##
Inside this REPL we can manage packages as usual:

```julia
] add IJulia
```
## Formatting ##
I have my Language server managed automatically by Mason:
 - Julia -> `julials`
Neovim provides completion, hover help, and diagnostics through `nvim-cmp` and `lspconfig`

I still need to set up proper debugging, linting, profiling, etc. in neovim

## Jupyter in Neovim ##
I'm still experimenting with how this works. For now here's what I've got

You can still launch JupyterLab from any directory:
```bash
jupyter lab # this starts the same Jupyter server used by VS Code
```
You can view and run notebooks in the browser while editing their paired script files (`.jl`) in Neovim.

One time install:
```bash
pipx install jupytext # makes it available globally
```
### Converting Betweeen Notebooks and Scripts ###
Because jupytext is available globally we can pair any notebook with a script:
```bash
jupytext --set-formats ipynb,jl:percent mynotebook.ipynb
```
Now edits made in Neovim (the `.jl`) file automatically sync when you open or save the notebook in JupyterLab.

You can edit `mynotebook.jl` in Neovim (cells are #%%), send cells to the REPL via vim-slime, and sync to `.ipynb` when you need a notebook with 
```bash
jupytext --sync mynotebook.ipynb
```

You can also convert one-off files:

```bash
jupytext --to notebook myscript.jl # .jl -> .ipynb
jupytext --to jl mynotebook.ipynb # .ipynb -> .jl
```
