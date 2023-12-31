import pycounts.data
from importlib_resources import files, as_file
import warnings


def get_flatland():
    """Get path to example "Flatland" [1]_  text file

    Returns
    -------
    pathlib.PosixPath
        path to file.

    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """
    warnings.warn("This function will be deprecated in v1.0.0", FutureWarning)
    
    fixtures = files(pycounts.data).joinpath('flatland.txt')
    with as_file(fixtures) as f:
        data_file_path = f

    return data_file_path
