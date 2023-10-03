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
from typing import Dict, List, Optional

from pydantic import conint
from pydantic.json_schema import GenerateJsonSchema

from pygeoapi.models.geojson import (
    create_geojson_feature_model, create_geojson_feature_collection_model,
    GeoJSONProperty, GeomType,
)


# Enum of data schema types depending on request action
class SchemaType(Enum):
    item = 'item'
    create = 'create'
    update = 'update'
    replace = 'replace'


def exclude_properties_default(properties: List[str], schema: Dict) -> None:
    """Remove the default value for given properties in a schema.

    The function remove all default values for the listed properties in a
    schema (`dict` instance). If the schema is a nested dictionary, the default
    values will be removed at all nesting levels.

    :param: list of properties to remove the default value for.
    :type properties: List[str]
    :param schema: input schema.
    :type schema: dict
    """
    for k, v in schema.items():
        if k in properties:
            _ = v.pop('default', None)
        if isinstance(v, dict):
            exclude_properties_default(properties, v)


class GeoJsonSchemaGenerator(GenerateJsonSchema):
    """Subclass of `GenerateJsonSchema` to customize JSON schema generation.
    """

    def generate(self, schema, mode='validation'):
        """Override `GenerateJsonSchema.generate` and remove default values for
        'bbox' and 'id' properties in the generated schema.
        """
        json_schema = super().generate(schema, mode=mode)
        exclude_properties_default(
            properties=['bbox', 'id'], schema=json_schema,
        )
        return json_schema


def get_geojson_feature_schema(
    properties: Optional[List[GeoJSONProperty]] = None,
    geom_type: Optional[GeomType] = None,
    geom_nullable: bool = True,
    n_dims: conint(gt=1) = 2,
) -> dict:
    """Get JSON schema of GeoJSON Feature.

    :param properties: list of feature's properties.
    :type properties: list of `GeoJSONProperty` objects, optional
    :param geom_type: type of GeoJSON geometry.
    :type geom_type: `GeomType`, optional
    :param geom_nullable: whether the geometry of the GeoJSON Feature can be
        set to 'null'.
    :type geom_nullable: bool, default: True
    :param n_dims: number of dimensions of the coordinates of the feature's
        geometry. Must be larger than 1.
    :type n_dims: int, default: 2

    :returns: JSON schema of GeoJSON Feature.
    :rtype: dict

    .. note::
        If ``properties`` and/or ``geom_type`` are not given/set to `None`, a
        GeoJSON Feature will only validate against the returned JSON schema if
        its 'properties' and/or 'geometry' members are set to 'null',
        respectively.
    """
    geojson_feature_model = create_geojson_feature_model(
        properties, geom_type, geom_nullable, n_dims,
    )
    return geojson_feature_model.model_json_schema(
        schema_generator=GeoJsonSchemaGenerator
    )


def get_geojson_feature_collection_schema(
    properties: Optional[List[GeoJSONProperty]] = None,
    geom_type: Optional[GeomType] = None,
    geom_nullable: bool = True,
    n_dims: conint(gt=1) = 2,
) -> dict:
    """Get JSON schema of GeoJSON FeatureCollection.

    :param properties: list of features' properties.
    :type properties: list of `GeoJSONProperty` objects, optional
    :param geom_type: type of GeoJSON geometry.
    :type geom_type: `GeomType`, optional
    :param geom_nullable: whether the geometry of the GeoJSON Features can be
        set to 'null'.
    :type geom_nullable: bool, default: True
    :param n_dims: number of dimensions of the coordinates of the features'
        geometry. Must be larger than 1.
    :type n_dims: int, default: 2

    :returns: JSON schema of GeoJSON FeatureCollection.
    :rtype: dict

    .. note::
        If ``properties`` and/or ``geom_type`` are not given/set to `None`, the
        GeoJSON Features will only validate against the returned JSON schema if
        their 'properties' and/or 'geometry' members are set to 'null',
        respectively.
    """
    geojson_feature_collection_model = create_geojson_feature_collection_model(
        properties, geom_type, geom_nullable, n_dims,
    )
    return geojson_feature_collection_model.model_json_schema(
        schema_generator=GeoJsonSchemaGenerator
    )
