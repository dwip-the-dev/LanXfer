# LanXfer - Secure & Fast LAN File Transfer 🚀

**LanXfer** is a **peer-to-peer file transfer** tool designed to make file sharing on local area networks (LAN) **easy**, **fast**, and **secure**. It allows two devices to transfer any size of file directly, with no central server or cloud service involved. Files are encrypted before transfer, ensuring that only the sender and receiver can access the content. 🔒

---

## ✨ Features

- 🤝 **Peer-to-Peer Transfer**: No server required—devices connect directly.
- ⚡ **Fast File Transfer**: Efficient transfer of large files with minimal latency.
- 🔐 **Encryption**: Strong encryption (AES/RSA) ensures that files are **viewable only by the sender and receiver**.
- 🕵️‍♂️ **Automatic Device Discovery**: Devices are discovered on the LAN using ARP.
- ✅ **Accept/Decline Option**: The receiver has full control over accepting or declining incoming files.
- 🚀 **Optimized for Speed**: Uses TCP/UDP protocols for fast, reliable transfer.
- 🛡️ **No Server**: Completely decentralized for privacy and security.

---

## ⚙️ Installation and Setup

1. **Clone the repository:**
  ```bash
  git clone https://github.com/yourusername/LanXfer.git
  cd LanXfer
  ```

2. **Create a Python virtual environment** (optional but recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
  ```

3. **Install dependencies:**
  > Currently, only standard Python libraries are used. Later, additional dependencies like `pycryptodome` for encryption will be added.
  ```bash
  pip install -r requirements.txt
  ```

---

## 🖧 How It Works

- **Device Discovery:**
  Once you run the program, LanXfer will automatically discover all devices in the same LAN using ARP.

- **Select the Receiver:**
  The sender will see a list of available devices in the LAN. Simply select the target device to initiate file sharing.

- **Send the File:**
  Choose the file you want to share. It will be encrypted, chunked into smaller parts, and sent securely to the receiver.

- **Accept or Decline:**
  The receiver will get a prompt to either accept or decline the incoming file transfer. The process is entirely under the control of the receiving device.

- **Secure Transfer:**
  All transfers are encrypted end-to-end for maximum privacy.

---

## 🔒 Security and Privacy

LanXfer ensures that only the sender and receiver can view the file contents. Encryption is implemented using **AES** for file encryption and **RSA** for secure key exchange, protecting files from unauthorized access during transit.

---

## 🤝 Contributing

We welcome contributions to improve LanXfer!
Feel free to fork the repository, create a new branch, and submit a pull request with your improvements. If you encounter any issues or have suggestions, open an issue or contact us.

---

## 💬 Contact

For any questions or inquiries, feel free to reach out through [GitHub Issues](https://github.com/Ujjwal-Devloper-5/LanXfer/issues) or email:
📧 **Ujjwalkumarbgpg6@gmail.com**

---

_Stay tuned for updates! This will soon be a professional-level service for secure LAN file transfers._ 🚀
