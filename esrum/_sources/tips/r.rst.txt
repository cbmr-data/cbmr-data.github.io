.. _p_tips_r:

##################
 Using R on Esrum
##################

This section how to use R on Esrum and lays out various tips for making
your work easier. This section is primarily focused on running R
non-interactively via Slurm, in order to take full advantage of the
available compute resources.

For interactive work, we recommend using the :ref:`p_service_rstudio`
servers or using an :ref:`s_interactive_session`.

************************
 Selecting an R version
************************

Several versions of R are available via the module system. To load
these, you need to load the version of R you want *and* a version of
GCC_, which is required to install/load R libraries.

If you intend to also make use of the RStudio servers, then we recommend
that you ``R/4.3.3`` (or another version of ``R/4.3.x``) with
``gcc/8.5.0``. This ensures that the R libraries you install are
compatible between the compute nodes and the RStudio servers.

By default, the 4.3.x versions of R loads ``gcc/8.5.0``, so you can
simply use the ``--auto`` option when loading ``R/4.3.x``:

.. code-block::

   $ module load --auto R/4.3.3
   Loading R/4.3.3
     Loading requirement: gcc/8.5.0

R modules installed using versions of R other than ``4.3.x`` will not be
available on the RStudio server, and you will need to install them
again.

.. warning::

   Using a GCC version greater than 8.x with ``R/4.3.x`` may cause
   modules you install to fail to load on the RStudio server with the
   errors similar to the following:

   .. code-block::

      Error: package or namespace load failed for ‘wk’ in dyn.load(file, DLLpath = DLLpath, ...):
      unable to load shared object '/home/abc123/R/x86_64-pc-linux-gnu-library/4.3/wk/libs/wk.so':
      /lib64/libstdc++.so.6: version `GLIBCXX_3.4.26' not found (required by /home/abc123/R/x86_64-pc-linux-gnu-library/4.3/wk/libs/wk.so)

   See the Troubleshooting section below for more information.

**********************************
 Submitting R scripts using Slurm
**********************************

The recommended way to run R on Esrum is as non-interactive scripts
submitted to slurm. This not only ensures that your analyses do not
impact other users, but also makes your analyses reproducible.

To run an R script on the command-line, simply use the ``Rscript``
command:

.. code-block::

   $ cat my_script.R
   cat("Hello, world!\n")
   $ Rscript my_script.R
   Hello, world!

For simple scripts you can use the ``commandArgs`` function to pass
arguments to your scripts, allowing you to use them to process arbitrary
data-sets:

.. code-block:: R

   args <- commandArgs(trailingOnly = TRUE)

   cat("Hello, ", args[1], "!\n", sep="")

.. code-block::

   $ Rscript my_script.R world
   Hello, world!

If your script requires a heterogeneous set of input files or options to
run, then it is recommended to use an argument parser such as the
argparser_ R library. To use the ``argparser`` library you must first
install it using the ``install.packages("argparser")`` command.

The following shows a brief example of how you might use the
``argparser`` library. It can also be downloaded :download:`here
<scripts/argparser.R>`.

.. literalinclude:: scripts/argparser.R
   :language: R

This allows you to document your command-line options, specify default
values, and much more:

.. code-block::

   $ Rscript my_script.R
   usage: my_script.R [--] [--help] [--opts OPTS] [--p-value P-VALUE]
       input_file

   This is my script!

   positional arguments:
   input_file     My data

   flags:
   -h, --help     show this help message and exit

   optional arguments:
   -x, --opts     RDS file containing argument values
   -p, --p-value  Maximum P-value [default: 0.05]

   Error in parse_args(parser) :
   Missing required arguments: expecting 1 values but got 0 values: ().
   Execution halted
   $ Rscript my_script.R my_data.tsv
   I would process the file my_data.tsv with a max P-value of 0.05

Finally, you write can write a small bash script to automatically load
the required version of R and to call your script when you submit it to
Slurm (using your preferred version of R):

.. code-block:: bash

   #!/bin/bash

   module load gcc/8.5.0 R/4.1.2
   Rscript "${@}"

The ``"${@}"`` safely passes all your command-line arguments to
``Rscript``, even if they contain spaces. This wrapper script can then
be used to submit/call any of your R-scripts:

.. code-block::

   $ sbatch run_rscript.sh my_script.R my_data.tsv --p-value 0.01
   Submitted batch job 18090212
   $ cat slurm-18090212.out
   I would process the file my_data.tsv with a max P-value of 0.01

**********************
 Installing R modules
**********************

Modules may be installed in your home folder using the
``install.packages`` command:

.. code-block::

   $ module load gcc/8.5.0 R/4.3.1
   $ R
   > install.packages("ggplot2")
   Warning in install.packages("ggplot2") :
     'lib = "/opt/software/R/4.3.1/lib64/R/library"' is not writable
   Would you like to use a personal library instead? (yes/No/cancel) yes
   Would you like to create a personal library
   ‘/home/abc123/R/x86_64-pc-linux-gnu-library/4.3’
   to install packages into? (yes/No/cancel) yes

When asked to pick a mirror, either pick ``0-Cloud`` by entering ``1``
and pressing enter, or enter the number corresponding to a location near
you and press enter:

.. code-block::

   --- Please select a CRAN mirror for use in this session ---
   Secure CRAN mirrors

   1: 0-Cloud [https]
   [...]

   Selection: 1

.. _s_service_rstudio:

*****************
 Troubleshooting
*****************

.. include:: r_troubleshooting.rst

.. _argparser: https://cran.r-project.org/web/packages/argparser/index.html

.. _gcc: https://gcc.gnu.org/

.. _heads: https://heads.ku.dk/

.. _rstudio: https://posit.co/products/open-source/rstudio/
