# Job Posting Duplicate Detection

## Introduction

The goal of this project is to assess skills in generating embeddings from text data and using Milvus, a high-performance vector search engine, to detect duplicate entries in job postings. The project emphasizes reproducibility using Docker or Docker Compose.

**Note:** Please include a 2-minute video to demo your work.

## Requirements

- Python 3.x
- PyTorch
- Sentence Transformers
- pymilvus

Install dependencies using:

```bash
pip install -r requirements.txt


# Installation
Clone the repository:

git clone https://github.com/arasgungore/job-posting-duplicate-detection.git

Navigate to the project directory:

cd job-posting-duplicate-detection
Install dependencies:

pip install -r requirements.txt


Docker/Docker Compose Integration
Containerization
Build the Docker image:

docker build -t job-posting-duplicate-detection .
Docker Compose
If you have multiple services (e.g., a database, a backend service, etc.), define each service in docker-compose.yml and ensure proper networking.

Run the Docker image:

docker-compose up

Results and Evaluation
Results and evaluation metrics are provided in the code comments of jobs.ipynb. Evaluate the effectiveness of the duplicate detection method based on precision, recall, and similarity threshold.

Docker Integration
The project includes Docker and Docker Compose files (Dockerfile and docker-compose.yml) for containerization, ensuring a reproducible and isolated environment. Follow the instructions in the Usage section to build and run the Docker image.

Video Demo
Watch the demo video for a quick overview of the project.

Contributing
Contributions are welcome! Feel free to open issues or pull requests for any improvements or new features.

