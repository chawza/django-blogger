from setuptools import setup, find_packages

setup(
    name='django-reusable-blog',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
        'markdown>=3.3',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A reusable Django blog application',
    # long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/django-reusable-blog',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
)
