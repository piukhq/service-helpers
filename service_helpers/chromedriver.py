import os
import platform
import zipfile

import requests


def chromedriver(path):
    c_version = str(os.popen("mdls -raw -name kMDItemVersion '/Applications/Google Chrome.app'").read())
    print(f"Detected Chrome version {c_version}")
    c_semver = ".".join(c_version.split(".")[:3])
    available_versions = requests.get(
        "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"
    ).json()
    best_version = [version for version in available_versions["versions"] if c_semver in version["version"]][-1]
    print(f"Best Chrome Driver Version: {best_version['version']}")
    platform_type = "mac-arm64" if platform.processor() == "arm" else "mac-x64"
    url = next(
        download for download in best_version["downloads"]["chromedriver"] if download["platform"] == platform_type
    )["url"]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open("/tmp/chromedriver.zip", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"Unzipping chromedriver to {path}")
    with zipfile.ZipFile("/tmp/chromedriver.zip", "r") as z:
        for file in z.infolist():
            file.filename = os.path.basename(file.filename)
            if file.filename == "chromedriver":
                z.extract(file, path=path)

    print(f"Fixing permissions on {path}/chromedriver")
    os.chmod(f"{path}/chromedriver", 0o755)


if __name__ == "__main__":
    print("This isn't intended to be run directly, go run main.py")
