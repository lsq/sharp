#!/usr/bin/python

import subprocess as pro
import os
import shutil
from shlex import quote


newShell=pro.check_output(["cygpath", "-m", '/usr/bin/bash']).strip(b"\n").decode()
if shutil.which('ls') is None:
    print("Error: Command 'which' not found.")
else:
    try:
      result = pro.run(['ls', 'c:/msys64'],
        executable=newShell,
        shell=True, check=True, stdout= pro.PIPE, stderr= pro.PIPE)
      print(result.stdout.decode())
      result = pro.run(['ls', 'c:/msys64'],
        shell=True, check=True, stdout= pro.PIPE, stderr= pro.PIPE)
      print(result.stdout.decode())
    except pro.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(f"Error output: {e.stderr.decode()}")

#  newShell=pro.check_output(["cygpath", "-m", '/usr/bin/bash']).strip(b"\n").decode()
#  content = 'PKG_CONFIG_PATH="<(pkg_config_path)" pkg-config --cflags-only-I vips-cpp vips glib-2.0'
content = 'which node'
print(f'new comspec: {os.environ.get('COMSPEC')}')
print(f'newshell: {newShell}')
ret = pro.run(
        content,
        stdout=pro.PIPE,
        executable=newShell,
        shell=True,
        )
print(f'{ret}')
# content = 'node -p \\"process.report.getReport().header.osName\\"'
# content = 'node -p \'process.report.getReport().header.osName\''
content = 'node -p "process.report.getReport().header.osName"'
print(f'{content}')
#  content = 'node -p "process.report.getReport().header.osName"'
#  print(f'{quote(content)}')
#  content = quote(content)
ret = pro.run(
        content,
        stdout=pro.PIPE,
        executable=newShell,
        shell=True,
        )
print(f'{ret}')
# print("hihihi".replace("i","o"))
