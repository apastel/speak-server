#!/usr/bin/env python3

import sys
import subprocess

def _is_package_installed(package_name):
    print(f'Checking if {package_name} is installed...', end='')
    result = subprocess.run(['dpkg', '-s', package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print('YES')
        return True
    stdout = result.stdout.decode('utf-8')
    stderr = result.stderr.decode('utf-8')
    if 'not installed' in stderr:
        print('NO')
        return False
    else:
        print(stdout)
        print(stderr, file=sys.stderr)
        raise(f'Failed to verify {package_name} was installed')

for package in [line.rstrip('\n') for line in open('apt-requirements.txt')]:
    if not _is_package_installed(package):
        print(f'Attempting to install {package}...')
        subprocess.run(['sudo', 'apt', '-y', 'install', package], check=True)
        print(f'Attempting to install {package}...DONE.')

print('Initializing python3-venv...')
# Creates a Virtual Environment containing Python3 and Pip3
subprocess.run(['python3', '-m', 'venv', 'venv'], check=True)
# Install dependencies into local venv
subprocess.run(['venv/bin/pip', 'install', '-r', 'pip-requirements.txt'], check=True)
print('Initializing python3-venv...DONE.')

# Launch main script inside the venv
cmd_line = ['sudo', 'venv/bin/python3', 'server/server.py']
cmd_line.extend(sys.argv[1:])
try:
    subprocess.run(cmd_line, check=True)
except subprocess.CalledProcessError as e:
    if e.returncode == 11:
        # Indicates that the subprocess already printed the error.
        exit(11)
    else:
        raise e