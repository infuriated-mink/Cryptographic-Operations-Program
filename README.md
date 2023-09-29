# Cryptographic Operations Program

![GitHub](https://img.shields.io/github/license/infuriated-mink/cryptographic-operations-program)
![GitHub last commit](https://img.shields.io/github/last-commit/infuriated-mink/cryptographic-operations-program)

## Description

The **Cryptographic Operations Program** is a comprehensive Python solution designed to address a wide range of cryptographic needs with a strong focus on data integrity and security. This program empowers users to perform various cryptographic operations, including:

- **File Hash Verification:** Easily verify the integrity of files by comparing their SHA-256 hashes with expected values provided in an external file.

- **AES Decryption:** A custom AES encryption and decryption module ensures the confidentiality of sensitive data.

- **Digital Signature Verification:** Verify the authenticity of decrypted data using a provided digital signature and public key.

## Getting Started

### Prerequisites

Before using this program, ensure you have the required Python modules installed:

```bash
pip install pycryptodome

### Installation
Clone this repository to your local machine:
bash

git clone https://github.com/your-username/cryptographic-operations-program.git
cd cryptographic-operations-program
## Install the necessary Python libraries:
bash

pip install pycryptodome
[Optional] Prepare your cryptographic files. Place the encrypted data file (part1.txt.enc), the digital signature file (part1.txt.sig), the public key file (publickey.pem), and the file containing expected hashes (part1.sha256) in the project directory.
## Usage
Open your terminal or command prompt.

## Navigate to the project directory:

cd cryptographic-operations-program
Run the program:
bash

python main.py

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
Special thanks to the pycryptodome library for cryptographic functionality.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please open an issue or create a pull request.

### Issues and Support
If you encounter any issues or have questions about this program, please open an issue on the GitHub repository.
