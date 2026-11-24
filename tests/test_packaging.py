"""Check that the wheel's package discovery excludes the source tests."""

from os import path
import runpy

import setuptools


def test_only_viewer_packages_are_distributed(monkeypatch):
    metadata = {}
    monkeypatch.setattr(setuptools, 'setup', lambda **options: metadata.update(options))
    source = path.dirname(path.dirname(path.abspath(__file__)))
    monkeypatch.chdir(source)
    runpy.run_path(path.join(source, 'setup.py'))

    packages = metadata['packages']
    assert 'panda3d_viewer' in packages
    assert all(package.split('.')[0] == 'panda3d_viewer' for package in packages)
