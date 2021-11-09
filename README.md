# The Impact of Diversity in the Emergence of Cooperation
Network Science 2021-2022

## Authors

**Group 17**

92436 [Catarina Alegria](mailto:catarina.alegria@tecnico.ulisboa.pt)

92444 [Daniela Amaral](mailto:daniela.amaral@tecnico.ulisboa.pt)

92567 [Vasco Rocha](mailto:vascorocha2000@tecnico.ulisboa.pt)

## Python3 Packages

Before running the code ensure that you have the following python3 packages installed:
* Networkx

```
pip install networkx
```
* Pandas
```
pip install pandas
```
* Matplotlib
```
pip install matplotlib
```

## Running
 Before running any program ensure you have the following directories:
 ```
 mkdir heterogeneous_sim
 ```
  ```
 mkdir homogeneous_sim
 ```
   ```
 mkdir random_heterogeneous_sim
 ```
```
 mkdir single_scale_sim
 ```

 To get a heatmap comming from a complete fully connected graph run:
 ```
 python3 homogeneous.py
 ```
   To get a heatmap comming from a single-scale graph run:
 ```
 python3 single_scale.py
 ```
   To get a heatmap comming from a Barabási-Albert scale-free random graph run:
 ```
 python3 random_heterogeneous.py
 ```
  To get a heatmap comming from a Barabási-Albert scale-free graph run:
 ```
 python3 heterogeneous.py
 ```
The generated files would be located in the /results directory.