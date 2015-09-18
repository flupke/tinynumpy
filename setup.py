from distutils.core import setup


setup(
    name='tinynumpy',
    version='1.2.0.dev1',

    description='A lightweight, pure Python, numpy compliant ndarray class',
    author='Wade Brainerd, Almar Klein',
    author_email='wadetb@gmail.com',
    url='https://github.com/wadetb/tinynumpy', # use the URL to the github repo
    # download_url='https://github.com/peterldowns/mypackage/tarball/0.1',
    keywords=['Science', 'Research', 'Engineering', 'Software Development'],
    classifiers=[],

    py_modules=['tinynumpy', 'tinylinalg'],
    package_dir={'': 'tinynumpy'},
)
