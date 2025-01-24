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
From there you can build it and publish it.

You shouldn't directly edit anything in the folder `_build_book` but in the original foldr `book`. 
There, you should use jinja2 templating to make sure that the links are build correctly.

All the images and interactive parts should be stored in a folder called `book/_static/assets`. The links
in to these files (in the *.md or *.ipynb files) have the following format 
`{{ assets_url }}/<relative_path_from_assets_folder>`. If you want to link to other parts of the book use
`{{ book_url }}/<relative_path_from_book_folder>` or `{{ content_url }}/<relative_path_from_content_folder>`.


```python
