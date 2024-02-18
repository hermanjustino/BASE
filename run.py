import os
import subprocess
import time

ascii_art = """
__________    _____    ____________________
\______   \  /  _  \  /   _____/\_   _____/
 |    |  _/ /  /_\  \ \_____  \  |    __)_ 
 |    |   \/    |    \/        \ |        |
 |______  /\____|__  /_______  //_______  /
        \/         \/        \/         \/ 
"""

# Print each character one by one with a delay
for char in ascii_art:
    print(char, end='', flush=True)
    time.sleep(0.005)

print("\n")

# Get the current working directory
current_path = os.getcwd()

# Print the current path in a menu format
print("====================================")
print("You are currently in: " + current_path)
print("====================================")
print("\n")


# Prompt for the name of the repo and the path
repo_name = input("Enter the name of the new repository: ")
path = input("Enter the path where the repository will be created: ")

# Create the full path
full_path = os.path.join(path, repo_name)

# Create the directories
os.makedirs(os.path.join(full_path, 'assets'), exist_ok=True)
os.makedirs(os.path.join(full_path, 'styles'), exist_ok=True)
os.makedirs(os.path.join(full_path, 'scripts'), exist_ok=True)

# Create the index.html file
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

# Create the styles.css file
with open(os.path.join(full_path, 'styles', 'styles.css'), 'w') as f:
    f.write('body { background-color: red; }')

# Create the scripts.js file
with open(os.path.join(full_path, 'scripts', 'scripts.js'), 'w') as f:
    f.write('// Add your JavaScript code here')

# Initialize an empty git repo
subprocess.run(['git', 'init'], cwd=full_path)

print("\nRepository setup completed successfully!")