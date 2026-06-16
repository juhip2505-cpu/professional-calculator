# Professional Calculator

A professional command-line calculator application built with Python using object-oriented programming principles.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Calculation history
- Help command
- Exit command
- Input validation
- Error handling
- CalculationFactory implementation
- REPL interface

## Project Structure

```
app/
├── calculator/
├── calculation/
├── operation/

tests/
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python3 main.py
```

Run tests:

```bash
pytest --cov=app tests/
```

## Test Coverage

This project achieves 100% test coverage using:

- pytest
- pytest-cov

## Commands

- add
- subtract
- multiply
- divide
- history
- help
- exit