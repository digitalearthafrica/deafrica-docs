.. _data_specs:

##############
Data Catalogue
##############

Digital Earth Africa hosts a repository of Earth observation datasets
spanning continental Africa.

******************************
DE Africa Continental Services
******************************


*Digital Earth Africa Continental services are continental-scale outputs that are produced by Digital Earth Africa from various combinations of the external datasets using specified modelling and calculation techniques, with validation also undertaken. Continental Services are provided with specified levels of update and latency and may be continuously updated as external datasets become available.*

---------------------------


Agriculture
^^^^^^^^^^^

.. toctree::
   :caption: Agriculture
   :hidden:
   :maxdepth: 1

    Cropland_extent_specs

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/crop_thumbnail.png

       :doc:`Cropland_extent_specs`

       Estimated location of croplands.

       :doc:`More <Cropland_extent_specs>`

Coastal
^^^^^^^

.. toctree::
   :caption: Coastal
   :hidden:
   :maxdepth: 1

   Coastlines_specs

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/Coastlines_thumbnail.png

       :doc:`Coastlines_specs`

       Annual shorelines and rates of coastal change along the entire African coastline at a 30 m resolution from 2000 to present. 

       :doc:`More <Coastlines_specs>`



Geomedians
^^^^^^^^^^

.. toctree::
   :caption: Satellite images
   :hidden:
   :maxdepth: 1

    GeoMAD_specs

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/GeoMAD_thumbnail.png

       :doc:`GeoMAD_specs`

       Cloud-free mosaics from Landsat and Sentinel-2 satellites.

       :doc:`More <GeoMAD_specs>`


Surface water
^^^^^^^^^^^^^

.. toctree::
   :caption: Surface water
   :hidden:
   :maxdepth: 1

   Landsat_WOfS_specs
   Waterbodies_specs

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/wofs_thumbnail.png

       :doc:`Landsat_WOfS_specs`

       Individual, annual and historic water observations.

       :doc:`More <Landsat_WOfS_specs>`

    .. container:: product-item

       .. image:: ../_static/data_specs/Waterbodies_thumbnail.png

       :doc:`Waterbodies_specs`

       A continental collection of African water bodies locations and surface area change at a 30m resolution from 1987 to present. 

       :doc:`More <Waterbodies_specs>`



Vegetation
^^^^^^^^^^

.. toctree::
   :caption: Vegetation
   :hidden:
   :maxdepth: 1

   
   Fractional_Cover_specs
   NDVI_Anomaly_specs
   NDVI_Climatology_specs

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/fc_thumbnail.png

       :doc:`Fractional_Cover_specs`

       Green vegetation, non-green vegetation and bare soil for every Landsat image.

       :doc:`More <Fractional_Cover_specs>`

    .. container:: product-item
    
       .. image:: ../_static/data_specs/NDVI_anom_thumbnail.png
    
       :doc:`NDVI_Anomaly_specs`
    
       Monthly mapping of vegetation condition against the long-term baseline.
    
       :doc:`More <NDVI_Anomaly_specs>`


    .. container:: product-item

       .. image:: ../_static/data_specs/NDVI_clim_thumbnail.png

       :doc:`NDVI_Climatology_specs`

       Long-term average vegetation condition (NDVI) for every Landsat pixel over the African continent.

       :doc:`More <NDVI_Climatology_specs>`



----------------
   
***************** 
External Datasets
*****************


*External Datasets are datasets that are made available to, and within Digital Earth Africa, but are not produced or maintained by Digital Earth Africa.*

----------------

Agriculture
^^^^^^^^^^^
.. toctree::
   :caption: Agriculture
   :hidden:
   :maxdepth: 1

    WaPOR_specs

.. container:: product-list

    .. container:: product-item

        .. image:: ../_static/data_specs/WaPOR_thumbnail.png

        :doc:`WaPOR_specs`

        The Water Productivity through Open access of Remotely sensed derived data (WaPOR) monitors and reports on agricultural water productivity through biophysical measures with a focus on Africa and the Near East, produced by the FAO.

        :doc:`More <WaPOR_specs>`


Elevation and topography
^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
   :caption: Elevation and topography
   :hidden:
   :maxdepth: 1

   COP_DEM_specs
   SRTM_DEM_specs


.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/COP-DEM_thumbnail.png

       :doc:`COP_DEM_specs`

       Corpenicus Digital Elevation Model with limited worldwide coverage at 30 metres and global coverage at 90 metres spatial resolution.

       :doc:`More <COP_DEM_specs>`


    .. container:: product-item

       .. image:: ../_static/data_specs/SRTM_DEM_thumbnail.png

       :doc:`SRTM_DEM_specs`

       NASA version 3.0 Shuttle Radar Topography Mission (SRTM) global 1 arc second (~30 metre) DEM and Digital Earth Africa SRTM DEM Derivatives.

       :doc:`More <SRTM_DEM_specs>`


Land Cover
^^^^^^^^^^

.. toctree::
   :caption: Land Cover
   :hidden:
   :maxdepth: 1

    
    CCI_Landcover_specs
    CGLS_LULC_specs   
    ESA_WorldCover_specs
    IO_LULC_specs
    Africapolis_urban_specs
   
.. container:: product-list

    .. container:: product-item
    
           .. image:: ../_static/data_specs/CCI_Landcover_thumbnail.png
    
           :doc:`CCI_Landcover_specs`
    
           ESA Climate Change Initiative Land Cover at 300 m resolution.
    
           :doc:`More <CCI_Landcover_specs>`   

    .. container:: product-item
    
           .. image:: ../_static/data_specs/CGLS_thumbnail.png
    
           :doc:`CGLS_LULC_specs`
    
           Copernicus Global Land Service annual land cover layers at 100 m spatial resolution.
    
           :doc:`More <CGLS_LULC_specs>`

    .. container:: product-item
    
           .. image:: ../_static/data_specs/ESA_WorldCover_thumbnail.png
    
           :doc:`ESA_WorldCover_specs`
    
           ESA WorldCover global land cover map at 10 m resolution.
    
           :doc:`More <ESA_WorldCover_specs>`
           
        
    .. container:: product-item
    
           .. image:: ../_static/data_specs/IO_LULC_thumbnail.png
    
           :doc:`IO_LULC_specs`
    
           ESRI 10-meter resolution global land use land cover time series.
    
           :doc:`More <IO_LULC_specs>`

    .. container:: product-item

       .. image:: ../_static/data_specs/Africapolis_urban_specs/Africapolis_urban_specs.png

       :doc:`Africapolis_urban_specs`

       OECD Sahel and West Africa Club  created Africapolis to provide a much needed standardised geospatial database on urbanisation dynamics in Africa, with the aim of making urban data in Africa comparable across countries and across time.

       :doc:`More <Africapolis_urban_specs>`



           
Meteorology           
^^^^^^^^^^^

.. toctree::
   :caption: Meteorology     
   :hidden:
   :maxdepth: 1

    CHIRPS_specs
    ERA5_Climate_Data_specs
           

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/CHIRPS_thumbnail.png

       :doc:`CHIRPS_specs`

       Daily and monthly rainfall estimates from rain gauge and satellite observations.

       :doc:`More <CHIRPS_specs>`

    .. container:: product-item

       .. image:: ../_static/data_specs/ERA5_thumbnail.png

       :doc:`ERA5_Climate_Data_specs`

       ERA5 global climate reanalysis product by the Copernicus Climate Change Service (C3S) at the ECMWF.

       :doc:`More <ERA5_Climate_Data_specs>`


Satellite images
^^^^^^^^^^^^^^^^

.. toctree::
   :hidden:
   :maxdepth: 1

    Landsat_C2_SR_specs
    Landsat_C2_ST_specs
    Sentinel-1_specs
    Sentinel-2_Level-2A_specs
   
.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/Landsat_thumbnail.png

       :doc:`Landsat_C2_SR_specs`

       Daily satellite images from Landsat 5, 7, 8 and 9.

       :doc:`More <Landsat_C2_SR_specs>`

    .. container:: product-item

       .. image:: ../_static/data_specs/ST_thumbnail.png

       :doc:`Landsat_C2_ST_specs`

       Surface Temperature from Landsat 5, 7, 8 and 9.

       :doc:`More <Landsat_C2_ST_specs>`

    .. container:: product-item

       .. image:: ../_static/data_specs/S1_thumbnail.png

       :doc:`Sentinel-1_specs`

       Synthetic Aperture Radar from Sentinel-1.

       :doc:`More <Sentinel-1_specs>`


    .. container:: product-item

       .. image:: ../_static/data_specs/S2_thumbnail.png

       :doc:`Sentinel-2_Level-2A_specs`

       Daily satellite images from Sentinel-2.

       :doc:`More <Sentinel-2_Level-2A_specs>`


Satellite Image Mosaic
^^^^^^^^^^^^^^^^^

.. toctree::
   :hidden:
   :maxdepth: 1

    ALOS_PALSAR_annual_mosaic_specs
    Sentinel-1_Monthly_Mosaic_specs
    Planet_NICFI_specs
    
    

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/ALOS_thumbnail.png

       :doc:`ALOS_PALSAR_annual_mosaic_specs`

       Synthetic Aperture Radar annual mosaics from JAXA.

       :doc:`More <ALOS_PALSAR_annual_mosaic_specs>`

    .. container:: product-item

       .. image:: ../_static/data_specs/Sentinel-1_Monthly_Mosaic_thumbnail.png

       :doc:`Sentinel-1_Monthly_Mosaic_specs`
       
       Sentinel-1 Monthly Mosaics enables easy time series analysis, either alone or combined with other datasets. 

       :doc:`More <Sentinel-1_Monthly_Mosaic_specs>`

    .. container:: product-item

       .. image:: ../_static/data_specs/PLANET_thumbnail.jpg

       :doc:`Planet_NICFI_specs`
       
       Planet NICFI visual mosaics provide optimized, true-color imagery, making them ideal for visual display and interpretation. 

       :doc:`More <Planet_NICFI_specs>`



Urban
^^^^^
.. toctree::
   :caption: Vegetation
   :hidden:
   :maxdepth: 1


    World_Settlement_Footprint_specs

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/WSF_thumbnail.png

       :doc:`World_Settlement_Footprint_specs`

       The World Settlement Footprint WSF is a 10m-resolution binary mask outlining the extent of human settlements globally for the years 2015 and 2019 based on multiple datasets, and the World Settlement Footprint Evolution shows the annual growth of human settlements globally at 30m-resolution. 

       :doc:`More <World_Settlement_Footprint_specs>`

Vegetation
^^^^^^^^^^

.. toctree::
   :caption: Vegetation
   :hidden:
   :maxdepth: 1

    Global_Mangrove_Watch_specs

.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/Global_Mangrove_Watch_thumbnail.png

       :doc:`Global_Mangrove_Watch_specs`

       Global Mangrove Watch global baseline map of mangroves for 2010 and change maps for 1996, 2007, 2008, 2009, 2015 - 2020. 

       :doc:`More <Global_Mangrove_Watch_specs>`


Soil
^^^^

.. toctree::
   :caption: Soil
   :hidden:
   :maxdepth: 1

   iSDA_Soil_Data

.. container:: product-list
       
    .. container:: product-item

       .. image:: ../_static/data_specs/iSDA_Soil_Bedrock_Depth_thumbnail.png

       :doc:`iSDA_Soil_Data`

       iSDA soil variables at 30 m resolution.

       :doc:`More <iSDA_Soil_Data>`       
       

    .. container:: product-item

       .. image:: ../_static/data_specs/GRAFS_thumbnail.png

       :doc:`GRAFS_specs`

       Global Root-zone moisture Analysis & Forecasting System (GRAFS) by the ANU Centre for Water and Landscape Dynamics. 

       :doc:`More <GRAFS_specs>`
       
              
   
About the data
----------------

.. toctree::
   :caption: About the data
   :hidden:
   :maxdepth: 1

   Landsat_tiers


.. container:: product-list

    .. container:: product-item

       .. image:: ../_static/data_specs/tiers_thumbnail.png

       :doc:`Landsat_tiers`

       How Landsat Collection 2 data tiers are used in Digital Earth Africa.

       :doc:`More <Landsat_tiers>`

If you have any feedback for the DE Africa data and services, please contact us at 
helpdesk@digitalearthafrica.org.
