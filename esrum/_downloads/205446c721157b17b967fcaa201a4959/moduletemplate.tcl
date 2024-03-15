#%Module

# Automatically determined name and version
set name [file dirname [module-info name]]
set version [file tail [module-info name]]

# FIXME: Update this line with a description of the software
set description "description of software goes here"
# FIXME: Replace `my-project` with the actual project name
set root /projects/my-project/apps/modules/software/${name}/${version}

prepend-path PATH ${root}/bin
# FIXME: If you need to export additional environment variables, then
#        add them here using `append-path`, `prepend-path` or `setenv`:
#        https://modules.readthedocs.io/en/latest/modulefile.html#mfcmd-prepend-path
#        https://modules.readthedocs.io/en/latest/modulefile.html#mfcmd-setenv

# Prevent loading multiple versions of the same software
conflict "${name}"

proc ModulesHelp { } {
   global name version
   puts stderr "\tLoads the ${name} version ${version} environment"
   puts stderr "\n\tFor further information, use 'module display [module-info name]'"
}

proc ModulesDisplay { } {
   global description
   puts stderr "\n${description}"
}

module-whatis "${name} [file tail [module-info name]] - ${description}"
