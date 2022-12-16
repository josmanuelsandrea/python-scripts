
# Re-scaling images

This is a python script that generates down-scaled images from an specific image.




## Installation

Clone the repository

```bash
git clone https://github.com/josmanuelsandrea/python-scripts
```

Move to the folder

```bash
cd python-scripts/re-scaling-images
```

Install the dependencies

```bash
pip install -r requirements.txt
```

At this point you already have all setup!
## How to use

To start using this script, you need to add an image in the root folder with the name 
of `source`. (You can change this on `main.py`):

```python
image_name = 'source'
```

By default, the format is set to png. If you want to resize an 
image with another format, you can change it:

```python
image_format = 'png'
```

Now that you configured the app. You can execute it with

```bash
python3 main.py
```