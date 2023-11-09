# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#          Mathieu Tachon <tachon.mathieu@protonmail.com>
#
# Copyright (c) 2022 Tom Kralidis
# Copyright (c) 2023 Mathieu Tachon
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================


from enum import Enum
from pathlib import Path
from pkgutil import get_loader
from typing import Union


class SchemaType(Enum):
    item = 'item'
    create = 'create'
    update = 'update'
    replace = 'replace'


def remove_required_from_schema(schema: dict) -> None:
    """Remove all properties from the 'required' list(s) in a schema.

    The function remove all 'required' lists in a schema (`dict` instance). If
    the schema is a nested dictionary, the 'required' lists will be removed at
    all nesting levels.

    :param schema: input schema.
    :type schema: `dict`
    """
    _ = schema.pop('required', None)
    for k, v in schema.items():
        if isinstance(v, dict):
            remove_required_from_schema(v)
        if isinstance(v, list):
            for el in v:
                if isinstance(el, dict):
                    remove_required_from_schema(el)


def get_schema_path(filename: str) -> Union[Path, None]:
    """Get the absolute path of a schema from the schemas directory.

    The function searches recursively in the pygeoapi/schemas directory and its
    subdirectories for a file with a given filename. If a file with the given
    filename is found, the function returns its absolute path, else `None`.

    :param filename: filename fo the file to be found.
    :type filename: `str`

    :returns: path of the file with the given filename if found, else `None`
    :rtype: `Union[Path, None]`
    """
    schemas_dir = Path(get_loader('pygeoapi').path).parent / 'schemas'
    return next((schemas_dir.rglob(f'**/{filename}')), None)
