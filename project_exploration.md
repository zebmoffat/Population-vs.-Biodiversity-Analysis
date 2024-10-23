#### SER494: Exploratory Data Munging and Visualization
#### An Analysis on the Relationship between Population and Biodiversity in New York State
#### Zeb Moffat
#### 10/22/2024

## Basic Questions
**Dataset Author(s):**
- New York State Department of Environmental Conservation (Biodiversity data)
- United States Census Bureau (Population data)

**Dataset Construction Date:**
- November 12, 2020 (Biodiversity data)
- July 1 2023 (Population data)

**Dataset Record Count:**
- 20507 (Biodiversity data)
- 63 (Population Data)

**Dataset Field Meanings:**  
Biodiversity data
- County (County in New York State), Category (Animal/Plant/Natural Community), Taxonomic Group (Classification of the measured category, e.g. Reptiles), Taxonomic Subgroup (Further classication of the Taxonomic Group e.g. Snakes), Scientific Name (Scientific name of the living organism/community), Common Name (Common name of the living organism/community), Year Last Documented (The most recent year the group was observed/recorded), NY Listing Status (The legal conservation status of the group under NY State regulations), Federal Listing Status (The conservation status of the group at the federal level of government), State Conservation Rank (Ranked risk of extinction within NY State), Global Conservation Rank (Ranked risk of extinction on the globe), Distribution Status (Status in the county, e.g. recently confirmed, unconfirmed) 

Population data
- Geographic Area (County, except it has the population for the whole state once), April 1, 2020 Estimates Base (Population for each county and New York State estimate from 04/01/2020), Population Estimate (as of July 1) 2020, 2021, 2022, 2023 (Four Fields, one for each year 2020-2023, as of July 1st that year)

**Dataset File Hash(es):**
- c837abd2642ce2c163f8ff59641f7cf1 (Biodiversity data)
- 6072df06952375ea3cc45fecc83e7258 (Population data)

**Dataset Sources**
- [Biodiversity dataset](https://catalog.data.gov/dataset/biodiversity-by-county-distribution-of-animals-plants-and-natural-communities)
- [Population dataset](https://www.census.gov/data/tables/time-series/demo/popest/2020s-counties-total.html) The population dataset is downloadable under "Annual Estimates of the Resident Population for Counties: April 1, 2020 to July 1, 2023 (CO-EST2023-POP)" and then by clicking the New York link.

## Interpretable Records
### Record 1 (Biodiversity dataset)
**Raw Data:** Albany,Animal,Reptiles,Snakes,Carphophis amoenus,Eastern Wormsnake,2009,Special Concern,not listed,S2,G5,Recently Confirmed

**Interpretation:** This row is from the biodiversity dataset. It contains information on the Eastern Wormsnake in the county Albany. This is a snake and it's classifications and names are accurate. This snake is also known to be somewhat endangered within New York but not globally, so it's rankings make sense. This row is reasonable for the meaning of the data.

### Record 2 (Population dataset)
**Raw Data:** Bronx County, New York; 1,472,653; 1,461,151; 1,424,084; 1,381,808; 1,356,476

**Interpretation:** This row is from the population dataset (I seperated the data with semicolons since it had commas already present). This row is reasonable for the meaning of the data. The Bronx is known to be a very populated county in New York. Even though there is some population decline over the years, it does make sense and the data seems sound.

## Background Domain Knowledge
Biodiversity, the variety of life on Earth, has sadly been declining. The loss of biodiversity can be attributed to several including but not limited to climate change, deforestation/urbanization, and invasive species. “Scientists estimate that current extinction rates exceed those of prehistoric mass extinctions. Loss of biodiversity also means loss of genetic diversity and loss of ecosystems” (NYSDEC “Biodiversity & Species Conservation”, paragraph 6).

This analysis attempts to explore how population is directly connected to the loss of biodiversity through population size. While not indicative of the whole globe, looking at the variety of ecosystems and the immense population throughout New York State could give a greater understanding of how human population affects biodiversity. “Biodiversity brings important environmental services to our parks and communities. The variety of plant and animal life that occur naturally in these areas help to clean and protect our environment” (NYS OPRHP “Biodiversity”, paragraph 2)

It is widely known that population growth has had a lasting change on our planet and its habitats. “The growing human population has dramatically altered Earth’s ecosystems, transforming forests, grasslands, and other wilderness areas into farms, pasture, timberland, mines, and settlements. People are now using around 71% of Earth’s habitable land and are indirectly affecting the rest of the globe through pollution and climate change” (Population Connection “Natural Resources” paragraph 6). This growing population clearly causes issues for our planet, but discouraging human reproduction isn’t something that everyone thinks should be done. Instead, we can emphasize sustainable practices, make responsible eco choices, and promote awareness on how we can treat our planet and its ecosystems better.

Understanding biodiversity and how it is affected by population, even in one state, brings us forward in our understanding of how to help our planet. By studying this complicated relationship, we can identify more steps of action for conservation and sustainability. A cleaner, healthier planet benefits every living thing.


### Sources
- [Biodiversity & Species Conservation](https://dec.ny.gov/nature/animals-fish-plants/biodiversity-species-conservation)
- [Biodiversity](https://parks.ny.gov/environment/biodiversity.aspx)
- [Natural Resources](https://populationconnection.org/why-population/natural-resources/)

## Dataset Generality
For my analysis I am using two datasets, a New York State population dataset and a biodiversity by New York county dataset. The New York State population data was collected and provided by the United States Census Bureau and the biodiversity dataset was collected and provided by the New York State Department of Environmental Conservation. Both of these sources are governmental and can be assumed to be factual. Since both datasets detail information specific to New York counties and they are factual, it can be reasonably assumed that they are representative of the real world. The biodiversity dataset has over 20,000 rows making it quite far-spreading in its representation of New York and its counties. The population dataset contains population estimates by the U.S. Census Bureau for each county. Therefore these datasets are trustworthy and indicative of the real world.

## Data Transformations
### Transformation 1
**Description:** Removed 3 "Unknown Counties" from biodiversity data

**Soundness Justification:** Since I am counting biodiversity based on each county, it doesn't make sense to include data from unknown counties, so those 3 rows were skipped.

### Transformation 2
**Description:** Removed Atlantic Ocean and Long Island Sound data

**Soundness Justification:** Since I am counting biodiversity based on each county, it doesn't make sense to include data from the Atlantic Ocean and Long Island Sound as they are not county specific.

### Transformation 3
**Description:** Removed Lake Ontario and Erie Open Waters data

**Soundness Justification:** Since I am counting biodiversity based on each county, it doesn't make sense to include data from Lake Ontario and Erie as they are not county specific.

### Transformation 4
**Description:** Removed range from year documentation

**Soundness Justification:** Some rows had ranges like 1990-1999 for year last documented. Which logically doesn't make sense since the most recent year would be the year last documented. Therefore I only used the most recent year, also making it more applicable to present day.

### Transformation 5
**Description:** Replaced "Not available" years with the integer 0

**Soundness Justification:** This allows me to make all data within the set integers. It is still easily seperable from the data if needed though.

## Visualizations
### Visual 1 (midpoint_year_vs_biodiversity.png)
**Analysis:** This scatterplot shows the midpoint documentation year vs how many biodiversity documentations each county has. This helps us understand when counties have been most busy documenting their biodiversity and how much they documented.

### Visual 2 (population_vs_biodiversity.png)
**Analysis:** This scatterplot shows how much biodiversity documentation has been done for each county. It also shows each county's population. This allows us to understand how much biodiversity is documented per with more or less populated county.

### Visual 3 (population_vs_midpoint_year.png)
**Analysis:** This scatterplot shows the midpoint year or around the busiest time of biodiversity documentation for each county. It also shows each county population. It allows us to understand when each county was busiest and how it correlates to their population.

### Visual 4 (taxonomic_groups_histogram.png)
**Analysis:** This histogram shows each taxonomic group that has been documented and how many times that group has been documented throughout the counties of New York. A taxonomic group is a related group like "plants".

### Visual 5 (taxonomic_subgroups_histogram.png)
**Analysis:** This histogram shows each taxonomic subgroup that has been documented and how many times that group has been documented throughout the counties of New York. A taxonomic subgroup is an even more specific related group like "flowering plants" or "sedges".
