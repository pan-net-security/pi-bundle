from distutils.core import setup

setup (
    name = "pi",
    version = "0.2.4",
    description = "Cog commands for privacyidea",
    author = "Diogenes Santos de Jesus",
    author_email = "diogenes.jesus@telekom.com",
    url = "https://github.com/pan-net-security/pi-bundle",
    packages = ["pi", "pi.commands", "pi.commands.token"],
    # can't refer to git addresses here so commenting
    # until pycog3 0.1.28 is available
    # install_requires=['requests==2.18.4',
    #                   'certifi==2017.7.27.1',
    #                   'chardet==3.0.4',
    #                   'idna==2.6',
    #                   'requests==2.18.4',
    #                   'urllib3==1.22'],
    keywords = ["cog", "privayidea", "otp", "bot", "devops", "chatops", "automation"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License"
    ]
)
