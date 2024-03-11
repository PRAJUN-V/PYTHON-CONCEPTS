# Specify the file path
file_path = r'C:\Users\HP\Documents\python.txt'

# Open the file and read its content
with open(file_path, 'r') as file:
    python_code = file.read()

# Execute the Python code
exec(python_code)
