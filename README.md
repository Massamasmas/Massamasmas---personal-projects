# Personal Projects Repository

This repository contains a collection of personal Python projects and utility scripts.

## Repository Structure

```
projects/
├── random_useful_scripts/     # Collection of utility Python scripts
├── worst-wordle-score/       # a project aiming to find the worst possible wordle score
└── .vscode/                  # VS Code configuration files
```

## Projects Overview

### Random Useful Scripts (`random_useful_scripts/`)

A collection of utility scripts for common string and list manipulation tasks:

- **`String_List_Converter.py`**
- Converts space-separated strings into Python lists
  - Takes a single string with space-separated items
  - Outputs a properly formatted Python list
  - Example: "Test1 Test2 Test3" → ['Test1', 'Test2', 'Test3']

- **`String_List_Organizer.py`**
- Formats Python lists into multi-column string output
  - Takes a list of strings and formats them into multi-column layout
  - Configurable column count (default: 5 columns)
  - Outputs formatted strings ready for copy-paste into code
  - Handles proper quoting and line breaks for code integration

- **`txt_to_string.py`**
- Converts text files to Python string literals
  - Command-line tool that reads any text file
  - Converts file content to a properly escaped Python string literal
  - Supports UTF-8 encoding and handles special characters
  - Can accept file path as argument or prompt for input

### Worst Wordle Score (`worst-wordle-score/`)

A project aimed at finding the worst possible Wordle starting word through comprehensive analysis:

- **`NYTimesOfficialWordlist.py`**
- NY Times Wordle answer words (464 words)
  - Contains the complete list of official Wordle  words
  - Formatted as a Python list (`nyTimesWordList`) for analysis

- **`AnswersList.py`** 
-  Wordle answers list (1853 words)
  - comprehensive list of Wordle answer words sourced from 
  https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b#file-wordle-answers-alphabetical-txt
  - Formatted as a Python list (`answersList`) for analysis

- **`ValidGuessList.py`** - Complete Wordle valid guesses database
  - comprehensive (10,657 words) list of Wordle valid guess words sourced from 
  https://gist.github.com/cfreshman/cdcdf777450c5b5301e439061d29694c#file-wordle-allowed-guesses-txt
  - Split into multiple lists for memory management
  - Includes words that can be guessed but may not be answers
  - Essential for analyzing all possible guess strategies

- **`WordLists/`** - Organized word data in both Python and text formats
  - Backup and alternative formats of all word lists
  - Separate files for answers and valid guesses
  - Multiple formats for different analysis tools

## Getting Started

### Prerequisites

- Python 3.x
- Any Python IDE or text editor (VS Code configuration included)

### Usage

Each script is self-contained and can be run directly:

```bash
# Run utility scripts
python random_useful_scripts/String_List_Converter.py
python random_useful_scripts/String_List_Organizer.py
python random_useful_scripts/txt_to_string.py "path/to/file.txt"

# View Wordle word lists
python worst-wordle-score/NYTimesOfficialWordlist.py
python worst-wordle-score/AnswersList.py
python worst-wordle-score/ValidGuessList.py
```

### Example Usage

#### String List Converter
Input string:
```python
"Test1 Test2 Test3 Test4 Test5"
```
Output:
```python
['Test1', 'Test2', 'Test3', 'Test4', 'Test5']
```

#### String List Organizer
Input list:
```python
inputList = ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10"]
n = 5  # Number of columns
```
Formatted output:
```
Test1", "Test2", "Test3", "Test4", "Test5"
"Test6", "Test7", "Test8", "Test9", "Test10
```

#### Text to String Converter
```bash
python txt_to_string.py "myfile.txt"
```
Converts file content to escaped Python string literal.

## Development Environment

This repository includes VS Code configuration with:
- Custom settings for Python development
- Launch configurations for debugging

## Recent Updates

- Expanded Wordle project with comprehensive word lists (12,947+ valid guesses, 464 answers)
- Added ValidGuessList.py with complete Wordle vocabulary for analysis
- Created txt_to_string.py utility for converting text files to Python literals
- Enhanced String_List_Converter.py for space-separated string processing
- Organized word lists into structured directories with multiple formats
- Updated project structure for better code organization and analysis capabilities

## Contributing

This is a personal repository, please don't mess with it unless you are me, or have been given explicit permission by me to work on the main. You can fork if you'd like, but don't merge it into the main repo.

## License

Copyright <2025> <Sammuel Majewski>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.