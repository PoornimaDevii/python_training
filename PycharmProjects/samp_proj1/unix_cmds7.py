
# import subprocess
#
# completed = subprocess.run(['ls', '-1'])
# print('returncode:', completed.returncode)
#
import subprocess

completed = subprocess.run(
    ['ls', '-1'],
    stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)

# du -sh to find the size of all the files

