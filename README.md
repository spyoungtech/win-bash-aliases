# win_aliases

Ever have this problem?

```
C:\Users\You\> vi foo.txt
'vi' is not recognized as an internal or external command,
operable program or batch file.
```

Well, no more! Proxy unix commands to WSL from your Windows native shell with `win_aliases`

## Installation

### Prerequsites

To use this package you must have Windows Subsystem for Linux installed.

```
pip install win_aliases
```

## Commands available

```
awk
cat
cp
curl
grep
ls
lsof
man
mv
nano
rm
ssh
tail
tar
vi
vim
```

Your favorite unix command not here? Open a PR and I'll add it! It's as simple as adding a string to a list.

Note: some commands, like `xargs`, are impractical to use because they would execute inside the WSL environment.