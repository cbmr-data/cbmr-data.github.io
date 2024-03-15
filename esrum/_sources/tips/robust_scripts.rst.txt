.. _p_tips_robustscripts:

#############################
 Writing robust bash scripts
#############################

Bash scripts are useful for automating tasks and for running batch jobs.
However the default behavior of bash is to keep running when errors
happen, and that can result in undesirable behavior such as running
programs with the wrong settings, analyzing bad data, and worse. This
page is written on the premise that it is better to fail loudly than to
generate bad results or do bad things quietly.

However, because of the many, many `bash pitfalls`_, it is also
recommended to use a more robust programming language when performing
more complex tasks.

*********************************
 Improving default bash behavior
*********************************

This section describes several options that can make bash scripts behave
in a more reasonable manner.

.. warning::

   While it is possible to set these options in your shell, this is
   *not* recommended since it will break scripts not designed with these
   options in mind and can result in your terminal closing every time
   you make a typo. For the same reason you *must not* set these options
   in scripts that you import into your shell using the ``source`` or
   ``.`` command.

Prevent use of undefined variables
==================================

Variables are used for a variety of purposes in bash, including to
access slurm options in batch scripts. However, unlike in most
programming languages, it is not an error to access a variable that does
not exist:

.. code:: shell

   $ cat myscript.sh
   #!/bin/bash
   MY_VARIABLE="record"
   echo "Tourist: I will not buy this ${MY_VARIABL}, it is scratched."
   echo "Clerk: Sorry?"
   $ bash myscript.sh
   Tourist: I will not buy this , it is scratched.
   Clerk: Sorry?

Note how the script keeps executing even though we made a mistake. A
common mistake is therefore to misspell variables in scripts and have
bash silent do the wrong thing.

While there are cases where it is useful to allow missing variables,
most of the time this is a mistake. To prevent this, you can set the
``nounset`` option, which causes bash to terminate on unset variables:

.. code:: shell

   $ cat myscript.sh
   #!/bin/bash
   set -o nounset  # Exit on unset variables
   MY_VARIABLE="record"
   echo "Tourist: I will not buy this ${MY_VARIABL}, it is scratched."
   echo "Clerk: Sorry?"
   $ bash myscript.sh
   test.sh: line 4: MY_VARIABL: unbound variable

This not only tells us that there is a problem with our script (and
where!), but it also stops bash from doing any more damage.

.. note::

   Should you *want* to allow a variable to be unset while using
   ``nounset``, you can use the ``${name:-default}`` pattern, where
   ``name`` is the name of a variable and ``default`` is the text you
   want to use if ``name`` is not set. To match the default behavior of
   bash simply use ``${name:-}``.

Stop running on program failures
================================

..
   TODO

Prevent bash from updating running scripts
==========================================

..
   TODO

Putting it all together
=======================

The following bash script template combines the suggestions above and
thereby helps avoid *some* of the pitfalls of using bash

.. code:: bash

   #!/bin/bash
   # FIXME: SBATCH commands go here!

   {
   set -o nounset  # Exit on unset variables
   set -o pipefail # Exit on unhandled failure in pipes
   set -o errtrace # Have functions inherit ERR traps
   # Print debug message and terminate script on non-zero return codes
   trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

   # FIXME: Your commands go here!

   # Prevent the script from continuing if the file has changed
   exit $?
   }

Note however that is not guaranteed to catch all

*******************************************
 Checking your scripts for common mistakes
*******************************************

In addition to implementing the suggestions listed on this page, it is
recommended that you use the shellcheck_ to check your bash scripts for
common mistakes.

For example, if we run shell check on the very first script shown on
this page:

.. code:: shell

   $ module load shellcheck
   $ shellcheck myscript.sh

   In myscript.sh line 2:
   MY_VARIABLE="record"
   ^---------^ SC2034 (warning): MY_VARIABLE appears unused. Verify use (or export if used externally).

   In myscript.sh line 3:
   echo "I will not buy this ${MY_VARIABL}, it is scratched."
                           ^-----------^ SC2153 (info): Possible misspelling: MY_VARIABL may not be assigned. Did you mean MY_VARIABLE?

.. _bash pitfalls: https://mywiki.wooledge.org/BashPitfalls

.. _shellcheck: https://github.com/koalaman/shellcheck
