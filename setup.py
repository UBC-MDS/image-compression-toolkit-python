from distutils.core import setup

setup(
    name='imageCompress',
    version='0.2dev',
    packages=['imageCompress'],
    scripts=['imageCompress/compress.py', 'imageCompress/crop.py', 'imageCompress/image_size.py'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    url='https://github.com/UBC-MDS/image-compression-toolkit-python.git',
    long_description='open("README.md").read()',
    install_requires=['skimage', 'numpy', 'scikit-learn', 'pytest'],
    author='Aditya Sharma | Sayanti Ghosh | Alden Chen'
)
