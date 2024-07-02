# Excel to JSON Converter with FastAPI

This project is a web application built using FastAPI that allows users to upload an Excel file, convert it to JSON format, and download the JSON file. It also provides functionality to clear the uploaded files and generated JSON files with a notification.

## Features

- Upload an Excel file and convert it to JSON format.
- Download the converted JSON file.
- Clear the uploaded files and JSON files.
- Display a toast notification upon successful clearing of files.

## Requirements

- Python 3.6+
- FastAPI
- Uvicorn
- Pandas
- Openpyxl
- Jinja2
- python-multipart

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/excel-to-json-fastapi.git
    cd excel-to-json-fastapi
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```


## Running the Application

1. **Run the FastAPI application:**

    ```bash
    python main.py
    ```

2. **Open a web browser and go to:**

    ```
    http://localhost:5101/
    ```

## File Structure

excel-to-json-fastapi/
│
├── main.py
├── requirements.txt
├── templates/
│ └── upload.html
├── static/
│ └── main.js
├── uploads/
│
└── README.md


## Usage

1. **Upload an Excel File:**
    - Click the "Choose Excel File" button and select an Excel file.
    - Click the "Upload and Convert" button to convert the file to JSON format and download it.

2. **Clear Files:**
    - Click the "Clear" button to delete all files in the `uploads` folder.
    - A toast notification will appear to confirm the successful clearing of files.
