# aster-calc-section

## Description
This collection of script enables the calculation of section properties with [aster](www.code-aster.org) code with the help of [salome meca](www.code-aster.org). Now, it works with I beam geometry.
- File Manager.py : the main python script reads input file and create communication temporary file. Then, geometry generation and mesh generation are called with salome meca. Finally, code aster is launched with the command MACR_CARA_POUTRE.
- GenPro.py : salome python script for the geometry and the mesh
- SectionAuto.comm : command file for code aster
- SectionAuto.export : setting for code aster calculation
- SectionAuto.input : I beam and H beam geometry
- SectionAuto.output : section properties results

## Use
- User need to adapt in every each scripts all file paths.
- User need to take care of python configuration in shell, salome and aster especially to launch pandas module within salome environment.

## Next steps
- Try to be less platform and user dependent ...
- Try to use this database in code aster calculation with beam elements.

## Philosophy
I would like to create some tools to facilitate the use of aster code with beam elements.
