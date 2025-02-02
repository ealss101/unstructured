# Unstructured Data Ingestion Pipeline

## Overview
This repository provides a set of data ingestion pipelines that leverage the **Unstructured Ingest** library to extract, process, and store documents from multiple sources, including:

- **Google Drive**
- **OneDrive**
- **Local Filesystem**

Each pipeline reads from a specified source, processes the documents using Unstructured's partitioning API, and saves the output to a designated folder based on configurations set in the `.env` file.

---

## Features
- **Supports multiple connectors:** Google Drive, OneDrive, and Local Filesystem.
- **Automated document partitioning** via Unstructured API.
- **Highly configurable** using `.env` file settings.
- **Supports high-resolution partitioning** with optional chunking and embedding.
- **Local storage for processed documents**.

---

## Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/reponame.git
cd reponame
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## Configuration
### **Setting Up the `.env` File**
Each pipeline is configured using environment variables stored in a `.env` file. Below is a sample `.env` file for different ingestion sources.

#### **Google Drive Configuration**
```ini
GCP_SERVICE_ACCOUNT_KEY_FILEPATH=path/to/your-service-account.json
GCP_SERVICE_ACCOUNT_KEY_STRING={your-service-account-json-string}
GOOGLE_DRIVE_FOLDER_ID={your-google-drive-folder-id}
LOCAL_FILE_GOOGLE_DRIVE_DOWNLOAD_DIR=./downloads/google_drive
LOCAL_FILE_GOOGLE_DRIVE_UPLOAD_DIR=./output/google_drive
UNSTRUCTURED_API_KEY={your-api-key}
UNSTRUCTURED_API_URL={your-unstructured-api-url}
```

#### **OneDrive Configuration**
```ini
ONEDRIVE_CLIENT_CRED={your-client-credentials}
ONEDRIVE_CLIENT_ID={your-client-id}
ONEDRIVE_TENANT={your-tenant-id}
ONEDRIVE_USER_PNAME={your-user-principal-name}
ONEDRIVE_AUTHORITY_URL={your-authority-url}
ONEDRIVE_PATH={your-onedrive-path}
LOCAL_FILE_ONE_DRIVE_DOWNLOAD_DIR=./downloads/onedrive
UNSTRUCTURED_API_KEY={your-api-key}
UNSTRUCTURED_API_URL={your-unstructured-api-url}
```

#### **Local File Configuration**
```ini
LOCAL_FILE_INPUT_DIR=./data
LOCAL_FILE_OUTPUT_DIR=./output
UNSTRUCTURED_API_KEY={your-api-key}
UNSTRUCTURED_API_URL={your-unstructured-api-url}
```

---

## Running the Pipelines

### **Google Drive Ingestion**
```bash
python google_drive_ingest.py
```

### **OneDrive Ingestion**
```bash
python onedrive_ingest.py
```

### **Local File Ingestion**
```bash
python local_ingest.py
```

---

## Documentation & Support
For more details on the connectors and configuration options, refer to the official Unstructured documentation:
- **Google Drive Connector**: [Google Drive Docs](https://docs.unstructured.io/api-reference/ingest/source-connectors/google-drive)
- **OneDrive Connector**: [OneDrive Docs](https://docs.unstructured.io/api-reference/ingest/source-connectors/one-drive)
- **Local Connector**: [Local Config Docs](https://docs.unstructured.io/api-reference/ingest/source-connectors/local)

If you need help, feel free to open an issue or reach out in the Unstructured community.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

