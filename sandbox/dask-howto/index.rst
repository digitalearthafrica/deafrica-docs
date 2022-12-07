.. _dask-howto:

Understanding Dask  
==========================

This documentation builds upon DE Africa’s existing Parallel Processing with Dask notebook. Each of these isolated examples builds on from the previous, with the aim of introducing a new Dask related concept as each example progresses. 

Dask is a tool used for data management, whereby data is broken down into manageable chunks to allow for scaling up analyses and time efficiency. Breaking data into chunks can allow for easier storage in memory and can draw upon multiple computing cores to speed up computations. 

To find out more, click **Next**, or select `Lazy-loading Data <./01_lazy_loading_dask.ipynb>`_ below.


.. toctree::
   :maxdepth: 1

   01_lazy_loading_dask
   02_lazy_operations_dask
   03_dask_client