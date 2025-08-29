.. _p_tips_robustscripts:

#############################
 Writing robust bash scripts
#############################

Bash scripts are useful for automating tasks and for running batch jobs.
However, the default behavior of bash is to keep running when errors
happen, and that can result in undesirable behavior such as running
programs with the wrong settings, analyzing bad data, and worse. This
page is written on the premise that it is better to fail loudly than to
generate bad results or do bad things quietly.

However, because of the many, many `bash pitfalls`_, using a more robust
programming language when performing more complex tasks is recommended.

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

.. code-block:: console

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

.. code-block:: console

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

By default, bash (and hence Slurm) will continue to execute a script
even if a command fails. If this is not detected, then it can lead to
partially or wholly corrupt data:

.. code-block:: bash
   :linenos:

   #!/bin/bash
   # 1. Create some data
   echo "I wish to complain about this dog what I purchased not half an hour ago from this very boutique." > sketch.txt
   # 2. Process the data (badly)
   sed -i -e's# dog # parrot ' sketch.txt
   # 3. Etc.
   gzip sketch.txt

This produces the following output:

.. code-block:: console

   $ ls
   my-sketch.sh
   $ bash my-sketch.sh
   sed: -e expression #1, char 16: unterminated `s' command
   $ ls
   my-sketch.sh sketch.txt.gz
   $ zcat sketch.txt.gz
   I wish to complain about this dog what I purchased not half an hour ago from this very boutique.

In more complicated scripts and/or if slurm logs are not carefully
vetted, this can lead to completely unexpected results.

There are several ways to handle these kinds of errors. We call ``exit``
with the argument (exit code) 1 to indicate to Slurm that the command
failed.

.. code-block:: bash
   :linenos:

   # 1. Exit if command fails, but nothing else
   sed -i -e's# dog # parrot ' sketch.txt || exit 1
   # 2. Manually handle the failure
   if ! sed -i -e's# dog # parrot ' sketch.txt; then
       echo "We're closin' for lunch."
       exit 1
   fi
   # 3. Ignore failures, if the command is expected to fail sometimes.
   #    This should be used with care!
   sed -i -e's# dog # parrot ' sketch.txt || true

This, however, does not work well if you wish to pipe commands:

.. code-block:: bash
   :linenos:

   if ! sed -i -e's# dog # parrot ' sketch.txt | gzip > sketch.txt.gz; then
       echo "We're closin' for lunch."
       exit 1
   fi

Running this code does not print ``We're closin' for lunch.``, because
the ``gzip`` command succeeds even if ``sed`` fails.

To mitigate these problems, we can make use of the following options:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 3-8

   #!/bin/bash

   # Abort on unhandled failure in pipes
   set -o pipefail
   # Ensure that custom functions inherit these options
   set -o errtrace
   # Print debug message and terminate script on failures
   trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

   # 1. Create some data
   echo "I wish to complain about this dog what I purchased not half an hour ago from this very boutique." > sketch.txt
   # 2. Process the data (badly)
   sed -i -e's# dog # parrot ' sketch.txt
   # 3. Etc.
   gzip sketch.txt

Running this script produces the following, helpful output:

.. code-block:: console

   $ ls
   my-sketch.sh
   $ bash my-sketch.sh
   sed: -e expression #1, char 16: unterminated `s' command
   sketch.sh: Error on line 13: sed -i -e's# dog # parrot ' sketch.txt
   $ ls
   my-sketch.sh sketch.txt

Prevent bash from updating running scripts
==========================================

A surprising fact about bash is that changes to a script can affect
already running instances of that script:

.. code-block:: bash

   $ cat example.sh
   sleep 5
   $ bash example.sh &
   $ echo 'echo "Hello, world!"' >> example.sh
   $ wait
   Hello, world!

This happens since bash reads the script line-by-line, and will
therefore pick up changes after the current line, if the script is
changed in place.

To force bash to load the entire thing up front, one can wrap the body
of the script in curly brackets. This prevents changes to existing
lines. To furthermore prevent newly added lines from being run, one can
add an explicit `exit` statement at the end of the script:

.. code-block:: bash

   #!/bin/bash
   {
       # Commands go here!
       exit $?
   }

Putting it all together
=======================

The following bash script template combines the suggestions above and
thereby helps avoid *some* pitfalls of using bash

.. code-block:: bash
   :linenos:

   #!/bin/bash
   # NOTE: SBATCH commands go here!
   {
   set -o nounset  # Exit on unset variables
   set -o pipefail # Exit on unhandled failure in pipes
   set -o errtrace # Have functions inherit ERR traps
   # Print debug message and terminate script on non-zero return codes
   trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

   # NOTE: Your commands go here!

   exit $? # Prevent the script from continuing if the file has changed
   }

A slightly more compact version is

.. code-block:: bash
   :linenos:

   #!/bin/bash
   # NOTE: SBATCH commands go here!
   {
   set -Euo pipefail # Exit on unset variables and failures
   trap 's=$?; echo >&2 "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

   # NOTE: Your commands go here!

   exit $? # Prevent the script from continuing if the file has changed
   }

Note however that is not guaranteed to catch all errors (see the `bash
pitfalls`_ page for more information). Using a more robust programming
language, or proper a pipeline, is therefore recommended for more
complicated tasks.

**********************************
 Using `trap` to clean up on exit
**********************************

The `trap` command offers an easy way to automatically clean up when a
script exits. For example, if we created a temporary file, that we wish
to delete when the script is done running:

.. code-block:: bash

   #!/bin/bash
   my_temp_file="$(mktemp)"
   trap "rm -v '${my_temp_file}'" EXIT

   echo "Do something with '${my_temp_file}' here!"

Running the script looks like this:

.. code-block:: console

   $ bash example.sh
   Do something with '/tmp/tmp.BaH9GKP50J' here!
   removed '/tmp/tmp.BaH9GKP50J'

A major advantage is that the `trap` command is always executed, even if
the script terminates early due to an error. The `trap` command will
also be run if the script is killed by a signal, for example via the
`kill` command, except if the signal `SIGTERM` is used.

*******************************************
 Checking your scripts for common mistakes
*******************************************

In addition to implementing the suggestions listed on this page, it is
recommended that you use the ShellCheck_ to check your bash scripts for
common mistakes.

For example, if we run shell check on the very first script shown on
this page:

.. code-block:: console

   $ module load shellcheck
   $ shellcheck myscript.sh

   In myscript.sh line 2:
   MY_VARIABLE="record"
   ^---------^ SC2034 (warning): MY_VARIABLE appears unused. Verify use (or export if used externally).

   In myscript.sh line 3:
   echo "I will not buy this ${MY_VARIABL}, it is scratched."
                           ^-----------^ SC2153 (info): Possible misspelling: MY_VARIABL may not be assigned. Did you mean MY_VARIABLE?

*******************************
 Running commands in Snakemake
*******************************

If you are using Snakemake to run your bash commands, then you are
already running commands in a `"strict" bash mode`_, namely with ``set
-euo pipefail``. This sets the ``nounset`` and ``pipefail`` options
mentioned above, as well as the ``errexit`` option that is equivalent to
the ``trap`` command above but which prints less information about the
failure:

.. code-block:: console

   $ snakemake
   sed: -e expression #1, char 16: unterminated `s' command
   [Thu Aug 29 11:26:32 2024]
   Error in rule 1:
       jobid: 0
       input: my-input.txt
       output: my-output.txt
       shell:
           sed -i -e's# dog # parrot ' my-input.txt > my-output.txt
           (one of the commands exited with non-zero exit code; note that snakemake uses bash strict mode!)

Note, however, that this does not apply to bash scripts that you execute
in your snakemake pipeline!

Snakemake also includes support for automatically quoting filenames by
using the ``:q`` modifier to variables: Instead of ``cat {input} | gzip
> {output}`` simply write ``cat {input:q} | gzip > {output:q}``. This is
the equivalent of ``cat "{input}" | gzip > "{output}"`` but also handles
cases like multiple filenames.

.. _"strict" bash mode: https://snakemake.readthedocs.io/en/stable/project_info/faq.html#my-shell-command-fails-with-exit-code-0-from-within-a-pipe-what-s-wrong

.. _bash pitfalls: https://mywiki.wooledge.org/BashPitfalls

.. _shellcheck: https://github.com/koalaman/shellcheck
