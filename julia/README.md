# Julia QuantEcon Lectures

This folder contains my work through the [QuantEcon lectures in Julia](https://julia.quantecon.org/).

---

## Layout

```
julia/
|--notebooks/ # (submodule) official QuantEcon Julia lecture notebooks
|--lecture1/ # notes and exercises from lecture1
   |--exercise1.jl # exercise 1 (if applicable)
   |--notes.md
|--lecture2/
|--shared/ # utility code shared across lectures
|--README.md # this file
```

---

## Setup

1. **Install Julia** (via [Juliaup](https://github.com/JuliaLang/juliaup) is recommended).
2. Ensure Julia is on your PATH (so you can type `julia` in a terminal).
3. Install [VS Code](https://code.visualstudio.com/) and the Julia extension.

---

## Workflow

Typical steps to work through a lecture:

1. Open VS Code inside the `julia/` folder.
2. Open a `.jl` file from `exercises/` or a notebook from `notebooks/`.
3. Start the Julia REPL inside VS Code (`Ctrl+Shift+P` → “Start REPL”).
4. Run code with `Shift+Enter` (sends to REPL) or run an entire script with `include("file.jl")`.

---

## Updating Notebooks

The official notebooks live in the `notebooks/` submodule. To update them:

```bash
git submodule update --remote --merge
```
And then commit the change:

```bash
git add julia/notebooks
git commit -m "Update Julia notebooks submodule"
git push origin main
```

---

## Notes

- My work should stay in `exercises/` or `notes.md` - the official notebooks should not be modified.
- If I want to experiment, I'll copy a notebook into the relevant `lectureN/` folder and edit that version.
