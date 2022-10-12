import sys
import argparse
from getpass import getpass

def add_file(args):
    print(args.add)
    if not args.passphrase and not args.key:
        print("Passphrase/Key? [p/k] ",end='')
        op=input()
        while op!='k' and op!='p':
            print("Passphrase/Key? [p/k] ",end='')
            op=input()
        if op=='p':
            passphrase=getpass("Passphrase:")
            print(passphrase)
        else:
            print("key: ",end='')
            key=input()
    else:print(args.passphrase)

if __name__=="__main__":
    try:
        parser=argparse.ArgumentParser()
        parser.add_argument('-a','--add',metavar="FILE",help="add file to vault")
        parser.add_argument('-e','--extract',metavar="FILE",help="extract file from vault")
        parser.add_argument('-c','--clear',metavar="FILE",help="clear file")
        parser.add_argument('-p','--passphrase',metavar="PASSPHRASE",help="passphrase")
        parser.add_argument('-k','--key',metavar="KEY",help="32 bytes hex key")
        args=parser.parse_args()
        if args.add:add_file(args)
        # for idx,arg in enumerate(sys.argv):
        #     print(arg)

    except(KeyboardInterrupt):
        print("Terminated")
