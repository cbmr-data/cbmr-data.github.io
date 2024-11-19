sacct: error: Problem talking to the database: Connection refused
=================================================================

If you are running Snakemake with the ``--slurm`` option on a compete
node, i.e. not the head node, then you will receive errors such as the
following:

.. code:: console

    Job 0 has been submitted with SLURM jobid 512921 (log: .snakemake/slurm_logs/rule_foo/512921.log).
    The job status query failed with command: sacct -X --parsable2 --noheader --format=JobIdRaw,State --name 2d898259-73e4-435d-aa77-44dc44d84c1b
    Error message: sacct: error: slurm_persist_conn_open_without_init: failed to open persistent connection to host:localhost:6819: Connection refused
    sacct: error: Sending PersistInit msg: Connection refused
    sacct: error: Problem talking to the database: Connection refused

To solve this, simply start your Snakemake pipeline on the head node
when using the ``--slurm`` option.
