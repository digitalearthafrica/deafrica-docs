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


.. warning::
    While Digital Earth Africa is committed to releasing its data to the public
    for free, the unfortunate reality is that data leaving (data egress) the AWS
    region incurs a non-trivial cost to DEA. In the future, to avoid out of
    control costs for hosting our data, we may need to enable "Requester Pays" on
    the data provided here.

    This will mean:
     * Data that is transferred from this bucket to AWS compute resources and
       services within the AWS region will remain free of cost;
     * All other downloads will require a user have an AWS account, this AWS
       account will incur the charges for data egress.

    If you would like to avoid disruption if and when and if this change is
    applied, you will need to configure your S3 download client to use an AWS
    account/identity and send the accept requester pays header
    ``x-amz-request-charged:requester`` most clients offer a simple checkbox or
    configuration flag to accept requester pays.


Cloud Optimized GeoTIFF (COG)
______________________________
Most of the products in Digital Earth Africa are available as Cloud Optimized
GeoTIFF (:term:`COG`) files.

For more information on using these files, see the
`Cloud Optimized GeoTIFF <https://www.cogeo.org/>`_ site.

For using COGs on S3 with QGIS, see the tutorial `How to read a Cloud
Optimized GeoTIFF with QGIS <https://www.cogeo.org/qgis-tutorial.html>`_.


SpatioTemporal Asset Catalog (STAC)
___________________________________

The SpatioTemporal Asset Catalog (STAC) specification provides a common
language to describe a range of geospatial information, so it can more easily
be indexed and discovered. A **'spatiotemporal asset'** is any file that
represents information about Earth captured in a certain space and time.

The DE Africa STAC endpoint is:

https://explorer.digitalearth.africa/stac/

For more information, see the
`SpatioTemporal Asset Catalog <https://stacspec.org/>`_ site.
