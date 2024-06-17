Job Posting Duplicate Detection
===============================

https://github.com/surbhi498/DuplicateJobPostings/blob/main/README.md#job-posting-duplicate-detection

Introduction
------------

https://github.com/surbhi498/DuplicateJobPostings/blob/main/README.md#introduction

The aim of this project is to evaluate skills in creating embeddings from text data and using Milvus, a high-performance vector search engine, to identify duplicate entries in job postings. The project highlights the importance of reproducibility using Docker or Docker Compose.

Please note: A 2-minute video demonstration of your work should be included.

Requirements
------------

https://github.com/surbhi498/DuplicateJobPostings/blob/main/README.md#requirements

- Python 3.x
- PyTorch
- Sentence Transformers
- pymilvus

Install dependencies using:

```source-shell
pip install -r requirements.txt
```

Installation
------------

Clone the repository:
```bash
git clone https://github.com/surbhi498/DuplicateJobPostings.git

Navigate to the project directory:
```bash
cd DuplicateJobPostings

Install dependencies:
```bash
pip install -r requirements.txt
```

Usage
-----

Docker/Docker Compose Integration

Containerization
Build the Docker image:
```bash
docker build -t job-posting-duplicate-detection .
```

Docker Compose
If you have multiple services (e.g., a database, a backend service, etc.), define each service in docker-compose.yml and ensure proper networking.

Run the Docker image:
```bash
docker-compose up
```

Results and Evaluation
-----------------------

Results and evaluation metrics are provided in the code comments of jobs.ipynb. Evaluate the effectiveness of the duplicate detection method based on precision, recall, and similarity threshold.

Docker Integration
The project includes Docker and Docker Compose files (Dockerfile and docker-compose.yml) for containerization, ensuring a reproducible and isolated environment. Follow the instructions in the Usage section to build and run the Docker image.

Video Demo
----------

Watch the demo video for a quick overview of the project.

Contributing
------------

Contributions are welcome! Feel free to open issues or pull requests for any improvements or new features.
