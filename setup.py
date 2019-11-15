
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
      include_package_data=True,
      install_requires=requires
     )