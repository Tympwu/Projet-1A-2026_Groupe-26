# Projet 1A 2025-2026

## Goal

This student project aims to provide an interactive way to visualize sports statistics and enable users to easily access and explore data related to athletes, teams, matches, and other sports entities.

## Usage

Install the necessary dependencies listed in `requirements.txt`

Run the CLI app with `python __main__.py`

## Usage

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt

## Test

Depending on your installation, run one of these commands:
`python -m pytest --cov`
`conda run pytest --cov`
`pytest --cov`

##Features
  - Importing and processing databases
  - Data parsing and normalization
  - Statistical analysis and data exploration
  - Interactive menu-based navigation
  - Object-oriented data management

# Project's Architecture
Projet-1A-2026_Groupe-26/             
├── data/
├── src/
│   ├── __init__.py
│   ├── Analysis/
│   ├── DAO/
│   ├── Menus/
│   ├── Model/
│   └── Parsers/
├── tests/
│   ├── __init__.py
│   ├── Analysis/
│   ├── Common/
│   ├── DAO/
│   ├── Model/
│   └── Parser/
├── __main__.py
├── .gitignore
├── AUTHOR.md
├── README.md
└── requirements.txt


# Notes for students

Miscellaneous things of note and advice for your project

- The code and its documentation are in English! This will have you practice a bit, English is key in IT. You may code in English or French (Or another language if you're _really_ adventurous), but do not mix them: Choose one and stick with it throughout the project.

- There's an `__init__.py` in every folder. They can be used for more advanced stuff, but you'll notice in that case that they're all empty; they're mostly here to ensure the Python compiler recognizes the contents of the folder as a **package** and is able to import them

- This project features the three "modes" of data analysis:

  - The analysis with helpers libraries (here, `pandas`) with a Jupyter Notebook
  - The analysis with helpers libraries with a CLI (`Command Line Interface`) app
  - The analysis with 'homemade' tools with the same CLI app
    - Only the third one is mandatory, you may choose between CLI and Notebook for the library-backed analysis based on your preference

- Note the sparse use of classes/objects. They're useful to pass formatted data around the app, and for display purposes with the interface; you probably won't have to use them for more than this in the context of this project. They're even less required when using `pandas`; you'll mostly pass raw data around in the form of dataframes/series.

- Pay attention to the structure of the project:
  - The sub-packages rarely import each other. They're as much as possible standalone and independent. The `__main__.py` is where everything is tied together. This helps write maintainable and easily testable code.
  - Methods that interact with the files (e.g. the readers for the `.csv` files) should never be unit-tested with real data (Think about the overhead in performance! Tests should be near-instantaneous). You'll notice test files with data that mimics the real data.
