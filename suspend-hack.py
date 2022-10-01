import os
import subprocess

proc = subprocess.Popen(['acpi_listen'], stdout=subprocess.PIPE)
while True:
    line = proc.stdout.readline()
    if "close" in line.decode('utf-8').strip():
        print('lid closed - suspend')
        #subprocess.Popen(['systemctl', 'suspend'], shell=True)
        os.system('systemctl suspend')
        #os.system('pm-suspend')

