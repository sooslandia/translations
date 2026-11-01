#!/bin/bash
set -e
MD4C_VERSION=0.6.0
MDPO_VERSION=2.1.4
AUDITWHEEL_VERSION=6.8.2

wget https://github.com/mity/md4c/archive/refs/tags/v$MD4C_VERSION.tar.gz
tar xf v$MD4C_VERSION.tar.gz
cd md4c-$MD4C_VERSION
mkdir build
cd build
cmake ..
make
make install
ldconfig
cd ../..

mkdir temp-wheels
cd temp-wheels
# mdpo caps Requires-Python below 3.14 and pip enforces that even with --ignore-requires-python,
# so fetch mdpo alone and build its dependencies from its metadata.
pip download --no-cache-dir --no-deps --only-binary=:all: --python-version 3.12 --dest . mdpo==$MDPO_VERSION
pip install --no-cache-dir --no-deps --ignore-requires-python ./mdpo-*.whl
python -c 'import importlib.metadata as m; print("\n".join(m.requires("mdpo")))' > mdpo-requirements.txt
# md-ulb-pwrap pins PyO3 0.24, which refuses Python newer than 3.13 unless built against the stable ABI.
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 pip wheel --no-cache-dir --wheel-dir . -r mdpo-requirements.txt
pip install --no-cache-dir auditwheel==$AUDITWHEEL_VERSION
auditwheel repair --plat manylinux_2_34_x86_64 --wheel-dir /wheels ./pymd4c-*.whl ./md_ulb_pwrap-*.whl
rm ./pymd4c-*.whl ./md_ulb_pwrap-*.whl
mv *.whl /wheels/
cd ..
chown -R $1 /wheels
