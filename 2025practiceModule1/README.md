## Task1

## Objective

This challenge aims to assess contestants' ability to integrate and deploy various

services within the Google Cloud Platform (GCP). Contestants must complete a

full application based on Cloud Run, Cloud SQL, and Cloud Storage while

automating deployment through Cloud Build, Cloud Deploy, and Cloud

Scheduler.

Note: Please refer to Table 1 for configuration of required resources! If it is a

mentioned service, you can name it yourself

Contestants must complete the following tasks:

## 1. Create Cloud SQL and Set Up Tables

- Create a Cloud SQL instance.

- Use the SQL script provided in gs://task1-source-code/sql.txt to create tables and columns.

- Ensure Cloud SQL can be connected to the Cloud Run service.

## 2. Process Cloud Storage Source Files

- gs://task1-source-code: Files in this folder cannot be modified, contestants can only read these resources.

- gs://task1-source-code-modify: Files in this folder can be modified, contestants must adjust the contents as needed.

## 3. Configure Cloud Build and Cloud Deploy

- Use Cloud Build to read the source code and Dockerfile to build the image from gs://task1-source-code.

- Push the built image to Artifact Registry.

- Cloud build needs to be able to create images and create releases to create new Cloud runs

## 4. Configure Cloud Scheduler


- Create a Cloud Scheduler job to run every hour.

- Cloud Scheduler must trigger Cloud Build to rebuild and redeploy Cloud Run.

## 5. Configure Cloud Run and Connect to VPC and Cloud SQL

- Configure Cloud Deploy to deploy the latest image to Cloud Run and set the latest version tag.

- Deploy the Cloud Run service and ensure it can connect to Cloud SQL.

- Cloud Run must use a VPC internal IP to access Cloud SQL (not a public IP).

- Ensure Cloud Run sets database connection information via environment variables.

- Set up Cloud Deploy to support rollback, allowing reversion to the previous version.

- You can refer to gs://task1-source-code-modify/yaml-sample.yaml to help you complete the VPC and environment variable settings.

## 6. Set Up Cloud Load Balancer and Cloud Storage Website

- Host index.html as the website entry point using Cloud Storage.

- Provide public access via Cloud Load Balancer and Cloud CDN.

- Ensure the website forwards requests to Cloud Run and Cloud Run stores request data in Cloud SQL.

## Completion Criteria

Contestants must successfully complete the following tasks and pass the tests:

- 1. Cloud SQL functions correctly: Able to access SQL and read/write data.

- 2. Cloud Run operates normally: The service can respond to API requests and interact with Cloud SQL.


- 3. Cloud Build & Cloud Deploy function correctly: Cloud Build correctly builds the image, and Cloud Deploy automatically deploys it.

- 4. Cloud Scheduler functions correctly: It triggers Cloud Build every hour to redeploy Cloud Run.

- 5. Cloud Load Balancer and Cloud Storage function correctly: The website displays index.html and interacts with Cloud Run through the frontend.

Contestants must complete all configurations as required and submit the final

solution within the given timeframe.

*Table 1*

| Network |   |
| --- | --- |
| VPC name | task1-vpc |
| Subnet name | task1-sb |
| Region | us-central1 |
| IPv4 range | 10.0.0.0/16 |

| Cloud SQL |   |
| --- | --- |
| Database Engine | MySQL |
| Cloud SQL edition | Enterprise |
| Preset | Sandbox |
| Instance ID | task1-sql |
| Username | root |
| User Password | password |
| region | us-central1 |
| Machine configuration | 2 vCPU, 8 GB |
| Storage type | SDD,10GB |
| Network | task1-vpc |

| Load Balancer |   |
| --- | --- |
| Name | task1-ealb |
| Frontend Protocol | HTTP |
| Frontend Port | 80 |


Backend Service Name

task1-bked
