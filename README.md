# sALR All-Sky Light Pollution Model

[![DOI](https://zenodo.org/badge/980192014.svg)](https://doi.org/10.5281/zenodo.15587614)
[![Static Badge](https://img.shields.io/badge/NPS%20DataStore-Code%3A%202313802-blue)](https://irma.nps.gov/DataStore/Reference/Profile/2313802)

A Python and ArcGIS Pro implementation of the simplified All-Sky Light Pollution Ratio (sALR) model described in [Dan Duriscoe et al. 2018](https://www.sciencedirect.com/science/article/pii/S0022407317308749), "A simplified model of all-sky artificial sky glow derived from VIIRS Day/Night band data". This code is used by National Park Service [Natural Sounds and Night Skies Division (NSNSD)](https://www.nps.gov/orgs/1050/index.htm) staff to generate regional light pollution maps for parks.

Input data for the model comes from the Colorado School of Mines [Earth Observation Group](https://eogdata.mines.edu/products/vnl/), who produce annual composites of VIIRS Day-Night Band satellite imagery of nighttime lights.

Details on how to run the sALR model pipeline can be found in the [sALR_Pipeline_docs.pdf](docs/sALR_pipeline_docs.pdf)


## Continental U.S. sALR Light Pollution Map (2020)
<img src="static/sALR_2020_Layout.png?raw=true" alt="2020 sALR Model" width="90%"/>