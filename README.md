Implementation of principles from the Good Research Guide Handbook

https://goodresearch.dev/index.html

https://github.com/patrickmineault/zipf

Using `poetry` rather than `conda`.

# What are the key differences?

It uses `poetry` rather than `conda` to package and manage dependencies.

I've created a command line to run this from.
See the line in the toml file:

```toml
[tool.poetry.scripts]
zipfs-law = "zipfs_law.cli:main"
```

[cli](./zipfs_law/cli.py) contains the workflow dag that creates the analysis.

I've separated most of the [input and output](./zipfs_law/inputoutput.py) into separate functions, as that big script was quite big.

----


# Workflow

I've downloaded these samples in the data directory.

- [Dracula](https://www.gutenberg.org/files/345/345-0.txt) → `data/dracula.txt`
- [Frankenstein](https://www.gutenberg.org/ebooks/42324.txt.utf-8) → `data/frankenstein.txt`
- [Jane Eyre](https://www.gutenberg.org/files/1260/1260-0.txt) → `data/jane_eyre.txt`

Now run at a terminal that has poetry activated:

```
zipfs-law data output
```

Open the notebook (`jupyter notebook`) and run all cells to check that the empirical distributions roughly look like the theoretical ones.
