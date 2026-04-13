from pathlib import Path

from setuptools import find_packages, setup


def read_requirements():
    requirements_path = Path("requirements.txt")

    for encoding in ("utf-8-sig", "utf-16", "utf-16-le"):
        try:
            lines = requirements_path.read_text(encoding=encoding).splitlines()
            break
        except UnicodeDecodeError:
            continue
    else:
        lines = requirements_path.read_text(errors="ignore").splitlines()

    requirements = []
    for line in lines:
        dependency = line.strip()
        if not dependency or dependency.startswith("#"):
            continue
        if dependency.startswith("-e ") or ":\\" in dependency:
            continue
        requirements.append(dependency)

    return requirements


setup(
    name="ANIME-RECOMMENDER",
    version="0.1",
    author="Eduardo Sousa",
    packages=find_packages(),
    install_requires=read_requirements(),
)
