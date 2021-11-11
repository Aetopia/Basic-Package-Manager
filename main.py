import argparse
import sys
import os
sys.path.insert(1, 'modules')
import package
import index

# Working Directory
Working_Dir=os.environ["USERPROFILE"]+"\\BasicPKGMGR"
try:
    os.mkdir(Working_Dir)
except:
    pass
os.chdir(Working_Dir)
index.GetIndexFile()

parser=argparse.ArgumentParser(usage="")
command=parser.add_mutually_exclusive_group(required=True)
command.add_argument('-i',
                     nargs=1,
                     metavar="<Package>",
                     help="Install a Package.",
                     action="store")
command.add_argument('-u',
                     nargs=1,
                     metavar="<Package>",
                     help="Update a Package.",
                     action="store")
command.add_argument('-r',
                     nargs=1,
                     metavar="<Package>",
                     help="Remove a Package.",
                     action="store")

args = parser.parse_args()
if args.i != None:
    package.PackageInstall(args.i[0])
elif args.u != None:
    package.PackageUpdate(args.u[0])
elif args.r != None:
    package.PackageRemove(args.r[0])
    
    
