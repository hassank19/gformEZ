# gformEZ
An AI tool that extracts all the questions in a google form exam and displays the correct answers using Gemini, saving the time the user takes to search for the answers manually.

## Features

- Reads Google Forms
- Extracts questions
- Uses Gemini to generate answers
- User reviews answers manually

## Requirements

- Python 3.11+
- Playwright
- Gemini API Key

## Installation

```bash
pip install -r requirements.txt
playwright install
```

## Usage

```bash
python python.py
```

1. Enter your Gemini API key.
2. Enter the Google Form URL.
3. Wait for answers to be generated.
4. Review the answers.
5. Fill and submit the form manually.

## Limitations

- AI may generate incorrect answers.
- Personal information should be entered manually.
- Requires a Gemini API key.
