import numpy as np
import pandas as pd

def separate(string):
    """
    Splits a range string into two float values.
    
    Args:
    string (str): The range string to split, e.g., '91-100'.
    
    Returns:
    np.array: An array containing the start and end of the range as floats.
    """
    parts = string.split('-')
    return np.array([float(parts[0]), float(parts[1])])

def writer(line1, line2, line3):
    """
    Generates and saves a dataset based on the provided ranges.
    
    Args:
    line1 (str): The range string for marks.
    line2 (str): The range string for percentiles.
    line3 (str): The range string for ranks.
    
    Returns:
    pd.DataFrame: A DataFrame containing the generated data.
    """
    # Convert range strings to arrays
    marks = separate(line1)
    percentile = separate(line2)
    rank = separate(line3)
    
    # Generate evenly spaced values within the specified ranges
    marks_range = np.linspace(marks[0], marks[1], num=10, dtype=int)  # 10 values for marks
    percentile_range = np.linspace(percentile[0], percentile[1], num=10)  # 10 values for percentiles
    rank_range = np.linspace(rank[0], rank[1], num=10, dtype=int)  # 10 values for ranks

    # Create a DataFrame for the new range
    data = {
        "Marks": marks_range,
        "Percentile": percentile_range,
        "Rank": rank_range
    }
    df = pd.DataFrame(data)

    # Append to CSV file (create if not exists, without headers)
    df.to_csv('marks_percentile_rank.csv', mode='a', header=False, index=False)

    return df

# Read the range values from the text file
with open('range.txt', 'r') as file:
    lines = file.readlines()

# Extract the first three lines from the file
first_three_lines = lines[:3]

# Extract individual lines for processing
line1 = lines[0].strip() if len(lines) > 0 else ''
line2 = lines[1].strip() if len(lines) > 1 else ''
line3 = lines[2].strip() if len(lines) > 2 else ''

# Generate and save the dataset using the extracted lines
df = writer(line1, line2, line3)

# Extract and print the remaining lines (optional)
remaining_lines = lines[3:]
print('First three lines:')
for line in first_three_lines:
    print(line, end='')

# Rewrite the file with the remaining content
with open('range.txt', 'w') as file:
    file.writelines(remaining_lines)
