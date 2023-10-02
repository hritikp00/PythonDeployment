import  subprocess
import string
import random

#Get current passowrd form user input
current_password = input("Enter the current MySQL password: ")

#Generate a new Password
new_password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))

#Change MySQL password using subprocess
subprocess.run(['mysql', '-u', 'root', '-p' + current_password, '-e',f"ALTER USER 'root'@'localhost' IDENTIFIED BY '{new_password}';"])

#Print and store new password in a file.
print(f"The new MYSQL password is: {new_password}")
with open('home/hritik/PythonDeployment/mysql_secret_password.txt', 'w') as f:
    f.write(new_password)