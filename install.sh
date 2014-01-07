files=( "novaclient/v1_1/shell.py" 
	"novaclient/v1_1/hypervisors.py"
	"nova/api/openstack/compute/contrib/hypervisors.py"
	"nova/compute/api.py"
	"nova/compute/manager.py"
	"nova/compute/rpcapi.py"
	"nova/virt/libvirt/driver.py")

TARGET=/usr/lib/python2.6/site-packages
TMP=/tmp/kvm-qos

needback = true
if [ -d $TMP ];
then
    needback = false
else:
    mkdir $TMP
fi

echo "Backup to $TMP, and replacing..."
for name in ${files[@]}
do
    if [ ! -d $TMP/"${name%/*}" ];
    then
	mkdir -p $TMP/"${name%/*}"
    fi

    if [ needback ];
    then
        cp $TARGET/$name $TMP/$name
    fi

    cp $name $TARGET/$name
done
