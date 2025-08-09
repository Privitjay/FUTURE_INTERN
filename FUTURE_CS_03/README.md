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

## 📂 Deliverables
- [x] GitHub repository with documented source code
- [x] Walkthrough video of encryption and file transfer
- [x] Security overview document
- [x] Example encrypted files and decryption steps

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

## 📌 OWASP Top 10 Mapping
| OWASP Risk              | Mitigation in Portal                                      |
|-------------------------|-----------------------------------------------------------|
| A01: Broken Access Control | RBAC, JWT auth, server-side validation                  |
| A02: Cryptographic Failures | AES-256 GCM, TLS 1.2+, secure key storage               |
| A05: Security Misconfiguration | HTTPS, secure headers, CSRF protection             |
| A08: Software/Data Integrity Failures | Hash checks, integrity verification          |

---

## 📈 Recommendations for Improvement
- Integrate HSM (Hardware Security Module) for key storage
- Implement file expiration policy for sensitive uploads
- Add automated malware scanning before encryption
- Deploy intrusion detection for suspicious file activity

---

## 📝 Conclusion
This AES-encrypted file portal ensures **confidentiality**, **integrity**, and **secure access control** for file uploads and downloads.  
By applying **industry best practices** and aligning with **OWASP Top 10** standards, it minimizes common security risks in file handling applications.

---
