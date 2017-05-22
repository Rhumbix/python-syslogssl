from setuptools import setup

setup(name='syslogssl',
      version='0.1',
      description='RFC 5424 TLS',
      long_description='Provides Syslog over TLS conformant to the RFC 5424 descriptions of the protocol',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
      ],
      keywords='syslog',
      url='https://github.com/lhl/python-syslogssl',
      author='lhl',
      author_email='',
      license='MIT',
      packages=['syslogssl'],
      install_requires=[ ],
      include_package_data=True,
      zip_safe=False)
