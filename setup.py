from setuptools import setup


from win_aliases import aliases


def console_scripts():
    scripts = []
    for alias in aliases:
        s = f'{alias} = win_aliases.__init__:{alias}'
        scripts.append(s)
    return scripts


def long_description():
    with open('README.md') as f:
        readme = f.read()

setup(
    name='win-bash-aliases',
    version='0.0.3',
    url='https://github.com/spyoungtech/win-bash-aliases/',
    license='MIT',
    author='Spencer Young',
    author_email='spencer.young@spyoung.com',
    description='Windows WSL bash aliases for cmd and powershell',
    long_description=long_description(),
    long_description_content_type="text/markdown",
    packages=['win_aliases'],
    install_requires=[],
    entry_points={
        'console_scripts': console_scripts()
    },
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
