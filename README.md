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

I spent around 3 hours on this, +/- 15 minutes.

Ruby is my main language, and I have some familiarity with python but
I'm sure there are some python conventions I might not be quite
be adhering to in this project. The biggest thing that some extra time
could provide is for me to learn some of those conventions and make
sure I'm not doing anything to weird.


Beyond that, here's a few things I would definitely do with more time:

- Add a code linter for style checking (I'm sure this would help me with conventions)
- Figue out how to get my tests to do relative imports of the class under
test without needing the sys.path.append append trick I found on Google
- Write some tests for main.py. Testing while using stdin an stdout
seems tricky, but a refactor would probably help with this
- Add malfromed input handling. The project prompt said not to worry
about this, so I didn't
- Make it easier to run without piping input
