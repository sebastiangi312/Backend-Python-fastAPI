# CSV Upload REST API with MongoDB

This project is a REST API that accepts CSV file uploads and saves them to a MongoDB database, where each column of the CSV file is one field in the database and each row is one record.

## Getting Started

### Prerequisites

- Python 3.x
- pip package manager
- MongoDB database server

### Installing

1. Clone this repository:

```Git
git clone https://github.com/sebastiangi312/Backend-assessment--Python---fastAPI.git
```

2. Install the required Python packages:

```Script
cd csv-upload-rest-api
pip install -r requirements.txt
```

3. Set the MongoDB connection details in `main.py`:

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['csvdb']
collection = db['csv_collection']
```

4.If you wish you can run the create_dummy.py to get a dummy.csv

```Script
python create_dummy.py
```

5.Start the API:

```Script
uvicorn main:app --reload
```
