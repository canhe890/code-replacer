import paramiko

PY_PATH = '/usr/lib/python2.7/site-packages/'
TAR_CMD = 'tar -czf %s.tar.gz %s'
RM_CMD = 'rm -rf %s'
CHMOD_CMD = 'chmod %s -R %s'


class CodeReplacer(object):
    def __init__(self, ip, user, pwd):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(ip, 22, user, pwd)
        self.sftp_client = paramiko.SFTPClient.from_transport(self.ssh_client.get_transport())

    def replace(self, localpath):
        pass

    def _tar(self, path):
        self.ssh_client.exec_command(TAR_CMD % (path, PY_PATH + path))

    def _verify(self, path):
        pass

    def _remove(self, path):
        self.ssh_client.exec_command(RM_CMD % (PY_PATH + path))

    def _upload(self, localpath):
        self.sftp_client.put(localpath, '/root')

    def _chmod(self, path):
        self.ssh_client.exec_command(CHMOD_CMD % ('755', PY_PATH + path))

    def close(self):
        self.ssh_client.close()
