# QuantEcon Lectures - My Workthrough

This repository is my personal workspace for solutions, tests, and notes while working through the [QuantEcon Lectures](https://quantecon.org/lectures/) from Thomas J. Sargent and John Stachurski.

It contains separate environments for **Julia** and **Python** versions of the lectures, as well as my own notes and exercises.

---

## Layout

```
quantecon_lectures/
|--julia/
   |--notebooks/ # (submodule) QuantEcon Julia lecture notebooks
|--python/
   |--notebooks/ # (submodule) QuantEcon Python lecture notebooks
|--README.md # this file

```

---

## Submodules

The official lecture notebooks are tracked as git submodules:

- Julia notebooks: `julia/notebooks`
- Python notebooks: `python/notebooks`

To clone this repository **with submodules**:

```bash
git clone --recurse-submodules git@github.com:pcnorrick1/quantecon_lectures.git
```

If you already cloned without submodules, initialize them with:

```bash
git submodule update --init --recursive
```

To update submodules later:

```bash
git submodule update --remote --merge
```

---

## Notes

- Each language has its own README with setup instructions.
- This repo is for **personal learning and exercises** - not a replacement for the official QuantEcon repos or website.
