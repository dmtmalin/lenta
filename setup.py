#!/usr/bin/env python
import os
import sys

from setuptools import setup, find_packages, Command

sys.path.insert(0, 'src')

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


class BowerInstallCommand(Command):
    user_options = []

    description = 'run bower install command'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        cmd = ['bower', 'install']
        self.spawn(cmd)

requires = [
    'Django==1.9.9',
    'architect==0.5.4',
    'psycopg2==2.6.2',
    'celery==3.1.23',
    'django-celery==3.1.17',
    'feedparser==5.2.1',
    'mixer==5.5.7',
    'redis==2.10.5',
    'reportlab==3.3.0',
    'trml2pdf==0.4',
    'unidecode==0.4.19',
]

setup(
    name='lenta',
    version='0.0.1',
    keywords='web django',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/dmtmalin/lenta',
    license='BSD License',
    author='dmt.malin',
    author_email='dmt.malin@gmail.com',
    description='Simple RSS digest',
    long_description=README,
    include_package_data=True,
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'lenta = lenta.manage:main',
        ]
    },
    cmdclass={
        'bower_install': BowerInstallCommand,
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)