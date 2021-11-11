# Modules
import configparser
import subprocess
import index

# ["powershell", "iex", '"&', '{$(irm', PackageURL+")}", '(Option)"']

def PackageInstall(PackageName):
    PackageURL=index.GetPackageURL(str(PackageName))
    subprocess.run(["powershell", "iex", '"&', '{$(irm', PackageURL+")}", 'install"'])

def PackageRemove(PackageName):
    PackageURL=index.GetPackageURL(str(PackageName))
    subprocess.run(["powershell", "iex", '"&', '{$(irm', PackageURL+")}", 'remove"'])

def PackageUpdate(PackageName):
    PackageURL=index.GetPackageURL(str(PackageName))
    subprocess.run(["powershell", "iex", '"&', '{$(irm', PackageURL+")}", 'update"'])       

    
