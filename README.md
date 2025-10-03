# 🌐 Microservice Architecture for Translating Website

This project is the second iteration of a translating platform, redesigned to overcome performance limitations from its original monolithic version. It now features a scalable microservice architecture with Redis caching and REST/gRPC communication between services.

## 🚀 Overview

The system is built to handle translation requests efficiently by distributing responsibilities across independent services. It includes:

- **API Gateway**: Central entry point for all client requests.
- **AuthService**: Handles authentication and token validation.
- **UserService**: Manages user profiles and preferences.
- **MessagingService**: Handles message formatting and delivery.
- **TranslatingService**: Processes and returns translated content.
- **Redis Cache**: Stores frequent queries and session data to reduce latency.


![Architecture Diagram](<img width="729" height="711" alt="image" src="https://github.com/user-attachments/assets/8e1fc48f-51ca-44e4-87e7-03097cb49e52" />
)

## ✅ Current Status

- ✅ `AuthService` — Functional
- ✅ `API Gateway` — Functional
- ⏳ Other services — In progress

## 🛠️ Technologies

| Layer         | Stack                          |
|--------------|---------------------------------|
| Backend       | Flask, gRPC                    |
| Caching       | Redis                          |
| Database      | PostgreSQL                     |
| DevOps        | Docker, Docker Compose         |
| Communication | REST, gRPC, Redis Pub/Sub      |

## 📦 Project Structure

