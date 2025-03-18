import subprocess
import re
from tqdm.notebook import tqdm

ADB = "/Users/user/Library/Android/sdk/platform-tools/adb" ## change this to your adb path
#JADX = "/Users/user/tools/jadx/jadx-1.5.1/bin/jadx"

pm_list_packages = subprocess.check_output([ADB, "shell", "pm", "list", "packages", "-f"], text=True)
for package in tqdm(pm_list_packages.splitlines(), desc="Pulling apks"):
    # package:/data/app/~~3yZz2YMGTSgaoNHr_k2fpw==/com.google.android.apps.photos--3_7vfJlMnNMgZMyEXVrvw==/base.apk=com.google.android.apps.photos
    match = re.match(r"package:(.*\.apk)=(.*)", package)
    apk_path = match.group(1)
    package_name = match.group(2)
    subprocess.run([ADB, "pull", apk_path, f"apks/{package_name}.apk"])
    # decompile apk with jadx
    #subprocess.run([JADX, "-d", f"decompiled/{package_name}", f"apks/{package_name}.apk"])