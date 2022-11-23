import os
import platform
import zipfile

import requests


def chromedriver(path):
    c_version = str(os.popen("mdls -raw -name kMDItemVersion '/Applications/Google Chrome.app'").read())
    c_major_version = str(c_version).split(".")[0]
    print(f"Detected Chrome version {c_version}")
    d_version = requests.get(f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{c_major_version}").text
    print(f"Best driver version candidate: {d_version}")
    d_filename = "chromedriver_mac_arm64.zip" if platform.machine() == "arm64" else "chromedriver_mac64.zip"
    d_url = f"https://chromedriver.storage.googleapis.com/{d_version}/{d_filename}"
    print(f"Downloading {d_url}")
    with requests.get(d_url, stream=True) as r:
        r.raise_for_status()
        with open("/tmp/chromedriver.zip", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"Unzipping {d_filename} to {path}")
    with zipfile.ZipFile("/tmp/chromedriver.zip", "r") as z:
        z.extractall(path)

    print(f"Fixing permissions on {path}/chromedriver")
    os.chmod(f"{path}/chromedriver", 0o755)


if __name__ == "__main__":
    print("This isn't intended to be run directly, go run main.py")
