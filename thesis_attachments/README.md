# Attachments Relevant to the Master's Thesis: Parallel Computation of LU Decomposition on GPUs for the Numerical Solution of Partial Differential Equations

This directory contains all attachments relevant to the master's thesis titled *"Parallel Computation of LU Decomposition on GPUs for the Numerical Solution of Partial Differential Equations"* written by Lukáš Matthew Čejka as the culmination of their master's degree in *Applied Software Engineering* at the *Faculty of Nuclear Sciences and Physical Engineering* at the *Czech Technical University in Prague*.

## Directories
The attachments in this directory are:
- `benchmarks/` - results and scripts of the BDDCML benchmark and the Decomposition benchmarks.
- `repositories/` - repositories related to the BDDCML benchmark and the benchmarks implemented in the Decomposition project.
- `thesis_scripts/` - scripts used to generate plots and information about matrices that appear in the thesis.
- `masters_thesis_lmc.pdf` - PDF of the thesis.

**Note**: Some directories are compressed in the `.zip` format.

### Directory: `benchmarks/`
The benchmark results are divided into two directories:
- `results/` - raw and parsed benchmark results.
   - Further divided into directories of results of the benchmarks that were run as part of the thesis: `bddcml/`, `decomposers/`, `solvers/`.
- `slurm_batch_files/` - batch scripts used to execute benchmarks on the RCI cluster and bash scripts used to load Slurm modules.

### Directory: `repositories/`
The repositories are divided into two directories:
- `bddcml_benchmark/` - repositories related to the BDDCML benchmark
   - Further divided into:
      - `bddcml_decomposition/` - the bddcml repository that is set up to use decomposers and solvers from the Decomposition project.
      - `deps/` - dependencies of the bddcml repository (includes the `decomposition/` and `tnl/` repositories)
- `decomposition_benchmark/` - the `decomposition/` and the `tnl/` repositories.
   - **Note**: The directories containing the matrices for the benchmark, `decomposition/src/Benchmarks/<benchmark_type>/scripts/mtx-matrices/`, only contain one 4-by-4 test matrix.

**Note**: Each of the two directories serves as an independent instance of the benchmarks.

### Directory: `thesis_scripts/`
The scripts that were used to generate figures/data for the thesis:
- `mtx_nnz_pattern_plot.m` - Matlab script that plots the nonzero element pattern of a matrix stored in the `.mtx` file format.
   - The plot is saved as a `.pdf` file.
- `mtxs_condition_number.m` - Matlab script that computes the condition number of all matrices - stored in the `.mtx` file format - in a directory.
   - The `.mtx` files can be in nested directories.
   - The output is saved to a CSV file.
- `visualize-metrics.py` - Python script that plots the iterative and pivoting metrics of ICM_*x*PP on a given matrix.
   - The console output of the Decomposition benchmark is required.
   - The plot is saved as a `.pdf` file.