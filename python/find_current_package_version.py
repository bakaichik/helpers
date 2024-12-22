import pkg_resources
from pathlib import Path

# List of imported packages
packages = [
    "torch",
    "nltk",
    "matplotlib",
    "pathlib",
    "json",
]

# Get package versions
package_versions = {}
for package in packages:
    try:
        package_versions[package] = pkg_resources.get_distribution(
            package).version
    except pkg_resources.DistributionNotFound:
        package_versions[package] = "Not Installed"

# File to write
requirements_file = Path("requirements.txt")

# Write versions to the file
with requirements_file.open("w") as file:
    for pkg, ver in package_versions.items():
        if ver != "Not Installed":
            file.write(f"{pkg}=={ver}\n")
