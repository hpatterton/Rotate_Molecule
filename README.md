# Rotate_Molecule
A minute Python program that reads PDB files and show a line rendering of a molecule, allowing rotation on the X, Y and Z axes, and zoom.

This simple program is not a serious molecular viewer.  It is intended to teach and demystify computer manipulation of molecules, in conjunction with reviewing elementary geometry and matrix algebra.
Rotate_molecule is a simple Python program that imports an elementary PDB class, allowing PDB files to be read, and specifically HETATM and CONECT data to be retrieved.  Note that the HETATM record descriptors are used to identify the X, Y and Z coordinates of atoms in SDF files (see PubChem).  Protein or nucleic acid PDB files typically identify polymer atoms with ATOM and not HETATM.  The PDB class can easily be adjusted to read the ATOM records, but the code currently reads HETATM records.  It is intended for viewing small ligands downloaded from PubChem in SDF format. The PDF file format is given at https://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html.  The SDF file format is given at https://pubs.acs.org/doi/pdf/10.1021/ci00007a012.
The path to the ligand SDF file is hardcoded in the code.  Edit as required.
The molecule is centred on its geometric centre.
The molecule can be rotated on the X axis (arrow up and down), Y axis (arrow left and right) or Z axis (Z and X keys). The image can also be zoomed (less than and greater than keys).

rotate_molecule.py is the main code, and imports the PDB class from the class_PDB.py file.  You need to have pygame and numpy modules installed.
