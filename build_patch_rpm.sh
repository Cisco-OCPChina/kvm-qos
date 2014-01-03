#!/bin/bash

TARGET='rpmbuilder/SOURCES'

echo $TARGET

diff -ruNa novaclient.orig novaclient > ${TARGET}/novaclient.patch
diff -ruNa nova.orig nova > ${TARGET}/nova.patch

cd rpmbuilder
rpmbuild --define "_topdir ./" -ba ./kvmqos.spec
cp RPMS/x86_64/*.rpm ../
