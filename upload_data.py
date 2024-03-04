from pymongo.mongo_client import MongoClient
import pandas as pd
import json
import logging
from src.logger import LOG_FILE_PATH  

# Set up logging using the configured log file path
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Uniform Resource Identifier (URI)
uri = "mongodb+srv://adi:aditya1@cluster0.vrfaboe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Define database name and collection name
DATABASE_NAME = "Credit-Card-Fraud-Detection"
COLLECTION_NAME = "Credit-Cards-Data"

# Read the data from CSV file into a DataFrame
df = pd.read_csv(r"D:\ML PROJECT\Credit Card Fault Detection\notebooks\output.csv")

# Convert the data into JSON format
json_record = list(json.loads(df.T.to_json()).values())

try:
    # Insert the data into the MongoDB collection
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    logging.info("All data has been successfully uploaded to MongoDB.")
    print("All data has been successfully uploaded to MongoDB.")
except Exception as e:
    # Log the error if data insertion fails
    logging.error(f"Error occurred while uploading data to MongoDB: {e}")
