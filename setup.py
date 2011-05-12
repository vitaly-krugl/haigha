import haigha
import os
from distutils.core import setup


requirements = map(str.strip, open('requirements.txt').readlines())

setup(
    name='haigha',
    version=haigha.VERSION,
    author='Vitaly Babiy, Aaron Westendorf',
    author_email="vbabiy@agoragames.com, aaron@agoragames.com",
    packages = ['haigha'],
    install_requires = requirements,
    url='https://github.com/agoragames/haigha',
    license="LICENSE.txt",
    long_description=open('README.txt').read(),
    keywords=['python', 'amqp', 'event', 'rabbitmq'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Topic :: Communications",
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
    ]
)
