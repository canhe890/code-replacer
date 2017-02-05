import paramiko

IP = '54.254.245.134'
USER = 'root'
PWD = 'cnp200@HW'
PY_PATH = '/usr/lib/python2.7/site-packages/'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(IP, 22, USER, PWD)

cmd = 'tar -czf hchc.tar.gz %s%s' % (PY_PATH, 'hchc')

stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.readlines())
ssh.close()
