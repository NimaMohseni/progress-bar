from distutils.core import setup

NAME = "progressbar"

DESCRIPTION = "progress bar for 'for' loops"

KEYWORDS = "For Loop Progress Bar Repository"

AUTHOR = "Nima Mohseni"

AUTHOR_EMAIL = "nimamohseni.w@gmail.com"

URL = "https://github.com/NimaMohseni/progressbar"

VERSION = "1.0.0"


setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    packages =['progressbar','progressbar.function',] ,
)
