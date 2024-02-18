import pandas as pd

# Load the dataset
file_path = 'D:/Projects/MTGRulesBot/mtg-ml-env/MagicCompRules_qa.csv'
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Information:")
df.info()

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values in each column:\n", missing_values)

# Display the first few rows of the dataset for a quick overview
print("\nFirst few rows of the dataset:")
print(df.head())

# Check for uniqueness in questions to identify potential duplicate entries
unique_questions = df['question'].nunique()
total_questions = df.shape[0]
print(f"\nUnique questions: {unique_questions} / Total questions: {total_questions}")

# It's also useful to check for any anomalies in 'answer_start' and 'context' relation
print("\nChecking for any anomalies in 'answer_start' and 'context' relation...")
for index, row in df.iterrows():
    context = row['context']
    answer = row['answer_text']
    start = row['answer_start']
    if context.find(answer) != start:
        print(f"Anomaly found at index {index}: Answer start index does not match with context.")
