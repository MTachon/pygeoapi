# =================================================================
#
# Authors: Mathieu Tachon <tachon.mathieu@protonmail.com>
#
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


from pygeoapi.schemas import (remove_required_from_schema, get_schema_path)


def test_remove_required_from_schema():
    """Test that 'required' are removed at all levels.
    """
    schema = {
        'title': 'mySchema',
        'type': 'object',
        'required': ['prop_a', 'prop_b'],
        'properties': {
            'prop_a': {'type': 'number'},
            'prop_b': {
                'type': 'object',
                'required': ['prop_a1'],
                'properties': {
                    'prop_a1': {'type': 'string'},
                    'prop_a2': {'type': 'number'},
                },
            },
        },
    }
    remove_required_from_schema(schema)

    assert schema.get('required') is None
    assert schema['properties']['prop_b'].get('required') is None


def test_get_schema_path():
    """Test that existing schema is found, and test correct behavior for
    non-existing schemas.
    """
    # Test with existing schema
    assert get_schema_path('featureGeoJSON.json').exists()

    # Test with non-existing schema
    assert get_schema_path('not_existing_schema.yml') is None
