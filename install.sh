$TARGET=/usr/lib/python2.6/site-packages

$TMP=/tmp/kvm-qos
if[ -d $TMP ]
	rm -rf $tmp
fi

mkdir $TMP

diff -ruNa novaclient.orig novaclient > ${TMP}/novaclient.patch
diff -ruNa nova.orig nova > ${TMP}/nova.patch

echo "Patch the kvm-qos to ${TARGET}"
cd $TARGET
patch -p0 < ${TMP}/novaclient.patch
patch -p0 < ${TMP}/nova.patch
