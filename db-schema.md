## Generating Database Diagrams and Working with PyDot

```
> pip install django-extensions
> pip install pydot

> Add 'django-extensions' in Settings.INSTALLED_APPS
```

#### Command to generate graph models

python manage.py graph_models --pydot -a -g -o \filename.png

#### Reference Commands

```
# to create model diagram for given specific Apps.
> python manage.py graph_models app1 app2 > filename.dot
OR
# to create model diagram for complete project definitions
> python manage.py graph_models -a > filename.dot
> dot -Tpng filename.dot -o filename.png
```
