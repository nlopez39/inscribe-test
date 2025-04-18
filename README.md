# Rick and Morty Character Info CSV Generator

Inscribe AI Customer Engineer Exercise Part 1 - CSV Generator

## Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the Code](#run-the-code)
- [Resources](#resources)
- [License](#License)

## Introduction

Use this Python application to fetch and process data from the **Rick and Morty API**, and generate a CSV file containing information about characters from the show. The CSV file will include each character’s:

- Name

- Status (Alive, Dead, or Unknown)

- Species

- Origin Location Name

- Last Known Location Name

Enjoy!

## Prerequisites

Install Python 3

1. **MacOS**
   <p>Install Python using Homebrew:</p>

   ```
   brew install python
   ```

   Or download from the official site [Download Python 3](https://www.python.org/downloads/)

2. **Windows**
   <p>Install from the official site:</p>

   [Download Python 3](https://www.python.org/downloads/)

3. **Linux**
   <p>Install via package manager:<p>

   ```
   sudo apt update
   sudo apt install python3 python3-pip
   ```

4. **Verify Install**

   ```
   python3 --version
   pip3 --version
   ```

## Installation

1. Clone the repository

   [Instructions on how to clone a repository from Github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

2. Create and activate a virtual environment (recommended for Homebrew Python users):

   ```
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows

   ```

3. **Install Dependencies**

   ```
   pip install -r requirements.txt
   ```

   Note: Using a virtual environment is recommended for users with Homebrew-installed Python to avoid potential conflicts with system-wide packages.

## Run the Code

1. Run the main script using:

   ```
   python main.py
   ```

2. A CSV file named `character.csv` will be generated in the project folder

## Resources

https://dev.to/bearer/sort-filter-and-remap-api-data-in-python-5i

https://stackoverflow.com/questions/61977076/how-to-fetch-data-from-api-using-python

https://www.w3schools.com/python/python_json.asp

https://stackoverflow.com/questions/61977076/how-to-fetch-data-from-api-using-python

https://pypi.org/project/requests/

https://rickandmortyapi.com/documentation/#filter-characters

https://stackoverflow.com/questions/67943578/python-and-api-output-to-csv

## Licenese

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project utilizes the standard MIT License.
