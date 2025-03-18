from glob import glob
from xml.etree import ElementTree
from tqdm.notebook import tqdm

# we gathered a list of decompiled apps in the ./decompiled/ folder
manifests = list(glob("decompiled/**/AndroidManifest.xml", recursive=True))
print(f"Found {len(manifests)} manifests")

for manifest in manifests:
    #print(manifest)
    root = ElementTree.parse(manifest).getroot()
    application = root.find("application")
    if not application:
        continue
    for element in application:
        #print(element.attrib)
        class_name = element.attrib.get('{http://schemas.android.com/apk/res/android}name')
        permissions = element.attrib.get('{http://schemas.android.com/apk/res/android}permission')
        exported = element.attrib.get('{http://schemas.android.com/apk/res/android}exported')
        read_permission = element.attrib.get('{http://schemas.android.com/apk/res/android}readPermission')
        write_permission = element.attrib.get('{http://schemas.android.com/apk/res/android}writePermission')
        if not class_name or class_name.startswith("com.google.android"):
            continue
        if exported == "true" and not permissions and not read_permission and not write_permission:
            print(f"{element.tag}: {class_name} | {permissions}")