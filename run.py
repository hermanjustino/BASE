import os
import time
import subprocess

# ASCII Art
ascii_art = """
  ____  _____ _____ _____ 
 | __ )| ____|  ___| ____|
 |  _ \|  _| | |_  |  _|  
 | |_) | |___|  _| | |___ 
 |____/|_____|_|   |_____|
"""

# Print each character one by one with a delay
for char in ascii_art:
    print(char, end='', flush=True)
    time.sleep(0.01)  # delay of 0.01 seconds

print("\n")

current_path = os.getcwd()

print("====================================")
print("You are currently in: " + current_path)
print("====================================\n")

init_repo = input("Do you want to initialize a Git repository here? (yes/no): ")

typeOfRepo = "repository"

if init_repo.lower() == "yes":
    
    subprocess.run(["git", "init"], check=True)
    print("Git repository initialized.")
else:
    print("No Git repository initialized.")
    typeOfRepo = "directory"

repo_name = input("Enter the name of the new " + typeOfRepo + ":")
path = input("Enter the path where the " + typeOfRepo + " will be created: ")

full_path = os.path.join(path, repo_name)

os.makedirs(os.path.join(full_path, 'assets'), exist_ok=True)
os.makedirs(os.path.join(full_path, 'styles'), exist_ok=True)
os.makedirs(os.path.join(full_path, 'scripts'), exist_ok=True)

with open(os.path.join(full_path, 'index.html'), 'w') as f:
    f.write('''<!DOCTYPE html>
<html>
<head>
\t<title>Page Title</title>
\t<link rel="stylesheet" type="text/css" href="styles/styles.css">
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>

<script src="scripts/scripts.js"></script>

</body>
</html>''')

with open(os.path.join(full_path, 'styles', 'styles.css'), 'w') as f:
    f.write('body { background-color: red; }')

with open(os.path.join(full_path, 'scripts', 'scripts.js'), 'w') as f:
    f.write('// Add your JavaScript code here')

subprocess.run(['git', 'init'], cwd=full_path)

print("\nRepository setup completed successfully!")