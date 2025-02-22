# Cloud SQL + Docker + Cloud Run

## 📌 Project Description
This project demonstrates how to connect a **Flask** application running inside **Docker** to a **PostgreSQL** database hosted on **Google Cloud SQL**. The application is then deployed on **Cloud Run**, providing a fully managed, serverless environment.

## 🏗️ Project Structure
```
cloudsql-docker/
│── Dockerfile         # Docker configuration file
│── app.py            # Flask application connecting to Cloud SQL
│── requirements.txt   # Dependencies list
│── .gcloudignore      # Files to be ignored by Google Cloud
└── README.md         # Project documentation
```

## 🚀 Setup Instructions

### 1️⃣ Prerequisites
Ensure you have the following installed and configured:
- **Google Cloud SDK**
- **Docker**
- **Google Cloud SQL PostgreSQL instance**

### 2️⃣ Create Cloud SQL PostgreSQL Instance
Run the following commands to create a Cloud SQL instance and a database:

```sh
gcloud sql instances create my-postgres-instance \
    --database-version=POSTGRES_14 \
    --tier=db-f1-micro \
    --region=us-central1

# Create a database
gcloud sql databases create my_database --instance=my-postgres-instance

# Create a database user
gcloud sql users create myuser --password=mypassword --instance=my-postgres-instance
```

Find the **Cloud SQL connection name**:
```sh
gcloud sql instances describe my-postgres-instance --format="value(connectionName)"
```

### 3️⃣ Build & Deploy with Docker & Cloud Run

#### 🔹 Build and push the Docker image:
```sh
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/cloudsql-docker
```

#### 🔹 Deploy to Cloud Run with Cloud SQL connection:
```sh
gcloud run deploy cloudsql-docker \
    --image=gcr.io/YOUR_PROJECT_ID/cloudsql-docker \
    --platform=managed \
    --region=us-central1 \
    --allow-unauthenticated \
    --add-cloudsql-instances=YOUR_CLOUDSQL_CONNECTION_NAME \
    --set-env-vars=INSTANCE_CONNECTION_NAME=YOUR_CLOUDSQL_CONNECTION_NAME
```

Replace `YOUR_PROJECT_ID` and `YOUR_CLOUDSQL_CONNECTION_NAME` with your actual project details.

### ✅ Access the Application
After deployment, Cloud Run will provide a **public URL**. Open it in your browser:
```
https://your-cloud-run-url/
```
You should see:
```
Connected to PostgreSQL in Cloud SQL!
```

## 🔧 Troubleshooting
- **Database connection issues?** Ensure the instance connection name is correct and the database is accessible.
- **Authentication errors?** Verify IAM permissions for Cloud SQL and Cloud Run.
- **Cloud SQL not accessible?** Enable the `Cloud SQL Admin API` and ensure your service account has the necessary roles.

## 📜 License
This project is open-source and can be freely used for learning purposes. 🚀

