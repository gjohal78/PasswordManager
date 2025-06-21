# Secure Password Manager

A secure, command-line password manager built with Python. It uses cryptographic hashing and encryption to safely store and retrieve your credentials.

## Features

- Master password authentication using salted SHA-256 hashing via `hashlib`
- AES-256 encryption of credentials using `cryptography.fernet`
- Secure input using `getpass`
- Add, retrieve, and list encrypted service credentials
- Modular, scalable, and beginner-friendly CLI design

## Technologies Used

- Python 3
- `hashlib` for password hashing
- `cryptography.fernet` for AES-based symmetric encryption
- `getpass` for secure password entry
- JSON for lightweight encrypted data storage

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```
