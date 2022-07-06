Direct access
=============

Amazon Web Services (AWS) S3 Bucket
____________________________________
Digital Earth Africa data is stored on Amazon Web Services in several publicly
accessible S3 buckets.

These buckets are:

* ``deafrica-landsat``
* ``deafrica-sentinel-1``
* ``deafrica-sentinel-2``
* ``deafrica-input-datasets``
* ``deafrica-services``

For information on where products can be found, see :ref:`data_specs`.

More information on inventory and notification services for some of the buckets can be found on their respective
datasets pages on the
`Digital Earth Africa Registry of Open Data on AWS <https://registry.opendata.aws/collab/deafrica/>`_

These buckets are in the AWS region ``af-south-1`` (Capetown).

To list the contents of a bucket using the `AWS Command Line <https://docs.aws.amazon.com/cli/latest/userguide/>`_::

    aws s3 ls --region=af-south-1 s3://deafrica-services/ --no-sign-request

Note that you will need to export the environment variable ``export AWS_S3_ENDPOINT=s3.af-south-1.amazonaws.com``
to be able to use some tools such as GDAL to access the data.


Cloud Optimized GeoTIFFs (COG)
______________________________
Most of the products in Digital Earth Africa are available as Cloud Optimized
GeoTIFF (:term:`COG`) files.

For more information on using these files, see the
`Cloud Optimized GeoTIFF <https://www.cogeo.org/>`_ site.

For using COGs on S3 with QGIS, see the tutorial `How to read a Cloud
Optimized GeoTIFF with QGIS <https://www.cogeo.org/qgis-tutorial.html>`_.

To convert an S3 path to a direct HTTPS link that you can use in many applications,
use the following format: ``https://<bucket>.s3.<region>.amazonaws.com/<key>`` where bucket
is the name of the bucket, the region is ``af-south-1` and key is the path to the file.


Spatio-Temporal Asset Catalog (STAC)
___________________________________

The SpatioTemporal Asset Catalog (STAC) specification provides a common
language to describe a range of geospatial information, so it can more easily
be indexed and discovered. A **'spatiotemporal asset'** is any file that
represents information about Earth captured in a certain space and time.

The DE Africa STAC endpoint is:

https://explorer.digitalearth.africa/stac/

For more information, see the
`SpatioTemporal Asset Catalog <https://stacspec.org/>`_ site and the
`DE Africa odc-stac example <odc_stac.ipynb>`_.
