# win-bash-aliases

[![Build status](https://ci.appveyor.com/api/projects/status/1d6m12gd2abb7ndu/branch/master?svg=true)](https://ci.appveyor.com/project/spyoungtech/win-bash-aliases/branch/master)
[![version](https://img.shields.io/pypi/v/win-bash-aliases.svg?colorB=blue)](https://pypi.org/project/win-bash-aliases/) 
[![pyversion](https://img.shields.io/pypi/pyversions/win-bash-aliases.svg?)](https://pypi.org/project/win-bash-aliases/) 


Ever have this problem?

```
C:\Users\You\> vi foo.txt
'vi' is not recognized as an internal or external command,
operable program or batch file.
```

Well, no more! Proxy unix commands to WSL from your Windows native shell with `win-bash-aliases`

Mix windows and bash commands
```
C:\Users\You>dir | grep bytes
               6 File(s)          4,195 bytes
               7 Dir(s)  191,543,554,048 bytes free
```

vi in cmd and powershell!

![vi](https://raw.githubusercontent.com/spyoungtech/win-bash-aliases/master/docs/_static/vi.gif)



## Installation

### Prerequsites

To use this package you must have Windows Subsystem for Linux installed.

```
py -m pip install win-bash-aliases
```

## Commands available

```
awk
cat
cp
curl
grep
less
ls
man
more
mv
nano
rm
ssh
tail
tar
vi
vim
wc
```

Your favorite unix command not here? Open a PR and I'll add it! It's as simple as adding a string to a list.

Note: some commands, like `xargs`, are impractical to use because they would execute inside the WSL environment.

## FAQ

> Is this safe to use in production?

🤷

You should expect some things not to behave perfectly at this stage in development.

> How does it work?

Just console entry points and wrapping around `bash -c`
