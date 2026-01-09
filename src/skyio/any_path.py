import os
import sys
import typing
from pathlib import Path as _Path_

try:
    from pathlib import _posix_flavour, _windows_flavour
except ImportError:
    _posix_flavour = _windows_flavour = None

if typing.TYPE_CHECKING:
    from . import GenericPath
    from .local_path import LocalPath
    from .cloud_path import CloudPath


class AnyPath(_Path_):
    """
    GenericPath class is an abstract class
    """
    if sys.version_info < (3, 12):
        _flavour = _windows_flavour if os.name == "nt" else _posix_flavour

    def upload_to(
        self,
        destination: typing.Union[str, "GenericPath", "CloudPath"],
        *args,
        **kwargs,
    ) -> "CloudPath":
        """
        Upload a file to a destination.
        :param destination: Destination path
        """
        raise NotImplementedError

    def get_mapper(self, *args, **kwargs):
        """
        Get the mapper
        :param args: Arguments
        :param kwargs: Keyword arguments
        :return: Mapper
        """
        raise NotImplementedError

    def download_to(
        self,
        destination: typing.Union[str, "GenericPath", "LocalPath"],
        *args,
        **kwargs,
    ) -> "LocalPath":
        """
        Download a file to a destination.
        :param destination: Destination path
        """
        raise NotImplementedError
