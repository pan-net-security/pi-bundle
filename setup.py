from distutils.core import setup

setup (
    name = "pi",
    version = "0.2.4",
    description = "Cog commands for privacyidea",
    author = "Diogenes Santos de Jesus",
    author_email = "diogenes.jesus@telekom.com",
    url = "https://github.com/pan-net-security/pi-bundle",
    packages = ["pi", "pi.commands"],
    install_requires=['pycog3==0.1.27', 'requests==2.18.4'],
    keywords = ["cog", "privayidea", "otp", "bot", "devops", "chatops", "automation"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ]
)
