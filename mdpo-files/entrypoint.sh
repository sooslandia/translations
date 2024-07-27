#!/bin/bash
set -e
wget https://github.com/mity/md4c/archive/refs/tags/release-0.5.2.tar.gz
tar xf release-0.5.2.tar.gz
cd md4c-release-0.5.2
mkdir build
cd build
cmake ..
make
make install
ldconfig
cd ..

git clone --depth=1 https://github.com/NixOS/patchelf
cd patchelf
./bootstrap.sh
./configure
make
make check
make install
cd ..

mkdir temp-wheels
cd temp-wheels
pip wheel --no-cache-dir --wheel-dir . mdpo==2.0.1
pip install --no-cache-dir auditwheel==6.0.0
auditwheel repair --plat manylinux_2_34_x86_64 --wheel-dir /wheels ./pymd4c-*.whl
rm ./pymd4c-*.whl
mv *.whl /wheels/
cd ..
chown -R $1 /wheels
