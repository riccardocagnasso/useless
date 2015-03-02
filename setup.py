from setuptools import setup, find_packages

print(find_packages('src'))

setup(
    name="Useles2s",
    version='0.1',
    author='Riccardo Cagnasso',
    author_email="riccardo@phascode.org",
    description='Useless is useless. Oh yeah, and parses bit and pieces' +
                'of ELF and PE dynamic libraries',
    license="MIT",
    packages=find_packages('src'),
    package_dir={'useless': 'src/useless/',
                 'useless.elf': 'src/useless/elf/'},

    scripts=['src/usls.py'],
    install_requires=[
        'cached_property',
        'prettytable'])
