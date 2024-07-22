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

   maps/deafrica_map
   maps/external_web_services
   sandbox/index
   platform_tools/explorer
   maps/geoportal
   platform_tools/web_services_gis
   platform_tools/cube-in-a-box
   platform_tools/direct_access
   platform_tools/odc_stac
   platform_tools/googledrive_access

.. container:: platform-list

   .. container:: product-item

      .. image:: _static/maps/Workbench.jpg
         :target: ./maps/
         :align: left

      :doc:`maps/deafrica_map`

      Our user friendly map-based access to DE Africa data and products

      :doc:`More <maps/deafrica_map>`


   .. container:: product-item

      .. image:: _static/maps/nicfi_maps.jpg
         :target: ./maps/external_web_services.html
         :align: left

      :doc:`maps/external_web_services`
      
      Intergrating external web services into the DE Africa platform.

      :doc:`More <maps/external_web_services>`


   .. container:: product-item

      .. image:: _static/sandbox/sandbox_mini.png
         :target: ./sandbox/
         :align: left

      :doc:`sandbox/index`

      Our JupyterLab Analysis Platform for exploring the data with access to analysis tools

      :doc:`More <sandbox/index>`


   .. container:: product-item

      .. image:: _static/platform_tools/explorer/metadata.png
         :target: ./platform_tools/explorer.html
         :align: left

      :doc:`platform_tools/explorer`

      The Metadata Explorer allows you to see where and when you can find data

      :doc:`More <platform_tools/explorer>`


   .. container:: product-item

      .. image:: _static/maps/geoportal_logo.png
         :target: ./maps/geoportal.html
         :align: left

      :doc:`maps/geoportal`

      Imagery from DE Africa is available in Esri’s Africa GeoPortal, providing geospatial tools, data and training

      :doc:`More <maps/geoportal>`
      

   .. container:: product-item

      .. image:: _static/data_specs/ST_thumbnail.png
         :target: ./platform_tools/
         :align: left

      :doc:`platform_tools/web_services_gis`

      Access to DE Africa data from QGIS or ArcGIS using Web Map Service and Web Coverage Service

      :doc:`More <platform_tools/web_services_gis>`


   .. container:: product-item

      .. image:: _static/platform_tools/cube_in_a_box/cube-in-a-box-thumbnail.png
         :target: ./platform_tools/cube-in-a-box.html
         :align: left

      :doc:`platform_tools/cube-in-a-box`

      The Cube in a Box is a simple way to run the Open Data Cube.

      :doc:`More <platform_tools/cube-in-a-box>`
   
   
   .. container:: product-item
    
      .. image:: _static/data_specs/Landsat_thumbnail.png
         :target: ./platform_tools/direct_access.html
         :align: left
            
      :doc:`platform_tools/direct_access`
        
      Directly access the data and metadata from cloud data storage
        
      :doc:`More <platform_tools/direct_access>`
      

   .. container:: product-item
    
      .. image:: _static/platform_tools/odc_stac/odc_stac_thumbnail.png
         :target: ./platform_tools/odc_stac.html
         :align: left
            
      :doc:`platform_tools/odc_stac`
      
      Load STAC compliant earth observation data as an `xarray.Dataset` from the python environment of your choice.
        
      :doc:`More <platform_tools/odc_stac>`
      
      
   .. container:: product-item
    
      .. image:: _static/platform_tools/odc_stac/odc_stac_thumbnail.png
         :target: ./platform_tools/googledrive_access.html
         :align: left
            
      :doc:`platform_tools/googledrive_access`
      
      Connecting Google Drive Folder to DE Africa Sandbox
        
      :doc:`More <platform_tools/googledrive_access>`


.. toctree::
   :caption: About
   :hidden:
   :maxdepth: 1

   about/contact
   about/training
   about/glossary
   genindex

