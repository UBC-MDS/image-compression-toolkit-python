from distutils.core import setup

setup(
    name='imageCompress',
    version='1.4',
    packages=['imageCompress'],
    scripts=['imageCompress/compress.py', 'imageCompress/crop.py', 'imageCompress/image_size.py'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    url='https://github.com/UBC-MDS/image-compression-toolkit-python',
    download_url='https://github.com/UBC-MDS/image-compression-toolkit-python',
    long_description='open("README.md").read()',
    install_requires=['scikit-image', 'numpy', 'scikit-learn', 'pytest'],
    author='Aditya Sharma | Sayanti Ghosh | Alden Chen'
)
