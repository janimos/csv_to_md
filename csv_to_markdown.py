import csv

def csv_to_markdown(csv_file_path):
    """
    Convert CSV file to Markdown table format
    Args:
        csv_file_path (str): Path to the input CSV file
    Returns:
        str: Markdown formatted table
    """
    markdown_table = []
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            # Read headers
            headers = next(csv_reader)
            
            # Create header row with separator
            markdown_table.append('| ' + ' | '.join(headers) + ' |')
            markdown_table.append('|' + '|'.join(['---' for _ in headers]) + '|')
            
            # Add data rows
            for row in csv_reader:
                markdown_table.append('| ' + ' | '.join(row) + ' |')
                
        return '\n'.join(markdown_table)
    
    except FileNotFoundError:
        return "Error: CSV file not found"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Example usage
    input_file = 'input.csv'  # Replace with your CSV file path
    markdown_output = csv_to_markdown(input_file)
    print(markdown_output)

if __name__ == '__main__':
    main()