from glob import glob
from os.path import basename, isdir
from lxml import etree
from subprocess import Popen

def getSnapperTree():
    """Get Tree from snapshots
    
    :Example
    
    {'root': {'name': 'root', 'fstype': 'btrfs', 'snapshots': [{'uid': '0', 'description': '', 'number': '84', 'type': 'single', 'pre': None, 'cleanup': 'Unknown', 'date': '2016-11-28 11:44:36'}, {'uid': '0', 'description': '', 'number': '85', 'type': 'pre', 'pre': None, 'cleanup': 'number', 'date': '2016-12-11 10:36:41'}, {'uid': '0', 'description': 'test12345 Example', 'number': '86', 'type': 'single', 'pre': None, 'cleanup': 'number', 'date': '2016-12-11 11:10:28'}], 'subvolume': '/'}}
    
    :return: List of snapshots
    :rtype: list of dict"""
    fullTree = dict()
    # If file configs don't exist in /etc/snapper/configs/, return an 'error dictionnary'. 
    if not isdir("/etc/snapper/configs/"):
        fullTree = {"error":"Directory /etc/snapper/configs not found"}
        return fullTree
    
    # Get list of all configs
    for fileentry in glob("/etc/snapper/configs/*"):
        subvolume = ""
        fstype = ""
        name = basename(fileentry)
        # Open file for extract informations
        # SUBVOLUME, FSTYPE and filename of course 
        with open(fileentry, "r") as ins:
            for line in ins:
                line = line.strip()
                splitted = line.split("=")
                if splitted[0] == "SUBVOLUME":
                    # Get subvolume (path) of snapshot, and extract it.
                    subvolume = splitted[1][1:-1]
                elif splitted[0] == "FSTYPE":
                    # Get type of FS.
                    fstype = splitted[1][1:-1]
                    
        if fstype != "" and subvolume != "":
            # Get list of snapshots from this config.
            list_from_path = subvolume + "/.snapshots/"
            snapshots = dict()
            for direntry in glob(list_from_path + "/*"):
                # Read information from info.xml
                config_file = direntry + "/info.xml"
                tree = etree.parse(config_file)
                
                snaptype = tree.xpath("/snapshot/type")[0].text
                snapdate = tree.xpath("/snapshot/date")[0].text
                try:
                    snapcleanup = tree.xpath("/snapshot/cleanup")[0].text
                except IndexError:
                    snapcleanup = "Unknown"
                try:
                    snapdesc = tree.xpath("/snapshot/description")[0].text
                except IndexError:
                    snapdesc = ""
                try:
                    uid = tree.xpath("/snapshot/uid")[0].text
                except IndexError:
                    uid = ""
                num_dir = basename(direntry)
                if snaptype == "post":
                    associated =  tree.xpath("/snapshot/pre_num")[0].text
                else:
                    associated = None
                snapshotline = {"number":num_dir, "uid":uid, "description":snapdesc, "date":snapdate, "type":snaptype, "cleanup":snapcleanup , "pre":associated}
                snapshots[num_dir] = (snapshotline)
                
                
            fullTree[name] = {"name":name, "subvolume":subvolume, "fstype":fstype, "snapshots":snapshots}
    return fullTree

    
