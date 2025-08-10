# 🔐 AES Encrypted File Upload/Download Portal – Security Report

## 📋 Project Overview
**Task:**  
Build a secure file upload/download portal implementing **AES encryption** to protect files **at rest** and **in transit**.

**Objectives:**
- Implement strong encryption (AES-256)
- Secure file storage and retrieval
- Protect encryption keys from unauthorized access
- Provide authentication & access control

---

## 🛠 Skills Gained
- Web development (Flask / Express)
- AES encryption & decryption
- Secure file handling and validation
- Encryption key management
- REST API design and testing
- Using Postman & curl for API testing

---

## ⚙️ Tools & Technologies
| Category            | Tools / Libraries                               |
|---------------------|------------------------------------------------|
| Programming         | Python Flask                                   |
| Encryption          | PyCryptodome                                   |
| Version Control     | Git & GitHub                                    |
| Testing             | Postman / curl                                  |
| Security Standards  | OWASP Top 10, NIST SP 800-57                     |

---



---

## 🛡 Security Implementation
### 1. **File Encryption (At Rest)**
- AES-256 in **GCM mode** for confidentiality + integrity
- Unique IV (Initialization Vector) per file
- Keys stored securely in environment variables or a dedicated KMS (Key Management Service)

### 2. **File Transmission (In Transit)**
- Enforced **HTTPS** with TLS 1.2+
- Secure headers using   Flask-Talisman (Python)
- CSRF protection for form submissions

### 3. **Authentication & Access Control**
- JWT-based authentication
- Role-based access (RBAC)
- Access logs for all file operations

---

## 🧪 Example API Endpoints
| Method | Endpoint               | Description                       | Auth Required |
|--------|------------------------|-----------------------------------|--------------|
| POST   | `/upload`              | Upload & encrypt a file           | ✅           |
| GET    | `/download/<file_id>`  | Download & decrypt a file         | ✅           |
| DELETE | `/delete/<file_id>`    | Remove file from storage          | ✅           |

---

## 📊 Security Testing
| Test Case                          | Result  | Notes                                     |
|------------------------------------|---------|-------------------------------------------|
| Upload valid file                  | Pass ✅ | AES encryption applied                    |
| Upload malicious file (XSS)        | Pass ✅ | Content type & file extension validation  |
| Unauthorized file access           | Pass ✅ | JWT auth blocks access                    |
| Man-in-the-middle attack attempt   | Pass ✅ | HTTPS enforced, no plaintext exposure     |

---


## Video Walk Through


## 📌 OWASP Top 10 Mapping
| OWASP Risk              | Mitigation in Portal                                      |
|-------------------------|-----------------------------------------------------------|
| A01: Broken Access Control | RBAC, JWT auth, server-side validation                  |
| A02: Cryptographic Failures | AES-256 GCM, TLS 1.2+, secure key storage               |
| A05: Security Misconfiguration | HTTPS, secure headers, CSRF protection             |
| A08: Software/Data Integrity Failures | Hash checks, integrity verification          |

---

 ## Setup & Usage 
 
markdown
Copy
Edit
## MorningstarClipper-Encrypted File Upload/Download Portal

Local demo implementing Morningstarclipper AES-GCM encryption for files at rest and HTTPS for transit.

## Quick setup (Linux)

1. Clone repo:
```bash
git clone <your-repo-url>
cd aes-file-portal
Create virtualenv & install:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Generate secrets:

bash
Copy
Edit
python3 generate_key.py
# Copy AES_SECRET_KEY and JWT_SECRET output to .env
Create .env using .env.example and paste values.

Initialize database & demo user:

bash
Copy
Edit
python3 db_init.py
# creates demo user: demo / password123
Run the app:

bash
Copy
Edit
python3 app.py
# App runs at https://localhost:5000 with adhoc TLS
API Examples (curl)
Login:

bash
Copy
Edit
curl -k -X POST https://localhost:5000/login -H "Content-Type: application/json" \
-d '{"username":"demo","password":"password123"}'
Upload:

bash
Copy
Edit
Export TOKEN="copy token from the previous step and paste here"
curl -k -X POST -H "Authorization: Bearer $TOKEN" -F "file=@/path/to/test.txt" \
https://localhost:5000/upload
List files:

bash
Copy
Edit
curl -k https://localhost:5000/files
Download:

bash
Copy
Edit
curl -k -H "Authorization: Bearer $TOKEN" \
https://localhost:5000/download/<stored_name> -o downloaded_file.txt

---

## 📝 Conclusion
This AES-encrypted file portal ensures **confidentiality**, **integrity**, and **secure access control** for file uploads and downloads.  
By applying **industry best practices** and aligning with **OWASP Top 10** standards, it minimizes common security risks in file handling applications.

---
