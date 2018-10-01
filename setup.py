import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PCRCalc',
    version='1.0.3',
    url='https://github.com/Godrigos/PCRCalc',
    license='GPL-3.0',
    author='Rodrigo Aluizio',
    author_email='',
    description='A PCR Mix Calculator',
    long_description=long_description,
    entry_points={'gui_scripts': ["PCRCalc = ui.py"]},
    package_data={
        '': ['images/*.png', 'presets/*.json', 'pcrcalc.ico'],
    },
    install_requires=['json', 'pillow', 'reportlab', 'ttkthemes'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
)

