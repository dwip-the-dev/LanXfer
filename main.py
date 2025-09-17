from flask import Flask, render_template, request, send_from_directory, redirect, url_for, jsonify, flash
import os
import time
import psutil
import shutil
import logging
import tempfile

app = Flask(__name__)
UPLOAD_FOLDER = "files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = "your-secret-key"

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

def check_disk_space(min_space_mb=100):
    """Check disk space and inodes."""
    disk = psutil.disk_usage("/")
    free_mb = disk.free / (1024 * 1024)  # Bytes to MB
    total_inodes = os.statvfs("/").f_ffree
    return free_mb >= min_space_mb and total_inodes > 1000

def check_tmp_space(min_space_mb=50):
    """Check /tmp partition space."""
    tmp_dir = tempfile.gettempdir()
    tmp_disk = psutil.disk_usage(tmp_dir)
    free_mb = tmp_disk.free / (1024 * 1024)
    return free_mb >= min_space_mb

@app.route("/")
def index():
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    disk_free = psutil.disk_usage("/").free / (1024**3)  # GB
    tmp_free = psutil.disk_usage(tempfile.gettempdir()).free / (1024**3)  # GB
    inodes_free = os.statvfs("/").f_ffree

    stats = {
        "uptime": uptime,
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "disk_free": disk_free,
        "tmp_free": tmp_free,
        "inodes_free": inodes_free
    }

    logging.debug(f"Index stats: disk={disk:.1f}%, disk_free={disk_free:.2f}GB, inodes_free={inodes_free}")

    return render_template("index.html", files=files, stats=stats)

@app.route("/stats")
def get_stats():
    try:
        uptime_seconds = time.time() - psutil.boot_time()
        uptime = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
        cpu = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        stats = {
            "uptime": uptime,
            "cpu": cpu,
            "memory": memory,
            "disk": disk
        }
        logging.debug(f"Stats endpoint: {stats}")
        return jsonify(stats)
    except Exception as e:
        logging.error(f"Stats error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        if not check_disk_space(min_space_mb=100):
            disk = psutil.disk_usage("/")
            inodes_free = os.statvfs("/").f_ffree
            logging.error(f"Disk check failed: {disk.free / (1024**3):.2f}GB free, {inodes_free} inodes free")
            flash(f"Error: Insufficient disk space or inodes. {disk.free / (1024**3):.2f}GB free, {inodes_free} inodes available.", "error")
            return redirect(url_for("index"))

        if not check_tmp_space(min_space_mb=50):
            tmp_disk = psutil.disk_usage(tempfile.gettempdir())
            logging.error(f"Temp dir check failed: {tmp_disk.free / (1024**3):.2f}GB free in {tempfile.gettempdir()}")
            flash(f"Error: Insufficient space in temp directory ({tmp_disk.free / (1024**3):.2f}GB free).", "error")
            return redirect(url_for("index"))

        if "file" not in request.files:
            flash("No files selected.", "error")
            return redirect(url_for("index"))

        files = request.files.getlist("file")
        if not files or all(file.filename == "" for file in files):
            flash("No valid files selected.", "error")
            return redirect(url_for("index"))

        uploaded_count = 0
        for file in files:
            if file.filename == "":
                continue
            try:
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
                uploaded_count += 1
            except Exception as e:
                logging.error(f"Failed to save file {file.filename}: {str(e)}")
                flash(f"Failed to upload {file.filename}: {str(e)}", "error")

        if uploaded_count > 0:
            flash(f"Successfully uploaded {uploaded_count} file(s).", "success")
        return redirect(url_for("index"))

    except Exception as e:
        logging.error(f"Upload error: {str(e)}")
        flash(f"Upload failed: {str(e)}", "error")
        return redirect(url_for("index"))

@app.route("/download/<filename>")
def download_file(filename):
    try:
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)
    except FileNotFoundError:
        flash(f"File {filename} not found.", "error")
        return redirect(url_for("index"))

@app.route("/cleanup")
def cleanup():
    try:
        for filename in os.listdir(app.config["UPLOAD_FOLDER"]):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        flash("All files cleared from upload folder.", "success")
    except Exception as e:
        logging.error(f"Cleanup error: {str(e)}")
        flash(f"Cleanup failed: {str(e)}", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
