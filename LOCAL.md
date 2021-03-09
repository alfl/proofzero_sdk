# Proof Zero SDK Local Development Instructions

## Install

```bash
virualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Also [install Jekyll](https://jekyllrb.com/docs/installation/).

## Quickstart

Start `jupyter` to edit notebooks:

```bash
jupyter notebook
```

In a separate session, start Jekyll.

```bash
./serve_docs.sh
```

In a separate session, run your build and tests:

```bash
./build.sh
nbdev_test_nbs
```


