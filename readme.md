# Playwright Practice Project

This project is a practice setup for using Playwright with Python. It includes various dependencies and tools to help automate and test web applications.

## Cloning the Repository

To clone this repository, use the following command:

```bash
git clone https://github.com/your-username/Playwright_practice.git
cd Playwright_practice
```

## Requirements

The project dependencies are listed in the `requirements.txt` file. To install them, you can use the following command:

```bash
pip install -r requirements.txt
```

## Dependencies

The project uses the following main dependencies:

- `colorama==0.4.6`
- `greenlet==3.1.1`
- `iniconfig==2.0.0`
- `MouseInfo==0.1.3`
- `packaging==24.2`
- `playwright==1.50.0`
- `pluggy==1.5.0`
- `PyAutoGUI==0.9.54`
- `pyee==12.1.1`
- `PyGetWindow==0.0.9`
- `PyMsgBox==1.0.9`
- `pyperclip==1.9.0`
- `PyRect==0.2.0`
- `PyScreeze==1.0.1`
- `pytest==8.3.5`
- `pytweening==1.2.0`
- `typing_extensions==4.12.2`

## Usage

To run the Playwright tests, you can use the following command:

```bash
pytest test_automation_playground.py
```

Make sure you have the necessary browsers installed for Playwright. You can install them using:

```bash
playwright install
```

## Project Structure

- `test_automation_playground.py`: Contains the Playwright test scripts.
- `conftest.py`: Contains the pytest fixtures for setting up and tearing down Playwright sessions.
- `session.py`: Defines the `PlaywrightSession` class used to manage Playwright sessions, allowing all test runs to occur in the same window without closing, except when the session ends.

