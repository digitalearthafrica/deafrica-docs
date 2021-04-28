Sandbox User Frequently Asked Questions
----------------------------------------

Having issues with the Sandbox? Check out this FAQ before 
contacting our support team.

.. contents::
   :local:
   

Sandbox verification code email not received
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please check the spam and junk folders in your email inbox.

Kernel crash or restart
^^^^^^^^^^^^^^^^^^^^^^^^

The Digital Earth Africa Sandbox has a finite amount of processing power 
allocated to each user. This means if you attempt to load or calculate a 
lot of data, the kernel may crash. You will have to rerun your notebook 
to continue working. However, if the notebook is still demanding too many 
resources, it will crash again. You can prevent kernel crashes by:

   * Decreasing the area selected for data processing
   * Shortening the time extent
   * Shutting down kernels of notebooks you have finished using: open the 
   notebook and select **Kernel -> Shut Down Kernel**
   
These actions reduce the memory load of your computation on the Sandbox.

File Save Error: 502 Bad Gateway
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your disk may be full. Users are allocated a finite space for 
files. Delete large files to free up more disk space. You can back up
files to your local drive by right-clicking the file and selecting 
"Download". Note that large files may take a long time to download.

Pod failed to spawn
^^^^^^^^^^^^^^^^^^^^

Select "Retry".

Dask spill to disk errors
^^^^^^^^^^^^^^^^^^^^^^^^^^

Dask-enabled notebooks may throw errors such as "No space left on device". 
This is caused by Dask spilling data to disk when memory limits are reached.

Here we suggest trying the following options: 

   1. Edit the Dask config file to prevent spilling to disk.
   Open a Terminal from the Sandbox Launcher. Using ``vi`` or another text 
   editor of your choice, open ``dask/distributed.yaml`` by typing the following 
   code into the Terminal line and pressing the ``Enter`` key.
   
   ``vi ~/.config/dask/distributed.yaml``
   
   Use arrow keys to navigate the file and press ``i`` to start editing. 
   As instructed here https://docs.dask.org/en/latest/setup/hpc.html, change the
   following settings to match:
   
      .. code-block:: python
           distributed:
             worker:
               memory:
                 target: false  # don't spill to disk
                 spill: false  # don't spill to disk
                 pause: 0.80  # pause execution at 80% memory use
                 terminate: 0.95  # restart the worker at 95% use
                 
   Press ``Esc`` then ``:``, ``wq``, ``Enter``.
   
   