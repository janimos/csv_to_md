# CSV to Markdown Table Converter

This script converts a CSV (or other delimited text file) into a Markdown table.

## Description

The Python script `csv_to_markdown.py` reads a specified delimited text file, processes its content, and outputs a Markdown formatted table to a file named `output.md` in the same directory as the script. It supports custom encodings and delimiters for the input file.

## Usage

To use the script, run it from your command line interface (CLI) using Python.

```bash
python csv_to_markdown.py <path_to_csv_file> [encoding] [separator]
```

### Arguments

*   `<path_to_csv_file>`: **Required**. The full or relative path to the input CSV or delimited text file.
*   `[encoding]`: **Optional**. The character encoding of the input file. For example, `utf-8` (default), `cp1257`, `latin1`.
*   `[separator]`: **Optional**. The delimiter character used in the input file. For example, `,` (default), `;`, `\t` (for tab).

### Output

The script will create (or overwrite) a file named `output.md` in the current working directory. This file will contain the Markdown table generated from the input file.

## Examples

1.  **Convert a comma-separated CSV file (using default encoding UTF-8):**

    ```bash
    python csv_to_markdown.py data.csv
    ```

2.  **Convert a semicolon-separated file with `cp1257` encoding:**

    ```bash
    python csv_to_markdown.py input_data.txt cp1257 ;
    ```

3.  **Convert a tab-separated file:**

    ```bash
    python csv_to_markdown.py sales_report.tsv utf-8 \t
    ```
    (Note: Depending on your shell, you might need to escape the tab character differently, e.g., `$'\t'` in bash or zsh).

## Error Handling

The script includes error handling for:
*   File not found.
*   Incorrect file encoding (UnicodeDecodeError).
*   Other general processing errors.
*   Errors during writing the output file.

Error messages will be printed to the console if any issues occur.
