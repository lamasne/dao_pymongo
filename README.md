# MongoDB DAO Skeleton for Python

This Python library provides a **DAO (Data Access Object) skeleton** for the NoSQL database MongoDB, ensuring efficient and structured database access. It manages connections using a **pymongo client singleton**, maintaining a single active database connection to prevent redundant and inefficient connection handling.

Additionally, this DAO **automates DTO (Data Transfer Object) handling** by converting database documents into structured objects. It supports **custom DTO mapping**, allowing users to define a dictionary linking business objects to collection fields.

## Features

### **Efficient Database Connection**
- Implements a **singleton pattern** to maintain a single MongoDB connection.  
- Reduces overhead by preventing redundant connection openings and avoids errors due to chaotic connection handling.  

### **Data Access and CRUD Operations**
- **Decouples data storage from business logic**:
  - Methods require no database-specific details (not even the collection name).  
  - Methods return either:
    - A **dict of `{id: object}` pairs** (or a single object).  
    - A **dict of `{attribute: value}` pairs** (or a single value).  
- Provides structured **insert and retrieval** operations.  

### **DTO Automation**
- **Custom DTO mappings**: Converts MongoDB documents into instances of custom classes.
- Returns either **mapped DTOs or raw documents** based on user preferences.  

## Installation
To install relevant packages, from a virtual environment, use command:
```bash
python -m pip install git+https://github.com/lamasne/dao_pymongo.git
```
To test the installation:
```python
from dao_pymongo.meta_functions import test_installation

test_installation()
```
        
## Usage
- Create a `mongodb_settings` file and a `co2class` dictionary.
- Initialize the **DAO**
```python
DAO(mongodb_settings, co2class)
```
- Use `DAO()` for database operations.

## License
This project is open-source and available under the MIT License.


