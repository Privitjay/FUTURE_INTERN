# 🛡️ Security Overview Report  
**Project:** AES-Encrypted File Upload/Download Portal  
**Author:** Donatus Junior Nwaoyibo 
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

### Main Components:

Upload Endpoint (/upload)

Accepts file from authenticated users

Validates file type and size

Encrypts with AES-256 before storage

Download Endpoint (/download)

Authenticates user via JWT

Decrypts file before sending to client

Key Management

AES key generated per file

Keys stored securely in environment variables or secrets manager

IV (initialization vector) stored alongside file metadata

## 3. 🔐 Security Controls Implemented
Control Area	Implementation	Purpose
Encryption at Rest	AES-256-CBC with random IV	Prevent unauthorized access to stored files
Encryption in Transit	HTTPS/TLS 1.2+ enforced	Prevent eavesdropping and MITM attacks
Authentication	JWT tokens for API access	Restrict file access to authorized users
Access Control	Role-based access (user/admin)	Prevent privilege escalation
Key Management	Keys stored in .env + rotated periodically	Reduce key compromise risk

## 4. 📊 Test Results
Test Environment:

OS: Ubuntu 22.04

Browser: Chrome v120

Tools: Postman, curl, Wireshark

Test ID	Test Case	Expected Result	Actual Result	Status
T001	Upload encrypted file	Stored as unreadable binary	✅ Pass	✅
T002	Download decrypts file	Matches original checksum	✅ Pass	✅
T003	Access without JWT	Returns HTTP 401 Unauthorized	✅ Pass	✅
T004	Attempt MITM on HTTPS	No plaintext captured	✅ Pass	✅

## 5. 🛡️ Threat Model & OWASP Mapping
Found/Expected Alert	Related OWASP Top 10 Category	Mitigation Implemented
Weak file validation	A05: Security Misconfiguration / A08: Software & Data Integrity Failures	File type + MIME checks
Unauthorized file access	A01: Broken Access Control	JWT auth + RBAC
Key exposure in code	A02: Cryptographic Failures	Keys in .env not committed
Brute force on login	A07: Identification & Authentication Failures	Rate limiting, lockout policy
Missing HTTPS	A02: Cryptographic Failures	HTTPS enforced

## 6. 📌 Example Encryption Process
AES-256 File Encryption in Python:

python
Copy
Edit
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

key = get_random_bytes(32)  # AES-256 key
iv = get_random_bytes(16)   # Initialization vector
cipher = AES.new(key, AES.MODE_CBC, iv)

with open('file.txt', 'rb') as f:
    plaintext = f.read()

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

with open('file.enc', 'wb') as f:
    f.write(iv + ciphertext)
7. 📝 Recommendations & Future Improvements
Short-Term (0–3 months):

Automate key rotation every 30 days

Implement server-side antivirus scanning for uploads

Add detailed audit logging for file actions

Long-Term (3–12 months):

Store keys in HSM or AWS KMS

Add MFA for all user accounts

Support client-side encryption for zero-knowledge file storage

8. 📦 Deliverables
GitHub Repository: https://github.com/yourusername/aes-file-portal

Walkthrough Video: [YouTube or Loom link]

Security Overview Document: (this report)
