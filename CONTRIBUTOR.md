# 

## Helpful commands

### Build the book

```bash
jupyter-book build <path_to_your_book>
```

### Publish the book

```bash
ghp-import -n -p -f _build/html
```

### Quirks

To make sure, that the Jupyter Notebooks run in both Jupyter Book and Google Colab, 
you need to use absolute links in the notebooks (also for images or interactive parts). 
For this reason, we use a pre-build system that preprocesses the book into a folder `_build_book`. 
From there you can build it and publish it. Run the following command in the `root` folder:

```bash
python build.py
```

if you want to build and publish the book to github pages, you can run the following command:

```bash
python build.py --all
```

You shouldn't directly edit anything in the folder `_build_book` but in the original foldr `book`. 
There, you should use jinja2 templating to make sure that the links are build correctly.

All the images and interactive parts should be stored in a folder called `book/_static/assets`. The links
in to these files (in the *.md or *.ipynb files) have the following format 
`{{ assets_url }}/<relative_path_from_assets_folder>`. If you want to link to other parts of the book use
`{{ book_url }}/<relative_path_from_book_folder>` or `{{ content_url }}/<relative_path_from_content_folder>`.

### Data
Data is stored in the folder `data` in the root directory

To load data in the notebooks, you should use raw urls like this:

```python
data = pd.read_pickle('{{ raw_data_url }}/drift_diffusion_models/coherence.pkl')
```
During development you can replace {{ repo_url }} with the actual repository url.

## Development

You can still run `jupyter-book build .` in the `book` folder, to test if everything works as expected but 
the links will not work in this build.

## Exercises and Solutions

We use post-processing to style exercise and solution cells.
To mark a cell as an exercise or solution cell, it needs to start with `### Exercise` or `### Solution` respectively.
Make sure that the cell is a markdown cell and not a code cell. Also, make sure that the solution is contained in one single cell.
