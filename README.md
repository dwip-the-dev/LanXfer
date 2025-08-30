# LanXfer - Secure & Fast LAN File Transfer

**LanXfer** is a **peer-to-peer file transfer** tool designed to make file sharing on local area networks (LAN) **easy**, **fast**, and **secure**. It allows two devices to transfer any size of file directly, with no central server or cloud service involved. Files are encrypted before transfer, ensuring that only the sender and receiver can access the content.

---

## 🚀 **Features**
- **Peer-to-Peer Transfer**: No need for a server—devices connect directly.
- **Fast File Transfer**: Transfer large files with minimal latency.
- **Encryption**: Strong encryption (AES/RSA) ensures that the file content is **viewable only by the sender and receiver**.
- **Automatic Device Discovery**: Devices are automatically discovered on the LAN using ARP.
- **Accept/Decline Option**: The recipient device has full control over accepting or declining incoming files.
- **Optimized for Speed**: Uses TCP/UDP protocols for fast, reliable transfer.
- **No Server**: Completely decentralized system for privacy and security.

---

## ⚙️ **Installation and Setup**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/LanXfer.git
   cd LanXfer
2. **Create a Python virtual environment (optional but recommended):**
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
3. **Install dependencies:**
  Currently, only standard Python libraries are used.
  Later, additional dependencies like pycryptodome for encryption will be added.
  ```bash
  pip install -r requirements.txt

💻 How to Use

Device Discovery:
Once you run the program, LanXfer will automatically discover all the devices in the same LAN using ARP.

Select the Receiver:
The sender will see a list of available devices. Simply select a device to initiate file sharing.

Send the File:
Choose the file you want to share, and it will be encrypted, chunked, and sent directly to the receiver.

Accept or Decline:
The receiver will receive a prompt to either accept or decline the incoming file transfer.

Secure Transfer:
Once accepted, the file is sent in secure chunks, ensuring that no third party can view the contents. Once complete, the receiver can decrypt and access the file.

⚠️ Warning - Under Development

This project is currently under development.
LanXfer is not yet a finished product and is still being optimized for reliable file transfer. It is a proof of concept and will soon be enhanced with additional features like:

Full encryption implementation

Multi-device support

Optimized for even faster transfers

Robust error handling and security measures

Please stay tuned for further updates. This will soon be a professional-level service for secure LAN file transfers.

🔒 Security and Privacy

LanXfer ensures that only the sender and receiver can see the file contents. Encryption is implemented using AES for file encryption and RSA for secure key exchange. We are committed to ensuring your files are safe from unauthorized access.

🤝 Contributing

We welcome contributions!
Please feel free to fork the repository, create a new branch, and open a pull request. If you encounter any issues or have suggestions for improvements, open an issue or contact us directly.

💬 Contact

For any questions or inquiries, feel free to reach out through GitHub Issues or email:
Ujjwalkumarbgpg6@gmail.com


Happy Transferring! 🚀
