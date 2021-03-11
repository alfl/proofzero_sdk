#!/usr/bin/env bash
set -e
echo "-> Building library."
nbdev_build_lib --fname "*.ipynb"
echo "-> Building docs."
nbdev_build_docs --fname "*.ipynb"
