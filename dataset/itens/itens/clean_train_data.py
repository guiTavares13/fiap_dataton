import pandas as pd
import os

input_folder = './'
output_folder = './filtered_output'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each .csv file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.csv'):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, "filtered_" + file_name)

        # Read the CSV file
        df = pd.read_csv(input_file)

        # Remove the specified columns if they exist
        columns_to_remove = ["body", "caption", "title"]
        for column in columns_to_remove:
            if column in df.columns:
                df = df.drop(columns=[column])

        # Create a new column "article-type"
        if "url" in df.columns:
            df['article-type'] = df['url'].str.extract(r'//g1\.globo\.com/(.*?)/noticia', expand=False)
            df['article-type'] = df['article-type'].str.replace('/', '-', regex=False)

        # Save the filtered CSV to the output folder
        df.to_csv(output_file, index=False)
        print(f"Processed and saved: {output_file}")

print("All files processed!")