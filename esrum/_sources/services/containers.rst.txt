.. _p_containers:

########################
 Containerized software
########################

Containerization_ is a technique for running jobs in an isolated and
reproducible manner, by bundling all necessary dependencies up to and
including entire operating systems and running the software using
virtualization.

The Esrum cluster supports two different methods for running
containerized software:

#. Singularity_ (now renamed to ``AppTainer``) for running containerized
   applications using the SLURM queuing system. Instructions are
   provided below for converting existing Docker/Podman containers.

#. Podman_ for longer-running services on the specialized container
   node. Podman is Docker_ compatible, but is designed from the ground
   up for running in user-space and therefore offers better security
   guarantees.

************************
 Singularity containers
************************

Singularity is available via :ref:`p_usage_modules` and allows you to
run containerized software as part of Slurm jobs. If possible, you
should prefer to run your containerized tools in this manner.

The following only covers the absolute basics. For more information
please refer to the official `Singularity documentation`_.

Running Docker Hub images
=========================

Container images available on `Docker Hub`_ can be converted to
singularity images in one step using the ``singularity build`` command.
For the following example, we will download and run version ``0.7.17``
of the `pegi3s/bwa`_ image on `Docker Hub`_:

.. code-block::

   $ module load --auto singularity
   $ singularity build --disable-cache pegi3s_bwa_0.7.17.sif docker://pegi3s/bwa:0.7.17

This fetches the ``pegi3s/bwa`` image with the tag ``0.7.17`` and saves
it to the local file ``pegi3s_bwa_0.7.17.sif``. It is recommended that
you save such images in the ``/apps`` folders of the project you are
working on so that your collaborators can also access it.

The ``--disable-cache`` option is optional but recommended, since
Singularity will otherwise cache the individual parts of the image it
downloaded in ``~/.singularity``. As described in
:ref:`p_usage_filesystem` your home is limited to 100 GB and larger
docker images can easily take up gigabytes of space.

Once you have run the ``build`` command, the image can be run using the
``singularity run`` command:

.. code-block::

   $ singularity run pegi3s_bwa_0.7.17.sif bwa

   Program: bwa (alignment via Burrows-Wheeler transformation)
   Version: 0.7.17-r1188
   Contact: Heng Li <lh3@sanger.ac.uk>

It is also possible to run `Docker Hub`_ images "directly" by using a
``docker://`` URL instead of the path to a singularity image:

.. code-block::

   $ singularity run docker://pegi3s/bwa:0.7.17 bwa

However, this caches the image in your home folder, and it is therefore
not recommended for the reasons described above.

Running custom Docker/Podman images
===================================

Docker/Podman images run on another system must be exported and
converted before they can be run on Esrum. The ``podman save`` and the
corresponding ``docker save`` command may be used to export an image to
a single file:

.. code-block::

   $ podman save my-image:v1.2.3 --output ~/my_image_v1.2.3.tar

Once the image has been exported, you can transfer it to Esrum using
``scp`` or another suck method:

.. code-block::

   $ scp ~/my_image_v1.2.3.tar abc1232@esrumhead01fl.unicph.domain:/projects/my_project/scratch/

Finally, you can convert the image on Esrum to the format used by
singularity:

.. code-block::

   $ ssh abc123@esrumhead01fl.unicph.domain
   $ module load --auto singularity
   $ cd /projects/my_project/scratch/
   $ singularity build my_image _v1.2.3.sif docker-archive://my_image_v1.2.3.tar

The singularity image can then be run using the ``singularity run``
command:

.. code-block::

   $ singularity run my_image_v1.2.3.sif

*******************
 Podman containers
*******************

The ``esrumcont01fl`` node is dedicated to running containerized
software that is not suitable for conversion to/running via Singularity.
Please :ref:`p_contact` us if you wish to run containers on the
container node.

.. _containerization: https://www.ibm.com/topics/containerization

.. _docker: https://www.docker.com/

.. _docker hub: https://hub.docker.com/

.. _pegi3s/bwa: https://hub.docker.com/r/pegi3s/bwa

.. _podman: https://podman.io/

.. _singularity: https://apptainer.org/

.. _singularity documentation: https://docs.sylabs.io/guides/latest/user-guide/
