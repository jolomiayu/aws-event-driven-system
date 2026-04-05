🚀 AWS Event-Driven Processing System

📌 Overview

This project demonstrates a fully serverless event-driven architecture using AWS services.

It showcases how to build a scalable and fault-tolerant system where messages are processed asynchronously using Amazon SQS, AWS Lambda, and DynamoDB, with a Dead Letter Queue (DLQ) for handling failures.

---

🏗️ Architecture

![Architecture](https://raw.githubusercontent.com/jolomiayu/aws-event-driven-system/main/architecture/architecture-diagram.png)

---

⚙️ Tech Stack

- AWS Lambda
- Amazon API Gateway
- Amazon SQS (Main Queue)
- Amazon SQS (Dead Letter Queue - DLQ)
- Amazon DynamoDB
- AWS SAM (Serverless Application Model)
- Python

---

🔄 How It Works

1. Client sends a POST request to "/send"
2. API Gateway triggers Producer Lambda
3. Producer Lambda sends message to SQS (Main Queue)
4. Consumer Lambda processes messages from SQS
5. Messages are stored in DynamoDB
6. If processing fails, message is retried
7. After retries, message is sent to Dead Letter Queue (DLQ)

---

🌐 API Endpoint

POST /send

Example Request

{
"message": "hello world"
}

---

📸 Screenshots

API Test

![API Test](https://raw.githubusercontent.com/jolomiayu/aws-event-driven-system/main/screenshots/api-test.png)

SQS Queues

![SQS Queues](https://raw.githubusercontent.com/jolomiayu/aws-event-driven-system/main/screenshots/sqs-queues.png)

Lambda Function

![Lambda](https://raw.githubusercontent.com/jolomiayu/aws-event-driven-system/main/screenshots/lambda-function-overview.png)

DynamoDB Items

![DynamoDB](https://raw.githubusercontent.com/jolomiayu/aws-event-driven-system/main/screenshots/dynamodb-table-items.png)

DLQ Message

![DLQ](https://raw.githubusercontent.com/jolomiayu/aws-event-driven-system/main/screenshots/dlq-message.png)

---

🚀 Deployment

sam build
sam deploy --guided

---

💡 Key Features

- Event-driven architecture
- Asynchronous processing using SQS
- Fault tolerance with Dead Letter Queue (DLQ)
- Persistent storage using DynamoDB
- Infrastructure as Code using AWS SAM

---

🧠 What I Learned

- Designing event-driven systems
- Implementing message queues with SQS
- Handling failures using Dead Letter Queues
- Building scalable and resilient cloud architectures

---

👨‍💻 Author

Jolomi Ayu
