import subprocess
class PingDevice:
    def __init__(self, host):
        self.host = host

    def ping(self):
        try:
            output = subprocess.check_output(["ping", "-c", "1", self.host])
            return True
        except subprocess.CalledProcessError:
            return False
