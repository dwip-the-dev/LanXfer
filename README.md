# ⚡ LanXfer – Lightning Fast LAN File Transfer ⚡

LanXfer is a **super simple, blazing fast, and secure LAN-based file transfer system**.  
Send files instantly between devices connected to the same network – no cloud, no bullshit, just raw speed. 🚀

---

# 🔑 Setup Secret Key

LanXfer uses Flask’s `SECRET_KEY` for session security.  
Generate a 64-character hex key using Python:

```
python3 -c "import secrets; print(secrets.token_hex(32))"
```
Copy the generated key and set it in your app:
```
app.config["SECRET_KEY"] = "your_generated_key_here"
```

---

# ⚙️Installation

## 📦Requirements

> Python 3.8+

> Flask,psutil

> A working LAN (obviously 😎)


## Install dependencies:

> pip install -r requirements.txt


---

# 🖥️ Running LanXfer

## 🐧 Linux

```
git clone https://github.com/Angel42199/LanXfer.git
cd LanXfer
python3 main.py
```
Access from your browser at:
> 👉 http://127.0.0.1:5000

> 👉 http://pc-ip:5000


---

## 🪟 Windows
```
git clone https://github.com/Angel42199/LanXfer.git
cd LanXfer
python main.py
```
Access from your browser at:
>👉 http://127.0.0.1:5000

>👉 http://pc-ip:5000

(Use ipconfig in CMD to find your local IP)


---

# 📂 Sending Files

1. Open LanXfer in your browser.


2. Choose file(s) to upload.


3. Click on download button to download a file.


4. Done. 💨


---

# 🔥 Features

⚡ Zero-cloud, direct LAN transfers

🔑 Secure Flask backend with SECRET_KEY

🌐 Works on Windows, Linux, Mac

🛡️ No spyware, no ads, no nonsense

🖤 Clean & minimal web UI



---

# 🛠️ Development

Want to hack it? Clone the repo and edit freely.
Pull requests welcome ✨

