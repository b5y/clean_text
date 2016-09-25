import os
import pytest

from clean_text.cleaner import (rename_file,
                                get_files,
                                read_and_process_file,
                                clean_text)

# For testing locally:
DIR_TEST_FILES = '.' + os.sep + 'tests' + os.sep + 'test_samples'


@pytest.fixture()
def files():
    return DIR_TEST_FILES


def test_get_files(files):
    list_of_files = []
    list_of_files.extend(get_files(files))
    assert list_of_files is not False


def test_read_and_process_file(files):
    file_ = DIR_TEST_FILES + os.sep + os.listdir(files)[0]
    read_and_process_file(file_)
    assert os.path.isfile(file_) is True
    assert isinstance(file_, basestring) is True
    new_file = rename_file(file_)
    assert os.path.isfile(new_file)
    os.remove(new_file)
    fake_file = os.listdir(files)[0]
    assert os.path.isfile(fake_file) is False
