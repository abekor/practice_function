import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='practice_function',
    version='0.0.1',
    author='Mike Huls',
    author_email='a.kor@metricsflow.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/abekor/practice_function',
    project_urls = {
        "Bug Tracker": "https://github.com/abekor/practice_function/issues"
    },
    license='MIT',
    packages=['practice_function'],
    install_requires=['requests'],
)
