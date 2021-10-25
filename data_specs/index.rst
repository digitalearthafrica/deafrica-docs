.. _data_specs:

Dataset specifications
========================

Digital Earth Africa hosts a repository of Earth observation datasets
spanning continental Africa.

The input datasets, including CEOS Analysis Ready Data and
ancillary data, are used to derive output services and
can be accessed directly through the DE Africa Platform.

.. toctree::
   :caption: Input datasets
   :maxdepth: 1

   Landsat_C2_SR_specs
   Landsat_C2_ST_specs
   Sentinel-1_specs
   Sentinel-2_Level-2A_specs
   ALOS_PALSAR_annual_mosaic_specs
   
DE Africa also provide services which are information products
derived from input datasets. The services are co-developed with partners
and may be released at beta, provisional or operational maturity level.
An operational service is continuously updated as required input 
datasets become available. Services may be updated, based on user feedback, 
to incorporate new sensors, new algorithms and auxiliary data.

.. rubric:: Services
   :class: fakeheading

.. topic:: :doc:`GeoMAD_specs`
   :class: platform

   .. image:: ../_static/maps/Workbench.jpg
      :target: GeoMAD_specs
      :width: 160px
      :height: 112px
      :align: left

   Sentinel-2, Landsat GeoMAD services

   :doc:`More <GeoMAD_specs>`

.. topic:: :doc:`Landsat_WOfS_specs`
   :class: platform

   .. image:: ../_static/sandbox/sandbox_mini.png
      :target: Landsat_WOfS_specs
      :width: 160px
      :height: 120px
      :align: left

   Our JupyterLab Analysis Platform for exploring the data with access to analysis tools

   :doc:`Water Observations from Space <Landsat_WOfS_specs>`

.. toctree::
   :caption: Services
   :maxdepth: 1
   
   GeoMAD_specs
   Landsat_WOfS_specs
   Fractional_Cover_specs
   Cropland_extent_specs

If you have any feedback for the DE Africa data and services, please contact us at 
helpdesk@digitalearthafrica.org.
