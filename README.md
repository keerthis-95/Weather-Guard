A lightweight, high-performance Python backend service designed to fetch, clean, and validate real-time weather metrics from external REST APIs concurrently. 

This project demonstrates core backend engineering principles, including multi-threaded data ingestion, robust schema validation using Pydantic, automated testing, and comprehensive error handling.

Tech Stack & Standard Libraries

Language: Python 3.10+
Data Validation: Pydantic (v2)
Testing Framework: Pytest
Concurrency: `concurrent.futures.ThreadPoolExecutor`
Networking & Parsing: `urllib.request`, `json`

Project Architecture
├── models.py          # Data definitions and Pydantic validation schemas
├── engine.py          # Master DataEngine managing ThreadPool worker distribution
├── main.py            # Main orchestration file and application entry point
├── test_weather.py    # Automated test cases checking payload boundary constraints
└── README.md          # Project documentation
