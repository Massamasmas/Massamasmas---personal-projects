# Personal Projects Repository

This repository contains a collection of personal Python projects and utility scripts.

## Repository Structure

```
projects/
├── random_useful_scripts/     # Collection of utility Python scripts
├── worst-wordle-score/       # 
a project aiming to find the worst possible wordle
└── .vscode/                  # VS Code configuration files
```

## Projects Overview

### 🔧 Random Useful Scripts (`random_useful_scripts/`)

A collection of utility scripts for common string and list manipulation tasks:

- **`String_List_Converter.py`** - Converts input strings into formatted output lists
- **`String_List_Organizer.py`** - Organizes and formats lists for code integration
  - Takes a list of strings and formats them into multi-column output
  - Configurable column count (default: 5 columns)
  - Outputs formatted strings ready for copy-paste into code
  - Handles proper quoting and line breaks

### 🎯 Worst Wordle Score (`worst-wordle-score/`)

Tools and resources related to Wordle word analysis:

- **`NYTimesOfficialWordlist.py`** - Complete New York Times Wordle official word list
  - Contains 464 official Wordle words
  - Formatted as a Python list for easy integration
  - Clean, ready-to-use dataset for Wordle analysis

## Getting Started

### Prerequisites

- Python 3.x
- Any Python IDE or text editor (VS Code configuration included)

### Usage

Each script is self-contained and can be run directly:

```bash
python random_useful_scripts/String_List_Organizer.py
python worst-wordle-score/NYTimesOfficialWordlist.py
```

### Example Usage - String List Organizer

Input:
```python
inputList = ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10"]
n = 5  # Number of columns
```

Output:
```
Test1", "Test2", "Test3", "Test4", "Test5"
"Test6", "Test7", "Test8", "Test9", "Test10
```

## Development Environment

This repository includes VS Code configuration with:
- Custom settings for Python development
- Launch configurations for debugging

## Recent Updates

- Modified NYTimesOfficialWordlist to contain only the word list data
- Added several utility scripts for string/list manipulation
- Organized projects into logical subdirectories

## Contributing

This is a personal repository, please don't mess with it unless you are me, or have been given explicit permission by me to work on the main. You can fork if you'd like, but don't merge it into the main repo.

## License

Copyright <2025> <Sammuel Majewski>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.