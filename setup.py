from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# version from your app
from biometric_attendance import __version__ as version

setup(
    name="biometric_attendance",
    version=version,
    description="Auto Sync for HRMS",
    author="nischal",
    author_email="nischalraj3003@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)