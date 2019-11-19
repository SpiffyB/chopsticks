
from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(name='chopsticks',
      version='1.0',
      description='chopsticks game',
      author='Tom MacArthur & Luca Bianchi',
      packages=find_packages(),
      url="https://github.com/SpiffyB/chopsticks"
      include_package_data=True,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
        ],
      python_requires='>=3.6',
      install_requires=requires
     )