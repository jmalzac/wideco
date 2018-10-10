from setuptools import setup

setup(
    name='jushack', 
    version='1.0.1',
    description='Hacked coffee machine Skill',
    author='Snips Labs',
    url='',
    download_url='',
    license='MIT',
    install_requires=['pyserial', 'configparser','netaddr', ' pycryptodome'],
    test_suite="tests",
    keywords=['snips', 'jus'],
    packages=['jushack'],
    package_data={'jushack': ['Snipsspec']},
    include_package_data=True
)
