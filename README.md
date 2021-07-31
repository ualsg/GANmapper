<p align="center">
  <a href="https://ual.sg/">
    <img src="images/logo.jpg" alt="Logo">
  </a>
  <h3 align="center">GANmapper - Geospatial Content Generator</h3>
</p>

This is the official repo of GANmapper, a building footprint generator using Generative Adversarial Networks

## Running GANmapper 
Steps:
1. Install prequisites
2. Use xxx script to obtain CRHD masks for prediction and training pair
4. Predict for wanted city
3. Convert prediction masks to polygons
4. get result!
### Prerequisites

You could use `environment.yml` to create a conda environment for Roofpedia

  ```sh
  conda env create -f environment.yml
  ```

### Data Preparation
Save a geojson file of building polygons (can be done in QGIS)
Extract the satellite tiles in slippymap format (can be done in QGIS)
### Prediction
Predictions can be carried out by running the following sample code. The name of the city depends on the name of each dataset.

 ```sh
  python predict_and_extract.py --city Berlin --type Solar
  ```
### Training
By preparing your own labels, you can train your own model. Training options can be set under `config/train-config.toml`

 ```sh
  python train.py
  ```
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

<!-- ## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name) -->



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

Roofpedia is made possible by using the following packages

* [PyTorch](https://pytorch.org/)
* [GeoPandas](https://geopandas.org/)
* [Robosat](https://github.com/mapbox/robosat) - 
 mask to feature function is borrowed from robosat
* [pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) - 
Model Architecture is heavily borrowed from the awesome repo by [junyanz](https://github.com/junyanz)