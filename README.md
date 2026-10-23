
<p align="center">
  <img src="https://github.com/SHEDOOMTC/Basic_Moco_2/blob/main/Assets/Moco_2_visuals.png" />
</p>


## **Course Overview**

**Basic Moco II** is the second in the **BASIC MOCO SERIES**. Continuing the lessons started in **[Basic Moco I](https://github.com/SHEDOOMTC/Basic_Moco_1)**, **Basic MoCo II** stives to bring the foundational concepts of forcefields and molecular dynamics simulations implemented in both AmberTools and Gromacs. These have been routine workflow from us here at **[RESLAR Labs](https://www.linkedin.com/company/reslar-labs)**.

Our goal remain the same: expose the learner to the basics and spur them to go ahead and learn more. A sound foundation in molecular modelling will set the stage for the upward climb. This course is suitable for undergraduate and early-career postgraduate students. As with every of of our courses, we hold that this course is far from being exhaustive; rather, it is an invitation to the endless world of science, computation, modelling and drug discovery.

A very special thanks to **[RESLAR Labs](https://www.linkedin.com/company/reslar-labs)**, **[Shadrach Eze](shadrachchinecheremeze@gmail.com)**, **[Munachiso Elekwa](https://github.com/Munaelekwa), [Stephen Nnemolisa](https://github.com/nnemolisastephen), **[Ignatius Satuku]( satukuignatious@gmail.com)**, [Dr. Wande M. Oluyemi](https://scholar.google.com/citations?user=puxjf8wAAAAJ&hl=en) and [Dr. Adewumi T. Adeniyi](https://scholar.google.com/citations?user=upkvyLEAAAAJ&hl=en)** for their oversights, contributions and review. 


## Table of Contents  
- [Course Requirements](#course-requirements)
- [Modules](#modules)  
  - [High Performance Computing (HPC) in Modern Biomolecular Simulations Module](#hpc-in-modern-biomolecular-simulations-module)  
  - [Advanced Python for Drug Disocvery Module](#advanced-python-for-drug-discovery-module)  
  - [Theory: Molecular Mechanics and Dynamics Module](#theory-molecular-mechanics-and-dynamics-module)
  - [Forcefields and Molecular Dynamics Engine Module](#forcefields-and-molecular-dynamics-engine-module) 
  - [AmberTools and Workflow Module](#ambertools-and-workflow-module)
  - [Gromacs Engine and Workflow Module](#gromacs-engine-and-workflow-module)  
  - [Analysis of Molecular Dynamics Simulation Run Module](#analysis-of-molecular-dynamics-simulation-run-module)
  - [Free Energy Computation Module](#free-energy-computation-module) 
- [Practicals](#practicals)
- [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs)
- [References](#references)
- [Contact Us](#contact-us)


## Course Requirements

This is a basic course intended for undergraduate and early-career postgraduate students. As such, the learner is expected to have **basic understanding in Biology and chemistry**. In addition, the details of the hardware, and software requirements including outcomes are available in the **[requirements file](link)**. The learner should also have taken the previous **[Basic MoCo I Course](https://github.com/SHEDOOMTC/Basic_Moco_1)**.

## Modules
The course is divided into **Eight (8) modules**. Each module has a **PDF document** and a **video recording** of the course, as a **YouTube link**.

There is no **capstone project** like in the first course **[Basic MoCo I Course](https://github.com/SHEDOOMTC/Basic_Moco_1)**. This time, the practicals are embedded in Jupyter notebook with solutions provided. The Practicals will follow the workflow in **[AmberTools](https://ambermd.org/AmberTools.php)** and **[Gromacs](https://www.gromacs.org/)** including the trajectory analysis.

## HPC in Modern Biomolecular Simulations Module
This continues the **[Basic Linux Module](https://github.com/SHEDOOMTC/Basic_Moco_1)** in the previous course. Understanding the CPU and GPU architecture and how to schedule jobs in the cluster is a powerful skill needed by computational chemists. Most Simulation engines derive efficiency by maximizing the ratio of jobs shared between the CPU and the GPU. Access the **[course video here]()**. The PDF copy of the module is **[here]()**.

## Advanced Python for Drug Disocvery Module
Training Machine Learning Models on supercomputers requires a good balance of python and bash scripting. Here we introduce **[tensorFlow]()**, **[Pytorch]()** and other architectures for Machine Learning and Deep Learning Architectures. Access the **[course video here]()**. The PDF copy of the module is **[here]()**.

## Theory: Molecular Mechanics and Dynamics Module
Molecular mechanics deals with static strucutures and biomolecules at the level of classical physics. Molecular dynamics introduces an element of motion or trajectory to model the movement of atoms over time. These two tools are indispensable in the sudy of many biomolecular process in the body. Access the **[course video here]()**. The PDF copy of the module is **[here]()**.

## Forcefields, and Molecular Dynamics Engine Module
To describe chemical structures in molecular mechanics and dynamics, we need mathematical functions that will accurately model the potential energy functions. These define how atoms interact within (bonded) and between (non-bonded) structures. Access the **[course video here]()**. The PDF copy of the module is **[here]()**

## AmberTools and Workflow Module
**[AmberTools](https://ambermd.org/AmberTools.php)** is a freely available suite of programs used for preparing, simulating, and analysing biomolecular systems. It forms part of the AMBER software package and supports molecular mechanics, molecular dynamics, and free-energy calculations. AmberTools includes utilities such as **tleap** for system preparation, **cpptraj** for trajectory analysis, and **MMPBSA.py** for binding free-energy estimation. Access the **[course video here]()**. The PDF copy of the module is **[here]()**

## Gromacs Engine and Workflow Module
**[GROMACS (GROningen MAchine for Chemical Simulations)](https://www.gromacs.org/)** is a high-performance, Open-source molecular dynamics simulation engine widely used for studying biomolecules such as proteins, nucleic acids, lipids, and small molecules. GROMACS is optimised for speed and efficiency on CPUs and GPUs, making it suitable for large-scale simulations. Access the **[course video here]()**. The PDF copy of the module is **[here]()**

## Analysis of Molecular Dynamics Simulation Run Module
The trajectory is usually an important output of a molecular dynamics run. Here, we will explore the use of **[CPPTRAJ]()** and **[GMX ](https://manual.gromacs.org/current/onlinehelp/gmx.html)** to analyze trajectories from both **[AmberTools](https://ambermd.org/AmberTools.php)** and **[GROMACS](https://www.gromacs.org/)** engine respectively. 

For the use of **[CPPTRAJ]()**, access the **[course video here]()** and the PDF copy **[here]()**.  

For the use of **[GMX ](https://manual.gromacs.org/current/onlinehelp/gmx.html)**, access the **[course video here]()** and the PDF copy **[here]()**.  

## Free Energy Computation Module
Free energy computation is a computational technique used to estimate the thermodynamic stability of molecular systems and the binding affinity between biomolecules, such as proteins and ligands. It quantifies the change in Gibbs free energy associated with molecular interactions or conformational changes. Common methods include **[MMG/PBSA (Molecular Mechanics Generalized Born/Poisson-Boltzmann Surface Area)](https://doi.org/10.1517/17460441.2015.1032936)**, **[Thermodynamic Integration (TI)]()**, **[Free Energy Perturbation (FEP)]()** and many other enhanced sampling techniques such as **[Umbrella Sampling]()**.

Here **[MMG/PBSA (Molecular Mechanics Generalized Born/Poisson-Boltzmann Surface Area)]()** implemented in **[AmberTools](https://ambermd.org/AmberTools.php)**, **[gmx_MMPBSA](https://github.com/Valdes-Tresanco-MS/gmx_MMPBSA)** and **[Umbrella Sampling]()** both implemented in **[GROMACS](https://www.gromacs.org/)** will be treated in the Practical sections [Practicals](#practicals).

## Practicals
There is no **capstone project** like in the first course **[Basic MoCo I Course](https://github.com/SHEDOOMTC/Basic_Moco_1)**. This time, the practicals are embedded in Jupyter notebook with solutions provided. The Practicals will follow the workflow in **[AmberTools](https://ambermd.org/AmberTools.php)** and **[Gromacs](https://www.gromacs.org/)** including the trajectory analysis for both.

# Usage

To run the Practicals:

**Clone the Repository**
```bash
git clone https://github.com/SHEDOOMTC/xxxxxxx
```
## For AmberTools
```bash
conda env create --name AmberTools --file environment.yml
conda activate AmberTools
```
**For MD Simulation run**
```bash
# Create a folder for each run
mkdir AmberTools_run && cd AmberTools_run
#Copy the contents of each to their respective folders
cp -r ../AmberTools_run_done/* .
#Launch the associated Jupyter Notebook
jupyter-notebook Practical_AmberTools.ipynb
#or run 
jupyter lab Practical_AmberTools.ipynb

```

**For Analysis of Trajectories**
```bash
# Create a folder for each run
mkdir AmberTools_analysis && cd AmberTools_analysis
#Copy the contents of each to their respective folders
cp -r ../AmberTools_analysis_done/* .
#Launch the associated Jupyter Notebook
jupyter-notebook Practical_AmberTools_Analysis.ipynb
#or run 
jupyter lab Practical_AmberTools_Analysis.ipynb
```

**For MMG/PBSA**
```bash
# Create a folder for each run
mkdir mmgbsa_run && cd mmgbsa_run
#Copy the contents of each to their respective folders
cp -r ../mmgbsa_run_done/* .
#Launch the associated Jupyter Notebook
jupyter-notebook Practical_AmberTools_mmgbsa.ipynb
#or run 
jupyter lab Practical_AmberTools_mmgbsa.ipynb
```

```bash
```
```bash
```

## Frequently Asked Questions (FAQs)
We have provided a list of questions you might encounter as you interact with this course and the right responses. See **[here]()**

## References
The list of references is very long and mostly provided at the end of the pdf copy of each module. The series of tutorials in **[AmberTools](https://ambermd.org/tutorials/)**, **[gromacs by Professor Lemkul](http://www.mdtutorials.com/gmx/)** and the **[Bioexcel team](https://tutorials.gromacs.org/)** are great reference tools in this regards.

If you use this tutorial, please cite as **Eze, S., Nnemolisa, S., Munachi, E., Ignatius, S., Oluyemi, W., & Adeniyi, A. (2026, yyyyy). SHEDOOMTC/yyyyy Zenodo.**

## Contact Us
For questions or issues, please contact us @ [Reslar Labs](reslarscience@gmail.com)  **&copy; 2026**, or [Dr. Oluyemi](oluyemiwm@abuad.edu.ng) or [Shadrach Eze](shadrachchinecheremeze@gmail.com).

Follow us on our **[LinkedIn](https://www.linkedin.com/company/reslar-labs)** page and **[Youtube](https://www.youtube.com/@RESLAR-science)** channel
