.. _p_ai_agents:

##########################
 Using AI Agents on Esrum
##########################

This page describes best practice for using AI agents on Esrum.

Briefly, it is strongly recommend that you use the provided
agent-container_ sandbox. This sandbox makes it easy to run any of the
supported agents on Esrum, with the agents only having access to
directories that you select.

In addition, the sandbox provides a persistent home folder outside of
your home on Esrum, in which you can store agent-specific config files,
as well as install tools you wish the agent to be able to access.

This helps prevent the exfiltration of sensitive data, as per our
:ref:`p_guidelines`.

.. tip::

    Please :ref:`contact us <p_contact>` if the agent you want to use is
    not available, and we will look at including it in the sandbox.

*****************
 Getting started
*****************

To start using a sandboxed AI Agent, simply load the module and run
``agent-container`` in the work folder containing your scripts or other
(non-sensitive) files:

.. code-block:: console

    $ cd /home/abc123/my-scripts/
    $ module load agent-container --auto
    $ agent-container claude

This will run Claude Code in a sandbox environment that only gives it
access to the ``/home/abc123/my-scripts/`` folder. No other folder on
Esrum can be accessed, including your normal home folder.

.. warning::

    It is important that the your work folder does not itself contain
    sensitive data. That is to say that ``/home/abc123/my-scripts/`` in
    the above example should only contain scripts and other
    non-sensitive files. It is, however, safe to include symlinks to
    data in your work folder, provided that the data itself is located
    elsewhere.

The container comes with built-in support for the following agents:

- ``agent-container claude``: Runs `Claude Code`_
- ``agent-container codex``: Runs `OpenAI Codex`_
- ``agent-container copilot``: Runs `GitHub Copilot`_
- ``agent-container gemini``: Runs `Google Gemini`_
- ``agent-container vibe``: Runs `Mistral Vibe`_

In addition, you can start a ``bash`` terminal in the sandbox via the
commands ``agent-container bash`` or ``agent-container shell``.

************************
 Command-line arguments
************************

All command-line arguments written after the agent name, ``shell``, or
``bash``, are passed directly to the process in the sandbox. For
example, to view the help text for ``claude``, simply run

.. code-block:: console

    $ agent-container claude --help

Arguments for ``agent-container`` itself must go before the agent name.
For example, to pass the ``--read-only`` option to ``agent-container``:

.. code-block:: console

    $ agent-container --read-only claude

*****************************************
 Mounting directories and read-only data
*****************************************

As described above, ``agent-container`` only has access to the current
work directory. Should you need to include additional folders in your
sandbox, then you can include them via the ``--include`` option. For
example, to include the directory ``/projects/cbmr_shared/apps`` in
addition to the current working directory,

.. code-block:: console

    $ cd /home/abc123/my-scripts/
    $ agent-container --include /projects/cbmr_shared/apps claude

This allows you to access both ``/home/abc123/my-scripts/`` and
``/projects/cbmr_shared/apps`` from inside the sandbox. You can specify
multiple ``--include`` options in this manner.

Additionally, you can make all your folders read-only. This includes
both the current working directory and any folders included via
``--include``. To do so, pass the ``--read-only`` option to
``agent-container``:

.. code-block:: console

    $ agent-container --read-only claude

.. _s_agents_installing_software:

********************************
 Installing additional software
********************************

If you need additional software in the sandbox, then you have two
options:

1. :ref:`Contact us <p_contact>` and ask to have the software added by
   default. This is appropriate for software that has wide usage.
2. For less commonly used software, you can install it in your sandbox
   home, for example using the included ``uv``, ``pixi``, or ``npm``
   command.

For example, to install the Conda package for R, using ``pixi``:

.. code-block:: console

    $ agent-container shell
    (agent-container) $ pixi global install r-base
    (agent-container) $ R --version
    R version 4.6.0 (2026-04-24) -- "Because it was There"

Or, to install ``ruff`` from PyPi using ``uv``:

.. code-block:: console

    $ agent-container shell
    (agent-container) $ uv tool install ruff
    (agent-container) $ ruff --version
    ruff 0.15.18

Any software installed in your sandbox home will persist between
invocations of the sandbox.

**************************
 Remote control of agents
**************************

In some cases, it is possible to remotely control the agent running in
the sandbox environment:

- ``claude``: Run ``agent-container claude --remote-control`` to start a
  session that you control via your browser or via the desktop app. See
  `here <claude-remote-control_>`_ for more information.
- ``codex``: Currently not feasible, due to Codex needing to connect via
  SSH when using remote control.
- ``copilot``: Run ``agent-container copilot --remote`` to start a
  session that you control via your browser. See `here
  <copilot-remote-control_>`_ for more information.
- ``gemini``: Not currently supported.
- ``vibe``: Not currently supported.

*************
 Limitations
*************

- For most part, it is not possible to take advantage of integration of
  agents and IDEs such as VS Code, as these need to be able to directly
  interact with the agents.
- The sandbox does not have access to any software on Esrum, including
  Slurm. Instead, see the :ref:`s_agents_installing_software` section
  above for how to add software to the sandbox.
- While in the sandbox, your home folder is set to
  ``/home/singularity``, even if you are started the sandbox in your
  (Esrum) home folder. This means that you must use the full path to
  reference files in your home folder, e.g. ``/home/abc123``.

.. _agent-container: https://github.com/cbmr-data/agent-container/

.. _claude code: https://claude.com/product/claude-code

.. _claude-remote-control: https://code.claude.com/docs/en/remote-control

.. _copilot-remote-control: https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/steer-remotely

.. _github copilot: https://github.com/copilot

.. _google gemini: https://gemini.google.com/

.. _mistral vibe: https://mistral.ai/products/vibe/

.. _openai codex: https://openai.com/codex/
