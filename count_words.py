import pandas as pd
from collections import Counter

# Path to the epigraphs file
epigraphs_file = "/Users/enochngan/Downloads/nora_roberts_linreg_copy/epigraphs.csv"

# Read the epigraphs file into a dataframe
epigraphs_df = pd.read_csv(epigraphs_file)

# Split words from the 'Epigraph' column and convert to lowercase
epigraph_words = epigraphs_df['Epigraph'].dropna().str.split().explode().str.lower()

# Count the occurrences of each word
word_counts = Counter(epigraph_words)

# Create a DataFrame with words and total counts
word_counts_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Total_Count'])

# Add columns for each theme
themes = epigraphs_df['Book Theme'].unique()
for theme in themes:
    # Filter rows for the current theme
    theme_words = epigraphs_df.loc[epigraphs_df['Book Theme'] == theme, 'Epigraph'].dropna()
    theme_word_list = theme_words.str.split().explode().str.lower()
    theme_word_counts = Counter(theme_word_list)
    
    # Add a column for the current theme
    word_counts_df[theme] = word_counts_df['Word'].map(theme_word_counts).fillna(0).astype(int)

# Save the updated word counts with theme-specific columns to a new CSV file
output_file = "/Users/enochngan/Downloads/nora_roberts_linreg_copy/word_counts.csv"
word_counts_df.to_csv(output_file, index=False)

print(f"Word counts with themes saved to: {output_file}")
