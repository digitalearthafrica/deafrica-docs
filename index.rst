.. Digital Earth Africa documentation master file, created by
   sphinx-quickstart on Wed Feb 17 00:08:26 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Digital Earth Africa User Guide
===============================

The `Digital Earth Africa <https://www.digitalearthafrica.org/>`_ platform
consists of a repository of Earth Observation data and a set of tools to
view and analyse that data.

.. toctree::
   :hidden:

   Home <self>

Data
====

.. toctree::
   :hidden:
   :caption: Data
   :maxdepth: 1

   data_specs/index


.. container:: platform-list

   .. container:: product-item

      .. image:: _static/data_specs/S2_thumbnail.png
         :target: ./data_specs/
         :align: left

      :doc:`data_specs/index`

      Access up-to-date technical specifications of all Digital Earth Africa datasets

      :doc:`More <data_specs/index>`
   

Platforms
=========

.. toctree::
   :hidden:
   :caption: Platforms
   :maxdepth: 1

   maps/index
   sandbox/index
   web_services/index
   web_services/access
   maps/geoportal
   web_services/explorer
   odc_stac/odc_stac


.. container:: platform-list

   .. container:: product-item

      .. image:: _static/maps/Workbench.jpg
         :target: ./maps/
         :align: left

      :doc:`maps/index`

      Our user friendly map-based access to DE Africa data and products

      :doc:`More <maps/index>`


   .. container:: product-item

      .. image:: _static/sandbox/sandbox_mini.png
         :target: ./sandbox/
         :align: left

      :doc:`sandbox/index`

      Our JupyterLab Analysis Platform for exploring the data with access to analysis tools

      :doc:`More <sandbox/index>`


   .. container:: product-item

      .. image:: _static/data_specs/ST_thumbnail.png
         :target: ./maps/
         :align: left

      :doc:`web_services/index`

      Access to DE Africa data from QGIS or ArcGIS using Web Map Service and Web Coverage Service

      :doc:`More <web_services/index>`


   .. container:: product-item

      .. image:: _static/data_specs/Landsat_thumbnail.png
         :target: ./web_services/access.html
         :align: left

      :doc:`web_services/access`

      Directly access the data and metadata from cloud data storage

      :doc:`More <web_services/access>`


   .. container:: product-item

      .. image:: _static/maps/geoportal_logo.png
         :target: ./maps/geoportal.html
         :align: left

      :doc:`maps/geoportal`

      Imagery from DE Africa is available in Esri’s Africa GeoPortal, providing geospatial tools, data and training

      :doc:`More <maps/geoportal>`


   .. container:: product-item

      .. image:: _static/web_services/metadata.png
         :target: ./web_services/explorer.html
         :align: left

      :doc:`web_services/explorer`

      The Metadata Explorer allows you to see where and when you can find data

      :doc:`More <web_services/explorer>`


   .. container:: product-item

      .. image:: _static/odc_stac/odc_stac_thumbnail.png
         :target: ./odc_stac/odc_stac.html
         :align: left

      :doc:`odc_stac/odc_stac`

      The odc-stac allows you to load STAC items into `xarray` Datasets.

      :doc:`More <odc_stac/odc_stac>`


.. toctree::
   :caption: About
   :hidden:
   :maxdepth: 1

   about/contact
   about/training
   about/glossary
   genindex

