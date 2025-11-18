from openai import OpenAI
import sqlite3
import numpy as np

client = OpenAI()

# TODO: load data from data folder

# Chunk text
CHUNK_SIZE = 0 # TODO: Set chunk size
chunks = [] # TODO: Split text into chunks of CHUNK_SIZE

# Create DB
conn = sqlite3.connect("vectors.db")
db = conn.cursor()

db.execute("DROP TABLE IF EXISTS chunks")

# TODO: create table
QUERY = """"""
db.execute(QUERY)

# TODO: insert chunks
# 1. Embed each chunk
# 2. Store content and embedding in DB

conn.commit()
conn.close()

print("Prepared and stored embeddings.")
