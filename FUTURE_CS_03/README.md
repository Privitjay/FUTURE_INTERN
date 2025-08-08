# 🛡️ Security Overview Report  
**Project:** AES-Encrypted File Upload/Download Portal  
**Author:** Your Name  
**Date:** 2025-08-09  

---

## 1. 📜 Project Overview

This project implements a secure file upload/download portal to protect files **at rest** and **in transit** using **AES encryption**. It demonstrates secure web development practices, encryption handling, and basic key management for a small-scale secure file-sharing application.

**Key Features:**
- AES-256 encryption for all files stored on the server
- HTTPS/TLS for encrypted communication
- JWT-based authentication for file access
- Role-based access control (RBAC)
- Secure key storage and management

**Tech Stack:**
- **Backend:** Python Flask
- **Encryption Library:** PyCryptodome
- **Database:** SQLite (for metadata)
- **Version Control:** Git & GitHub
- **Testing Tools:** Postman, curl, Wireshark

---

## 2. 🛠️ Architecture Overview

**Flow Diagram:**  
```text
User → HTTPS → Flask API → AES Encrypt/Decrypt → Encrypted File Storage
