# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import skbio
import qiime2


def filter_distance_matrix(distance_matrix: skbio.DistanceMatrix,
                           sample_metadata: qiime2.Metadata,
                           where: str=None) -> skbio.DistanceMatrix:
    ids_to_keep = sample_metadata.ids(where=where)
    # NOTE: there is no guaranteed ordering to output distance matrix because
    # `ids_to_keep` is a set, and `DistanceMatrix.filter` uses its iteration
    # order.
    try:
        return distance_matrix.filter(ids_to_keep, strict=False)
    except skbio.stats.distance.DissimilarityMatrixError:
        raise ValueError(
            "All samples were filtered out of the distance matrix.")
