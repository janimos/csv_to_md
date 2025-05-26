import sys
import os
import pandas as pd

def csv_to_markdown(csv_file_path, encoding='utf-8', separator=','):
    """
    Reads a delimited file with a specified encoding and separator,
    and converts its content to a Markdown table string.

    Args:
        csv_file_path (str): The path to the input CSV file.
        encoding (str): The encoding of the input file (e.g., 'utf-8', 'cp1257').
                        Defaults to 'utf-8'.
        separator (str): The delimiter used in the input file (e.g., ',', ';').
                         Defaults to ','.

    Returns:
        str: A string containing the Markdown table representation of the data,
             or an error message if the file cannot be read or processed.
    """
    try:
        # Specify the separator when reading the CSV
        df = pd.read_csv(csv_file_path, encoding=encoding, sep=separator)

        # Convert the DataFrame to a Markdown table string
        markdown_table = df.to_markdown(index=False)
        return markdown_table

    except FileNotFoundError:
        return f"Error: File not found at '{csv_file_path}'"
    except UnicodeDecodeError:
        return f"Error: Could not decode the file with encoding '{encoding}'. Please check the file encoding."
    except Exception as e:
        return f"Error processing file: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python your_script_name.py <path_to_csv_file> [encoding] [separator]")
        print("  [encoding]: Optional. The encoding of the input file (e.g., 'cp1257'). Defaults to 'utf-8'.")
        print("  [separator]: Optional. The delimiter used in the input file (e.g., ';'). Defaults to ','.")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = 'output.md'
    file_encoding = 'utf-8'  # Default encoding
    file_separator = ','   # Default separator

    # Check for optional encoding argument
    if len(sys.argv) > 2:
        file_encoding = sys.argv[2]

    # Check for optional separator argument
    if len(sys.argv) > 3:
        file_separator = sys.argv[3]

    print(f"Processing file: {input_file_path} with encoding: {file_encoding} and separator: '{file_separator}'")

    markdown_output = csv_to_markdown(input_file_path, encoding=file_encoding, separator=file_separator)

    if markdown_output.startswith("Error:"):
        print(markdown_output)
    else:
        try:
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_output)
            print(f"Successfully wrote Markdown output to '{output_file_path}'")
        except Exception as e:
            print(f"Error writing to output file '{output_file_path}': {e}")

if __name__ == '__main__':
    main()
