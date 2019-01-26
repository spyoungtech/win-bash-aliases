from setuptools import setup


from win_aliases import aliases


def console_scripts():
    scripts = []
    for alias in aliases:
        s = f'{alias} = win_aliases.__init__:{alias}'
        scripts.append(s)
    return scripts


setup(
    name='win_aliases',
    version='0.0.1',
    url='https://github.com/spyoungtech/win_aliases/',
    license='MIT',
    author='Spencer Young',
    author_email='spencer.young@spyoung.com',
    description='Windows WSL bash aliases for cmd and powershell',
    packages=['win_aliases'],
    install_requires=[],
    entry_points={
        'console_scripts': console_scripts()
    },
    classifiers=[
        'Programming Language :: Python',
    ],
)
