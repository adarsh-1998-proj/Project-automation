import psutil
import time
import smtplib
from email.mime.text import MIMEText

# Email Alert Setup
def send_email_alert(subject, body):
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    password = "your_email_password"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# System Health Check
def system_health_check():
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # Log results
    health_log = (
        f"System Health Check at {time.ctime()}\n"
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory.percent}%\n"
        f"Disk Usage: {disk.percent}%\n"
        "-------------------------------\n"
    )
    
    with open("system_health_log.txt", "a") as log_file:
        log_file.write(health_log)
    
    print(health_log)
    
    # Trigger alert if thresholds are crossed
    if cpu_usage > 80:
        send_email_alert("High CPU Usage Alert", health_log)
    if memory.percent > 90:
        send_email_alert("High Memory Usage Alert", health_log)
    if disk.percent > 90:
        send_email_alert("Low Disk Space Alert", health_log)

# Automate the health check every 10 minutes
if __name__ == "__main__":
    while True:
        system_health_check()
        time.sleep(600)  # Wait for 10 minutes
