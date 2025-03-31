# ml-playground
ai sandbox 


preset: 

jupyter notebook
python 
fingers
toes  


1) create .ipynb file
2) set virtual env 

```
pipenv --python 3.11
pipenv install ipykernel==2.1.4
pipenv run python -m ipykernel install --user --name=YOUR_SYSTEM_NAME_HERE --display-name="YOUR_DISPLAY_NAME_HERE"
```
3) install dependencies 
```
pipenv install
```


Datasets:

- 20Newsgroups
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups
- iris
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris
- olivetti_faces
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html
- wine
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
- Toy:
https://scikit-learn.org/stable/datasets/toy_dataset.html
- Real world:
https://scikit-learn.org/stable/datasets/real_world.html

