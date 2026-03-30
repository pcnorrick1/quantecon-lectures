## QuantEcon Lectures - Python

This folder contains my work through the [QuantEcon lectures in Python](https://quantecon.org/lectures/)

Unlike the Julia lectures, QuantEcon has several "courses" for Python. I will use separate folders for each

The first one is called "Python Programming for Economics and Finance"

---

## Layout

```
python/
|--notebooks/ # (submodule) official QuantEcon Python lecture notebooks
|--python-programming-for-econoimcs-and-finance
    |--lecture1/ # notes and exercises from lecture1
        |--exercise1.py # exercise 1 (if applicable)
        |--notes.md
    |--lecture2/
    |--shared/ # utility code shared across lectures
    |--README.md
|--a-first-course-in-quantitative-economics-with-python
|--intermediate-quantitative-economics-with-python
|--README.md # this file
```
---

## Setup

Note that I am using the `anaconda` distribution of Python

1. Create / activate a conda environment (`quantecon` in my case)
2. Install Python packages into the environment as needed
3. Install VS Code along with the **Python** and **Jupyter** extensions

A typical setup looks like:

```bash
# Only need to do once
conda create -n quantecon python=3.12
conda activate quantecon
conda install numpy scipy pandas matplotlib quantecon
```

---

# Workflow

Typical steps to work through a lecture:

1. Open VS Code inside the `python/` folder and appropriate sub-folder
2. Create or edit a `.py` file from the correct `lectureN/` folder or open a notebook
3. Make sure VS Code is using the correct interpreter (should be the conda environment (`quantecon`)): `Cmd+Shift+P` -> `Python: Select Interpreter`
4. Run code either:
 - in a script with `python file.py` in the integrated terminal
    * `which python` in the integrated terminal will point to the conda environment: `/opt/anaconda3/envs/quantecon/bin/python`
 - interactively in VS Code with `Shift + Enter`
 - directly in a notebook

 ---

 ## Using Notebooks

 Open notebooks directly from `python/notebooks`

 Use the conda environment (`quantecon`) and make sure the notebook kernel is set to **Python (quantecon)**

 If launching Jupyter manually from the terminal:
 ```bash
 conda activate quantecon
 jupyter lab
 ```
 Then open the notebooks and select the correct Python kernel

 In VS Code, just open the notebook directly and choose the `Python (quantecon)` kernel

## Experimenting with notebooks
Copy from the submodule into your own `lectureN/` folder, e.g.:
```bash
cp notebooks/lecture5/some.ipynb lecture5/my_experiment.ipynb
```
This way, the submodule stays clean

---

## Updating Notebooks

The official notebooks live in the `notebooks/` submodule. To update them:

```bash
git submodule update --remote --merge
```
And then commit the change:

```bash
git add python/notebooks
git commit -m "Update Python notebooks submodule"
git push origin main
```

---

## Submodule Cleanup
Submodules should be treated as **read-only**.
If you see stray changes inside `python/notebooks` (e.g. `.log` files):

```bash
cd python/notebooks
git reset --hard HEAD
```
Back in the main repo, commit only when you actually want to move the submodule pointer.

---

## Notes

- My work should stay in `exercises/` or `notes.md` - the official notebooks should not be modified.
- If I want to experiment, I'll copy a notebook into the relevant `lectureN/` folder and edit that version.

