# ReplaceInAllRows

## Description

ReplaceInAllRows is a Python program designed to replace a set of literals in all given rows. It is lightweight, efficient, and easy to use for text processing tasks.

This program was made to automate text processing heavy tasks in a parameterized environment where there is a need to replace values regularly. ReplaceInAllRows was specifically designed to **rapidly copying and pasting data from tables or spreadsheets into the input files**, hence the lack of a delimiter in the replacements.txt file, which limits the usage of whitespaces. More details in the Usage and Know Issues sections.

## Features

- Replaces multiple literals in every row simultaneously.
- Supports both replacements and deletions.
- Supports cleanup by giving both the option to collapse consecutive delimiters and to clean delimiters at the beginning and end of the rows.
- Does not modify the original files, allowing users to review the applied changes if needed.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/clamor/ReplaceInAllRows.git
    ```
2. Navigate to the project directory:
    ```
    cd ReplaceInAllRows
    ```
    
## Usage

Add the rows where you want to apply changes to the input.txt file.

Add the changes you want to make to the replacements.txt file. This program support deletion by leaving a blank space after the old value.

Run the program with the following command:
```
python replaceinallrows.py
```

### Command-line options

- `-c` : Collapses consecutive delimiters into a single one.
- `-r` : Removes any delimiter found at the beginning and end of each row.

### Example

Input file:
```
# Every match from the OLD_VALUE column will be replaced in ALL of the following lines
This is     a test
Saying test is like saying example
1111 2222 3333 4444
;11111;234;567;hi;;;done;
testing|some||delimiters|
```

Replacements file:
```
# OLD_VALUE    NEW_VALUE (Leave empty for deletions)
test    example
1111 7777
234 
```

Command:
```
python replaceinallrows.py -c -r
```

Output file:
```
This is     a example
Saying example is like saying example
7777 2222 3333 4444
77771;567;hi;done
exampleing|some|delimiters
```

## Known Issues

- Replacement of strings involving whitespaces is not supported.
- Only supports the following delimiters: 
        ```
        -_.:,;/|\?&@#%^*!~()[]
        ```
- No support for custom input or replacement files via command arguments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
