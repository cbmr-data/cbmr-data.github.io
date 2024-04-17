#%Module

# Automatically determined name and version
set name [file dirname [module-info name]]
set version [file tail [module-info name]]

set description "Toolkit for processing sequences in FASTA/Q formats"
set root /projects/my-project/apps/modules/software/${name}/${version}

prepend-path PATH ${root}/bin

# Prevent loading multiple versions of the same software
conflict "${name}"

module-whatis "${name} [file tail [module-info name]] - ${description}"

proc ModulesHelp { } {
   global name version
   puts stderr "\tLoads the ${name} version ${version} environment"
   puts stderr "\n\tFor further information, use 'module display [module-info name]'"
}

proc ModulesDisplay { } {
   global description
   puts stderr "\n${description}"
}
