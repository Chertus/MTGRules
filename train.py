from transformers import RobertaTokenizerFast, RobertaForQuestionAnswering, TrainingArguments, Trainer
from datasets import load_dataset

def main():
    # Specify paths to your dataset files
    train_dataset_path = 'D:/Projects/MTGRulesBot/mtg-ml-env/MagicCompRules_train.csv'
    test_dataset_path = 'D:/Projects/MTGRulesBot/mtg-ml-env/MagicCompRules_test.csv'

    # Load datasets
    train_dataset = load_dataset('csv', data_files=train_dataset_path, split='train')
    test_dataset = load_dataset('csv', data_files=test_dataset_path, split='train')

    # Initialize the tokenizer
    tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base')

    # Tokenize the datasets
    def tokenize_function(examples):
        return tokenizer(examples['context'], examples['question'], truncation=True, padding='max_length', max_length=512)

    tokenized_train_dataset = train_dataset.map(tokenize_function, batched=True)
    tokenized_test_dataset = test_dataset.map(tokenize_function, batched=True)

    # Initialize the model
    model = RobertaForQuestionAnswering.from_pretrained('roberta-base')

    # Training arguments
    training_args = TrainingArguments(
        output_dir='D:/Projects/MTGRulesBot/mtg-ml-env/TrainedRules',
        num_train_epochs=3,
        per_device_train_batch_size=8,
        evaluation_strategy='epoch',
        save_strategy='epoch',
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_test_dataset,
        tokenizer=tokenizer,
    )

    # Train the model
    trainer.train()

if __name__ == '__main__':
    main()
