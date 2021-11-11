import urllib.request
import configparser
import os

def TemplateIndex():
    if os.path.isfile("PackageIndexURL.ini") is False:
        Index = configparser.ConfigParser()
        Index['Index URL'] = {'URL':
                              'https://raw.githubusercontent.com/Aetopia/Basic-Package-Manager/main/Indexes/Packages.ini'}
        with open("PackagesIndexURL.ini",'w') as IndexURL:
            Index.write(IndexURL)

def GetPackageURL(Package):
    TemplateIndex()
    PackageIndex = configparser.ConfigParser(interpolation=None)
    PackageIndex.read("Packages.ini")
    PackageURL=PackageIndex['Packages'][str(Package)]
    return PackageURL

def GetIndexFile():
    TemplateIndex()
    Index = configparser.ConfigParser(interpolation=None)
    Index.read("PackagesIndexURL.ini")
    Index_URL=Index['Index URL']['URL']
    urllib.request.urlretrieve(Index_URL, "Packages.ini")
