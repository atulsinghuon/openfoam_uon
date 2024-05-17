Basic structure
===============

OpenFOAM, a collection of C++ header files and libraries, allows for many customization for a CFD analysis. The files, are usually strutured in three directories as 0, constant and system.

1. **0** folder includes the settings for the initial and boundary conditions for the flow that is analysed. 
2. The files in **constant** directory defines the material properties of the fluid used for the simulation. The mesh also gets stored in this directory by the sub-directory **polyMesh** here. 
3. The **system** folder includes codes to control various setttings of the simulation. 
    a. **system/blockMeshDict** controls the mesher **blockMesh**.
    b. **system/decomposeParDict** controls the mesh for a parallel run within the code. 
    c. **system/controlDict** controls the simulation paramters such as, solver, endTime, writeInterval etc. 
    d. **system/fvSolution** controls the iterative pressure-velocity coupling setting. 
    e. **system/fvSchemes** controls the numerical scheme within the solver. 

4. The solver runs in the following order. 

.. figure:: images/solveorder.png

This may of course vary depending on application and solver requirements, but the chain of editing the files would remain roughly in the order mentioned above. 
