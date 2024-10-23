__author__ = "Zeb Moffat"
__date__ = "10/22/2024"

import wf_dataprocessing
import wf_visualization
import time

if __name__ == '__main__':
    print("Biodiversity data and population data from 'data_original/' will now be read and processed.")
    time.sleep(0.5)
    wf_dataprocessing.run()
    time.sleep(0.5)
    print("Finished processing, cleaning, and writing data.\n")
    time.sleep(0.5)
    print("Summary statistics and pairwise correlations will now be calculated. "
          "Distributions of data will also be plotted.")
    wf_visualization.run()