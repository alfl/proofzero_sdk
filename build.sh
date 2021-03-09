#!/usr/bin/env bash
set -e
echo "-> Building library."
nbdev_build_lib --fname index.ipynb --fname core.ipynb
echo "-> Building docs."
nbdev_build_docs --fname index.ipynb --fname core.ipynb
