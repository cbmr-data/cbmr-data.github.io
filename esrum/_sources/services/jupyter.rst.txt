.. _p_service_jupyter:

###################
 Jupyter Notebooks
###################

`Jupyter Notebooks`_ are available via the module system on Esrum and
can be run on regular compute nodes or on the GPU/high-memory node,
depending on the kind of analyses you wish to run and the size of your
workload.

By default, Jupyter only includes support for Python notebooks, but
instructions are included :ref:`below <s_jupyter_kernels>` for how to
add support for R.

.. note::

   We are currently working on making Jupyter available along with the
   :ref:`s_service_rstudio`. We will announce when this service is
   ready.

*****************************
 Starting a Jupyter notebook
*****************************

To start a notebook on a node, run the following commands:

.. code-block:: console

   $ module load jupyter-notebook
   $ srun --pty -- jupyter notebook --no-browser --ip=0.0.0.0 --port=XXXXX

The number used in the argument ``--port=XXXXX`` must be a value in the
range 49152 to 65535, and must not be a number used by another user on
Esrum. The number shown here was randomly selected for you, and you can
refresh this page for a different suggestion.

.. raw:: html

   <noscript>
   <div class="admonition warning"><p class="admonition-title">Warning</p><p>A random port could not be selected, because Javascript is disabled. Please choose a number in the range 49152 to 65535, and use this number whenever the documentation says <code class="docutils literal notranslate"><span class="pre">XXXXX</span></code></p></div>
   </noscript>

This will allocate a single CPU and ~16 GB of RAM to your notebook. If
you need additional resources for your notebook, then please see the
:ref:`reserving_resources` section for instructions on how to reserve
additional CPUs and RAM, and the :ref:`p_usage_slurm_gpu` page for
instructions on how to reserve GPUs or large amounts of memory. The
``srun`` accepts the same options as ``sbatch``.

.. tip::

   It is recommended that you execute the ``srun`` command in a ``tmux``
   or ``screen`` session, to avoid the notebook shutting down if you
   lose connection to the head node. See :ref:`p_tips_tmux` for more
   information.

************************************
 Connecting to the Jupyter Notebook
************************************

To connect to the notebook server, you will first need to set up a
connection from your PC to the compute node on which your notebook is
running. This is called "port forwarding" and is described on the
:ref:`p_tips_forwarding` page.

However, to do so you must first determine on which compute node your
job is running. This can be done in a couple of ways:

-  Look for the URLs printed by Jupyter when you started it on Esrum:

   .. code-block:: text
      :emphasize-lines: 4

      To access the notebook, open this file in a browser:
          file:///home/abc123/.local/share/jupyter/runtime/nbserver-2082873-open.html
        Or copy and paste one of these URLs:
            http://esrumcmpn07fl.unicph.domain:XXXXX/?token=0123456789abcdefghijklmnopqrstuvwxyz
         or http://127.0.0.1:XXXXX/?token=0123456789abcdefghijklmnopqrstuvwxyz

   In this example, our notebook is running on the ``esrumcmpn07fl``
   node. All Esrum node names end with ``.unicph.domain``, but we do not
   need to include this part of the name.

-  Alternatively, run the following command on the head node in a
   separate terminal:

   .. code-block:: console

      $ squeue --me --name jupyter
      JOBID  PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
      551600 standardq  jupyter   abc123  R       8:49      1 esrumcmpn07fl

   By looking in the ``NODELIST`` column, we can see that the notebook
   is running on ``esrumcmpn07fl``, as above.

Once you've determined what node your notebook is running on, go to the
:ref:`p_tips_forwarding` page and setup port forwarding to that node and
the port you used when starting Jupyter (e.g. ``XXXXX``), then you can
open the URL starting with ``http://127.0.0.1``, that Jupyter printed.
Typically, this can be done simply by holding Ctrl and left-clicking on
the URL.

.. _s_jupyter_kernels:

*******************************
 Adding an R kernel to Jupyter
*******************************

The Jupyter module only comes with a Python kernel. If you instead wish
to use R in your Jupyter notebook, you can add an R Kernel for the
specific version of R that you wish to use.

To do so, run the following commands, replacing `R/4.3.3` with the
version of R that you wish to use:

.. code-block:: console

   $ module load jupyter-notebook/6.5.4
   $ module load --auto R/4.3.3
   $ R
   > install.packages('IRkernel')
   > name <- paste("ir", gsub("\\.", "", getRversion()), sep="")
   > displayname <- paste("R", getRversion())
   > IRkernel::installspec(name=name, displayname=displayname)
   > quit(save="no")

This will make an R kernel with the name ``R 4.3.3`` available in
Jupyter. You can repeat these commands for each version of R that you
wish to make available as a kernel. Run the command ``module purge``
between each, to ensure that you have loaded only the expected version
of R and ``gcc`` that R depends on.

Once you are done adding R versions, you start notebook as shown above:

.. code-block:: console

   $ module load jupyter-notebook/6.5.4
   $ srun --pty -- jupyter notebook --no-browser --port=XXXXX

While you do not need to load the R module first, if you only wish to
run R code, you must do so if you wish to install R libraries via the
notebook:

.. code-block:: console

   $ module load jupyter-notebook/6.5.4
   $ module load --auto R/4.3.3
   $ srun --pty -- jupyter notebook --no-browser --port=XXXXX

*******************************************
 Running Slurm jobs from Jupyter notebooks
*******************************************

We provide a Python module (jupyter_slurm_) for submitting Slurm jobs
from Jupyter notebooks. This allows you to perform computationally
expensive analyses in a notebook, potentially across multiple nodes,
without having to reserve the resources required for this for the
duration of your notebook.

Installing ``jupyter_slurm``
============================

To use this module, you need to either install it together with Jupyter,
or you can "inject" it into your notebook. The former option is
recommended, and also allows you to install other libraries that you
need.

Option A: Installing the module with Jupyter
--------------------------------------------

#. Deactivate any currently active `conda` and python environments

   .. code-block:: console

      # to deactivate Conda environments:
      conda deactivate
      # to deactivate Python environments:
      deactivate

#. Load the python version you wish to use

   .. code-block:: console

      module load python/3.11.3

#. Create a virtual environment for `jupyter` / `jupyter_slurm`. The
   name `jupyter_slurm` may be replaced by any name that you prefer

   .. code-block:: console

      python3 -m venv jupyter_slurm

#. Install `jupyter` in the environment. You can install either the
   latest version or, if you prefer, a specific version of `jupyter`
   notebook:

   .. code-block:: console

      ./jupyter_slurm/bin/pip install notebook # the latest version, or
      ./jupyter_slurm/bin/pip install notebook==7.4.5 # a specific version

   Install any other python modules you need in the same manner.

#. Install `jupyter_slurm` in the environment

   .. code-block:: python

      # install the latest version of the module
      ./jupyter_slurm/bin/pip install /projects/cbmr_shared/apps/dap/jupyter_slurm/latest
      # or, alternatively, a specific version
      # ./jupyter_slurm/bin/pip install /projects/cbmr_shared/apps/dap/jupyter_slurm/0.0.1

To start the notebook, run, replacing ``XYZ`` with the port number you
are using (see above for more information)

.. code-block:: console

   shell srun --pty -- ./jupyter_slurm/bin/jupyter notebook --no-browser --ip=0.0.0.0 --port=XYZ

You can now import and use the ``jupyter_slurm`` module as described
below.

Option B: "Injecting" the module into your notebook
---------------------------------------------------

This method is not recommended, but allows you make use of
``jupyter_slurm`` if you are using the ``jupyter`` environment module on
Esrum, or another version of Jupyter where you cannot install your own
python modules.

Instead of installing the module, we add it to Python's ``sys.path``
list as shown below. This list defines where Python looks when importing
modules and this code therefore has to be run before attempting to
import the module:

.. code-block:: python

   import sys
   # to load the latest version
   sys.path.append("/projects/cbmr_shared/apps/dap/jupyter_slurm/latest/src")
   # or, alternatively, to load a specific version
   # sys.path.append("/projects/cbmr_shared/apps/dap/jupyter_slurm/0.0.1/src")

You can now import / use ``jupyter_slurm`` as described below.

Running Slurm jobs using ``jupyter_slurm``
==========================================

The ``jupyter_slurm`` provides wrapper functions for ``sbatch`` and for
``srun``. For example, to queue a job using ``sbatch``, use the function
with the same name:

.. code-block:: python

   import jupyter_slurm as jp

   jobid = jp.sbatch(
       [
           ["samtools", "markdup", "my data.sam", "--output", "my data.markdup.bam"],
           ["samtools", "index", "my data.markdup.bam"],
       ],
       modules=["samtools"],
   )
   print("Started job with ID", jobid)

This generates an ``sbatch`` script in which the ``samtools`` module is
loaded, and then runs the two ``samtools`` commands. The Job ID for this
job is returned the function. See below for how to pass shell commands
to the script.

.. note::

   You can see the script that the ``sbatch`` function generates by
   calling the ``sbatch_script`` function instead. The two functions
   take the same arguments, but ``sbatch_script`` returns a list of
   lines in the resulting script.

.. code-block:: python

   import jupyter_slurm as jp

   result = jp.srun(
       ["samtools", "idxstats", "my data.markdup.bam"],
       modules=["samtools"],
       capture=True,
   )
   print("Command ", ("failed" if result else "completed"), " with return code", result.returncode)
   print("  STDOUT =", result.stdout)
   print("  STDERR =", result.stderr)

Writing shell commands for the ``sbatch`` and ``srun`` functions
----------------------------------------------------------------

In the above examples, shell commands have been specified as lists of
strings:

.. code-block:: python

   [
       ["samtools", "markdup", "my data.sam", "--output", "my data.markdup.bam"],
       ["samtools", "index", "my data.markdup.bam"],
   ]

This has the advantage that ``jupyter_slurm`` can automatically escape
special characters such as spaces for you. This ensures that your
commands work regardless of what your filenames look like.

Alternatively, you can pass shell commands as strings, but in that case
you *must* manually quote/escape special characters:

.. code-block:: python

   [
       "samtools markdup 'my data.sam' --output 'my data.markdup.bam'",
       "samtools index 'my data.markdup.bam'",
   ]

This is equivalent to what gets generated automatically when passing
arguments as lists of strings.

Function reference
==================

``sbatch`` function
-------------------

.. code:: python

   def sbatch(commands: Sequence[str] | Sequence[Sequence[str]],
              *,
              cpus: int = 1,
              gpus: int = 0,
              gpu_type: Literal["a100", "h100", "A100", "H100"] | None = None,
              memory: int | str | None = None,
              job_name: str | None = None,
              modules: SequenceNotStr[str] = (),
              extra_args: SequenceNotStr[str] = (),
              output_file: str | Path | None = None,
              array_params: str | None = None,
              wait: bool = False,
              mail_user: str | bool = False,
              strict: bool = True) -> int

Submit an sbatch script for running one or more commands.

**Arguments**:

-  ``commands`` - One or more commands to be run using sbatch. May be a
   list of strings, in which case the strings are assumed to be properly
   formatted commands and included as is, or a list of list of strings,
   in which case each list of strings is assumed to represent a single
   command, and each argument is quoted/escaped to ensure that special
   characters are properly handled.

-  ``cpus`` - The number of CPUs to reserve. Must be a number in the
   range 1 to 128. Defaults to 1.

-  ``memory`` - The amount of memory to reserve. Must be a positive
   number (in MB) or a string ending with a unit (K, M, G, T). Defaults
   to ~16G per CPU.

-  ``gpus`` - The number of CPUs to reserve, either 0, 1, or 2. Jobs
   that reserve CPUs will be run on the GPU queue. Defaults to 0.

-  ``gpu_type`` - Preferred GPU type, if any, either ‘a100’ or ‘h100’.
   Defaults to None.

-  ``job_name`` - An optional string naming the current Slurm job.

-  ``modules`` - A list of zero or more environment modules to load
   before running the commands specified above. Defaults to ().

-  ``extra_args`` - A list of arguments passed directly to srun/sbatch.
   Multi-part arguments must therefore be split into multiple values:
   [“–foo”, “bar”] and not [“–foo bar”]

-  ``output_file`` - Optional name of log-file foom the job.

-  ``array_params`` - Optional job-array parameters (see “–array”).

-  ``mail_user`` - Send an email to user on failures or completion of
   the job. May either be an email address, or ``True`` to send an email
   to ``$USER@ku.dk``.

-  ``wait`` - If true, wait for the job to complete before returning.
   Defaults to False.

-  ``strict`` - If true, the script is configured to terminate on the
   first error. Defaults to true.

**Returns**:

-  ``int`` - The JobID of the submitted job.

``srun`` function
-----------------

.. code:: python

   def srun(
       command: Sequence[str],
       *,
       cpus: int = 1,
       gpus: int = 0,
       memory: int | str | None = None,
       modules: SequenceNotStr[str] = (),
       extra_args: SequenceNotStr[str] = (),
       capture: bool = False,
       text: bool = True,
       strict: bool = True
   ) -> SrunResult[None] | SrunResult[str] | SrunResult[bytes]

Run command via ``srun``, and optionally capture its output.

.. warning::

   This function can only be used from esrumhead01fl!

**Arguments**:

-  ``command`` - The command to run, either as a single string that is
   assumed to contain a properly formatted shell command, or as a list
   of strings, that is assumed to present each argument in the command.

-  ``cpus`` - The number of CPUs to reserve. Must be a number in the
   range 1 to 128. Defaults to 1.

-  ``memory`` - The amount of memory to reserve. Must be a positive
   number (in MB) or a string ending with a unit (K, M, G, T). Defaults
   to ~16G per CPU.

-  ``gpus`` - The number of CPUs to reserve, either 0, 1, or 2. Jobs
   that reserve CPUs will be run on the GPU queue. Defaults to 0.

-  ``gpu_type`` - Preferred GPU type, if any, either ‘a100’ or ‘h100’.
   Defaults to None.

-  ``extra_args`` - A list of arguments passed directly to srun/sbatch.
   Multi-part arguments must therefore be split into multiple values:
   [“–foo”, “bar”] and not [“–foo bar”]

-  ``modules`` - A list of zero or more environment modules to load
   before running the commands specified above. Defaults to ().

-  ``capture`` - If true, srun’s stdout and stderr is captured and
   returned. Defaults to False.

-  ``text`` - If true, output captured by ``capture`` is assumed to be
   UTF8 and decoded to strings. Otherwise bytes are returned. Defaults
   to True.

-  ``strict`` - If true, the script is configured to terminate on the
   first error. Defaults to true.

**Raises**:

-  ``SlurmError`` - Raised if this command is invoked on a compute node.

**Returns**:

-  ``int`` - The exit-code from running ``srun`` (non-zero on error)
   int, str, str: The srun exit-code, stdout, and stderr, if ``capture``
   is True. int, bytes, bytes: As above, but ``text`` is False.

*****************
 Troubleshooting
*****************

.. include:: jupyter_troubleshooting.rst
   :start-line: 8

.. _jupyter notebooks: https://jupyter.org/

.. _jupyter_slurm: https://github.com/cbmr-data/esrum-utils/tree/main/jupyter-slurm

.. _rstudio: https://posit.co/products/open-source/rstudio/

.. raw:: html

   <script defer>
    document.addEventListener('DOMContentLoaded', function() {
      replaceTextContent(document.body, "XXXXX", getEphemeralPort());
    });
   </script>
