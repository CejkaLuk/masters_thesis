import numpy as np
from scipy import stats # For getting the mode of an array
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import re
import os

# Use LaTeX font for matplotlib
plt.rcParams['text.latex.preamble']=r"\usepackage{lmodern}"
params = {'text.usetex' : True, 'font.size' : 13, 'font.family' : 'lmodern'}
plt.rcParams.update(params) 

def get_matrix_metrics(log_file: str, matrix_name: str):
   """Returns iterations per sections and number of pivots per diagonal section."""
   with open(log_file, "r") as file:
      lines = file.readlines()

   matrix_str = ""
   start_line = None
   end_line = None
   pivots_per_section_str = ""

   for i, line in enumerate(lines):
      if "-> Running benchmark for:" in line and matrix_name in line:
         start_line = i
         break

   if start_line is not None:
      for i, line in enumerate(lines[start_line:]):
         if re.match(r"Row: \d+ ->\s+", line):
            matrix_str += line.strip() + "\n"
         elif "Pivots per section" in line:
            pivots_per_section_str = line.strip()
         elif "Total pivots" in line:
            end_line = i
            break
   else:
      print(f"Line containing '-> Running benchmark for:' and '{matrix_name}' not found!. Exiting...")
      exit(1)

   if end_line is not None:
      matrix_str = "\n".join(matrix_str.split("\n")[:end_line])
   else:
      print(f"Line containing 'Total pivots' not found. I'm missing a point to stop scanning the lines at. Exiting...")
      exit(1)

   return (TNL_matrix_print_to_np_matrix(matrix_str), TNL_vector_print_to_np_array(pivots_per_section_str))


def TNL_matrix_print_to_np_matrix(tnl_matrix_printed: str) -> np.array:
   """Parses matrix printed by TNL to NumPy matrix."""
   # Extract the values from the string and convert to a NumPy array
   rows = tnl_matrix_printed.strip().split("\n")
   matrix = []
   for row in rows:
       values = row.split()[3:]
       row_values = [int(value.split(":")[1]) for value in values]
       matrix.append(row_values)

   return np.array(matrix)

def TNL_vector_print_to_np_array(tnl_vector_printed: str) -> np.array:
   """Parses vector printed by TNL to NumPy matrix."""
   # Use regular expression to find numeric values
   numbers = re.findall(r'\d+', tnl_vector_printed)

   # Convert the numbers list into a NumPy array
   return np.array(numbers, dtype=int)

def iterations_pivots_plot(matrix: np.array, pivots_per_section: np.array, output_dir: str, matrix_name: str, save_fig: bool):
   """Plot iterative and pivoting metrics."""
   fig, ax = plt.subplots()   

   # Plot the matrix
   cax = ax.matshow(matrix, cmap='viridis')

   # Set the x and y ticks 
   ax.set_xticks(np.arange(matrix.shape[1]+1)-0.5, minor=True)
   ax.set_yticks(np.arange(matrix.shape[0]+1)-0.5, minor=True)
   ax.grid(which='minor', color='white', linestyle='-', linewidth=1.5)
   ax.tick_params(which='both', bottom=False, left=True)

   # X-axis label on the top axis
   ax.xaxis.set_label_position('top')

   # Set axes' labels
   ax.set_ylabel('Section row ID')
   ax.set_xlabel('Section column ID')

   # Create a colorbar
   cbar = fig.colorbar(cax)
   # Divide the color bar interval into 6 equally spaced subintervals
   ticks = np.linspace(cax.get_clim()[0], cax.get_clim()[1], num=6)
   # Round the subinterval edges to their nearest integers
   rounded_ticks = np.round(ticks).astype(int)
   cbar.set_ticks(rounded_ticks)
   cbar.set_label('Iterations in section')

   # Determine positions of bottom x-axis ticks
   bottom_xticks_pos = np.linspace(0, len(pivots_per_section) - 1, len(pivots_per_section))
   # Set 2nd x-axis to be at the bottom of the plot
   ax2 = ax.secondary_xaxis('bottom')
   
   # Set the ticks
   ax2.set_xticks(bottom_xticks_pos)
   # If there are more than 8 sections and the mode of the number of pivots per each section is greater than 3 digits
   # the numbers would overlap on the bottom x-axis -> rotate
   if len(pivots_per_section) > 8 and stats.mode(pivots_per_section, keepdims=False)[0] > 999:
      ax2.set_xticklabels(pivots_per_section.astype(int), rotation=45, ha='right')
   else:
      ax2.set_xticklabels(pivots_per_section.astype(int))
   ax2.set_xlabel('Pivots in diagonal section')

   plt.tight_layout()

   if save_fig:
      # Save the plot as a PDF file
      output_file = f"{output_dir}/{matrix_name}_icm32pp_metrics.pdf"
      plt.savefig(output_file, format='pdf', bbox_inches='tight', pad_inches = 0)
   else:
      plt.show()

   plt.clf()

def main():
   # File to take from
   PRECISION = "double"
   # Matrix for which to extract iterative and pivoting metrics
   MATRIX_NAME = "msc10848"
   # Save the plot
   SAVE_PLOT = True

   # This script assumes that it is run from the directory masters_thesis/resources/scripts
   REPO_ROOT = "../.."

   # Input directories
   metrics_dir = f"{REPO_ROOT}/resources/ch03/decomposition-benchmarks/decomposers/ICM32PP_metrics"
   log_filepath = f"{metrics_dir}/benchmark_log_decomposers_276cd27_icm32pp_metrics_{PRECISION}_precision.txt"

   # Output directory - for the plot
   output_dir = f"{REPO_ROOT}/images/ch03/input-matrices"

   if not os.path.exists(log_filepath):
      print(f"File {log_filepath} not found! Exiting...")
      exit(1)
   if not os.path.exists(output_dir):
      print(f"Directory {output_dir} not found! Exiting...")
      exit(1)

   matrix, pivots_per_section = get_matrix_metrics(log_filepath, MATRIX_NAME)

   iterations_pivots_plot(matrix, pivots_per_section, output_dir, MATRIX_NAME, SAVE_PLOT)

if __name__ == "__main__":
   main()