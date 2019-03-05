import subprocess
import sys

aliases = {'vi',
           'cp',
           'grep',
           'mv',
           'rm',
           'tail',
           'awk',
           'ssh',
           'cat',
           'tar',
           'curl',
           'man',
           'nano',
           'ls',
           'vim',
           'more',
           'less',
           'wc',
           'dig',
           'host',
           'ss',
           'zip',
           'unzip',
           'gzip',
           'sed',
           }

def make_alias(alias):
    def bash_alias():
        args = ' '.join(sys.argv[1:])
        if args:
            cmd = alias + ' ' + args.replace('\\', '/')
        else:
            cmd = alias
        command = ['bash', '-c', cmd]
        subprocess.run(command)
    return bash_alias


for alias in aliases:
    bash_alias = make_alias(alias)
    globals()[alias] = bash_alias

