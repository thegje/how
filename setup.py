from setuptools import setup

setup(
    name="how",
    version="0.1",
    scripts=["how.py"],
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "how = how:main"  # 'howdo' command runs main()
        ]
    }
)