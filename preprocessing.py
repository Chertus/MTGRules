import re

def extract_rules(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the document into sections based on headings
    sections = re.split(r'\n\d+\.\s', content)[1:]  # Skip the first split which is before the first rule

    rules = []
    for section in sections:
        # Each section might start with the rule number, remove it
        rule_body = re.sub(r'^\d+(\.\d+)*\s', '', section).strip()
        rule_number = section.split('.')[0].strip()
        # You might want to further process each rule_body to extract specific rules or subrules
        rules.append((rule_number, rule_body))
    
    return rules

def main():
    filename = 'D:/Projects/MTGRulesBot/mtg-ml-env/MagicCompRules_20240206.txt'
    rules = extract_rules(filename)

    # Example of how to save rules to a new file
    # Adjust this part to format questions and answers as needed
    with open('processed_rules.txt', 'w', encoding='utf-8') as out_file:
        for rule_number, rule_body in rules:
            out_file.write(f"Rule {rule_number}: {rule_body}\n\n")

if __name__ == "__main__":
    main()
