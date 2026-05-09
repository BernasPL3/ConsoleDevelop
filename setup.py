from setuptools import setup

APP = ['main.py']

OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'ConsoleDevelop',
        'CFBundleDisplayName': 'ConsoleDevelop',
        'CFBundleIdentifier': 'com.consoledevelop.app',
        'CFBundleVersion': '1.0.0',
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
