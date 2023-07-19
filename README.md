# Soccer Challenge

A command-line application that calculates the ranking table for
a soccer league.

## Running Locally

First, set up a virtual environment. Assuming you have python3
installed already, just run:

```bash
python3 -m venv myenv
```

Next, activate the virtual environment. On Mac OS, run:

```bash
source myenv/bin/activate
```

Finally, use `pip` to install the dependencies:

```bash
pip install -r requirements.txt
```

You can now run the program with:

```bash
cat sample-input.txt | python3 main.py
```

This repository contains the needed `sample-input.txt` file, but
you're welcome to test on another filename.

## Running Tests

If you've already set up a virtual environment and installed
dependencies as descriped in the "Running Locally" section,
then you can run the entire test suite with:

```bash
pytest
```

You can run an individual test file by providing the relative path:

```bash
pytest tests/test_league.py
```

## List of Improvements

TODO:
