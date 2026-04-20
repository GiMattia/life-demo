# life-demo

A tiny Conway's Game of Life project used for a live tutorial on modern Python development practices.

This is the **`start` branch**: the project already works, but it is intentionally still rough. The goal of the tutorial is to clone it, run it, inspect it, and improve it step by step.

---

## What this project does

- simulates Conway’s Game of Life in the terminal
- runs for a fixed number of steps
- keeps the code small enough to understand and modify during a live session

This repository is meant to be **developed**, not just executed once.

---

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

---

## Getting started

Clone the repository, move into it, and sync the environment:

```bash
git clone https://github.com/GiMattia/life-demo.git
cd life-demo
uv sync --group test
```

---

## Run and test

You shall write on the terminal the command

```bash
life-demo
```

to run the executable.
To test, you shall write the command

```bash
pytest
```

## Requirements

This is not meant to be a polished branch. Instead, it provides a safe starting point to explore, modify, and improve the code during the tutorial.