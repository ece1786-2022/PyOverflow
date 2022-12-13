# PyOverflow

The project files and folders are as follows:


* `Data` - Contains the data used for training and testing
* `models` - Contains the trained models
* `scraping_docs` - Contains the scripts used to scrape the documentation of Python
* `CNN_baseline_multiclass.ipynb` - The baseline CNN model for multiclass classification
* `data_combiner.ipynb` - Combines the data from the 4 labels into one csv for both train and test datasets
* `data_processing.ipynb` - Data processing for training data
* `gpt-2-training.ipynb` - Training the GPT-2 model
* `requirements.txt` - The required packages
* `test_data_processing.ipynb` - Data processing for test data
* `test_maker.ipynb` - Creates the test dataset from the stackoverflow data dump

# Instructions for replication

## Requirements:
* Python 3.9 and all the required packages are in the `requirements.txt` file

## Running everything from scratch:
The files are run in the following order:
1. `scraping_docs/*.py` - to scrape the documentation of Python
2. `data_processing.ipynb` - to process the training data
3. `data_combiner.ipynb` - to combine the data from the 4 labels into one csv for both train and test datasets
4. `test_maker.ipynb` - to create the test dataset from the stackoverflow data dump
5. `test_data_processing.ipynb` - to process the test data
6. `gpt-2-training.ipynb` - to train the GPT-2 model
7. `CNN_baseline_multiclass.ipynb` - to train the baseline CNN model

## Using the trained models:
The trained models are available in the `models` folder. The `CNN_baseline_multiclass.ipynb` file can be run to test the baseline CNN model. The `gpt-2-training.ipynb` file can be run to test the GPT-2 model.