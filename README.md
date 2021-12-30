Implementation of principles from the Good Research Guide Handbook

https://goodresearch.dev/index.html

https://github.com/patrickmineault/zipf

Using `poetry` rather than `conda`.

# What are the key differences?

I've created a command line to run this from.
See the line in the toml file:

```toml
[tool.poetry.scripts]
zipfs-law = "zipfs_law.cli:main"
```

as well as the `cli.py` file.

----

I've downloaded these in the data directory.

- [Dracula](https://www.gutenberg.org/files/345/345-0.txt) → data/dracula.txt
- [Frankenstein](https://www.gutenberg.org/ebooks/42324.txt.utf-8) → data/frankenstein.txt
- [Jane Eyre](https://www.gutenberg.org/files/1260/1260-0.txt) → data/jane_eyre.txt
