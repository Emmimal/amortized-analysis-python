# Amortized Analysis in Python: Build and Measure a Dynamic Array

Companion code for the tutorial
**[Amortized Analysis in Data Structures: Explained with Python](https://emitechlogic.com/amortized-analysis-in-data-structures-explained-with-python/)**
on [EmiTechLogic](https://emitechlogic.com/).

Every Python tutorial says `list.append()` is O(1), yet every so often one
`append()` copies the whole list. Both statements are true. In this project you
build a small dynamic array that counts its own work, measure its cost, and
prove with three different methods why `append()` is O(1) *amortized*. Every
claim in the tutorial is backed by a test you can run.

## What is inside

| File | What it does |
| --- | --- |
| `dynamic_array.py` | `DynamicArray`: a growable array that counts every item it copies. The growth rule is a parameter. |
| `analysis.py` | Helpers that turn the array's work into numbers: cost per append, accounting-method bank balances, and the potential method. |
| `two_stack_queue.py` | `TwoStackQueue`: a first-in, first-out queue built from two stacks, as a second amortized example. |
| `measure.py` | Prints the cost per append, the cost of the first 17 appends, how CPython's real `list` grows, and doubling vs fixed growth. |
| `test_dynamic_array.py` | Checks ordering, capacity doubling, copy counts, and error handling. |
| `test_analysis.py` | Turns the three proofs into tests: aggregate (total cost stays under 3n), accounting (a charge of 3 never runs out of credit, a charge of 2 does), and potential (amortized cost is always 3). |
| `test_two_stack_queue.py` | Checks first-in, first-out order and that each item moves at most once. |
| `requirements.txt` | The one dependency: `pytest`. |

## Requirements

- Python 3.9 or newer (tested on Python 3.13)
- `git`, to clone the project
- `pytest`, installed in the steps below

The code uses only the standard library, apart from `pytest` for the tests.

## Quick start

### 1. Clone the repository

```console
$ git clone https://github.com/Emmimal/amortized-analysis-python.git
$ cd amortized-analysis-python
```

### 2. Create and activate a virtual environment

On macOS and Linux:

```console
$ python3 -m venv venv
$ source venv/bin/activate
```

On Windows (Command Prompt):

```console
> python -m venv venv
> venv\Scripts\activate
```

On Windows (PowerShell):

```console
> python -m venv venv
> venv\Scripts\Activate.ps1
```

When the environment is active, your prompt starts with `(venv)`.

### 3. Install the dependency

```console
(venv) $ python -m pip install -r requirements.txt
```

### 4. Run the tests

```console
(venv) $ python -m pytest
```

You should see all 14 tests pass:

```text
..............                                                           [100%]
14 passed in 0.37s
```

### 5. Run the measurements

```console
(venv) $ python measure.py
```

Expected output on Python 3.13:

```text
Cost per append for a doubling array
n=     10  total cost=       25  per append=2.50
n=    100  total cost=      227  per append=2.27
n=  1,000  total cost=    2,023  per append=2.02
n=100,000  total cost=  231,071  per append=2.31

Cost of each of the first 17 appends
[1, 2, 3, 1, 5, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 17]

How CPython's list grows
len= 0 -> 56 bytes
len= 1 -> 88 bytes
len= 5 -> 120 bytes
len= 9 -> 184 bytes
len=17 -> 248 bytes
len=25 -> 312 bytes
len=33 -> 376 bytes
len=41 -> 472 bytes
len=53 -> 568 bytes

Items copied: doubling vs adding 10 slots
n=  1,000  doubling=    1,023  add 10=      49,600
n= 10,000  doubling=   16,383  add 10=   4,996,000
n=100,000  doubling=  131,071  add 10= 499,960,000
```

The third block, how CPython's list grows, depends on your Python version and
implementation, so your byte counts may differ. The other three blocks are
deterministic and should match exactly.

## What the numbers show

- **Cost per append stays flat.** From 10 to 100,000 appends, the average cost
  per append stays between 2 and 3. That is what amortized O(1) looks like.
- **Resizes are rare.** In the first 33 appends only appends 2, 3, 5, 9, 17 and
  33 cost more than 1, and the gaps between them keep doubling.
- **Growth must be geometric.** At 100,000 appends, doubling copies about 131
  thousand items, while adding a fixed 10 slots copies about 500 million.

## Try it yourself

Use the array directly in a Python session:

```pycon
>>> from dynamic_array import DynamicArray
>>> array = DynamicArray()
>>> for i in range(9):
...     array.append(i)
...
>>> len(array), array.capacity, array.copies
(9, 16, 15)
```

Nine appends copy 1 + 2 + 4 + 8 = 15 items in total. To see what happens with a
different growth rule, pass your own function:

```pycon
>>> from dynamic_array import DynamicArray
>>> fixed = DynamicArray(grow=lambda capacity: capacity + 10)
>>> for i in range(1_000):
...     fixed.append(i)
...
>>> fixed.copies
49600
```

Run a single test file, or a single test:

```console
(venv) $ python -m pytest test_analysis.py
(venv) $ python -m pytest test_analysis.py -k potential
```

## Project layout

```text
amortized-analysis-python/
├── README.md
├── requirements.txt
├── dynamic_array.py
├── analysis.py
├── two_stack_queue.py
├── measure.py
├── test_dynamic_array.py
├── test_analysis.py
└── test_two_stack_queue.py
```

All modules sit in one folder, so every import is a plain module name. Run all
commands from the project folder.

## Troubleshooting

**`ModuleNotFoundError: No module named 'dynamic_array'`**
You are running a command from the wrong folder. Run `cd amortized-analysis-python`
first, then run the command again.

**`No module named pytest`**
The virtual environment is not active, or the dependency is not installed.
Activate the environment (step 2), then run
`python -m pip install -r requirements.txt`.

**`python: command not found`**
On some systems the command is `python3`. Use `python3` in place of `python`
for the commands above.

**PowerShell refuses to run `Activate.ps1`**
Run PowerShell as your normal user and allow scripts for this session with
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`, or use
Command Prompt instead.

**The CPython growth numbers differ from the README**
That is expected. List growth is an implementation detail and can differ
between Python versions and between implementations such as PyPy.

## Read the full tutorial

The step-by-step explanation behind this code, including the three proofs, the
two-stack queue, and when amortized O(1) is not enough, is in the article:

[Amortized Analysis in Data Structures: Explained with Python](https://emitechlogic.com/amortized-analysis-in-data-structures-explained-with-python/)

## Author

Written by Emmimal P Alexander at [EmiTechLogic](https://emitechlogic.com/). 
