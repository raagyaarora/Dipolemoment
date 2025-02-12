# Dipolemoment
Dipole moment from DFT Born effective charges
Step1: Calculate Born effective charges from DFT: Quantum espresso/VASP
Step2: Store them in a file
Example: 111   Atom1 (3x3 Borm effective charge tensor)
         222
         333
         Atom2
         Atom2
         Atom2
         So on ..............
Step3: Create a file corresponsding to displacements of atoms
Step4: Usepython script provided to perform matrix multiplications and get the total dipole moment

Useful for ferroelectrics, antiferrorelectric systems
