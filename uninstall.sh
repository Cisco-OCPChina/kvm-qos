files=( "novaclient/v1_1/shell.py" 
	"novaclient/v1_1/hypervisors.py"
	"nova/api/openstack/compute/contrib/hypervisors.py"
	"nova/compute/api.py"
	"nova/compute/manager.py"
	"nova/compute/rpcapi.py"
	"nova/virt/libvirt/driver.py")

TARGET=/usr/lib/python2.6/site-packages
TMP=/tmp/kvm-qos

if [ ! -d $TMP ];
then
    echo "$TMP does not exist, can't restoring..."
    exit
fi

echo "Restoring..."
for name in ${files[@]}
do
    cp -r $TMP/$name $TARGET/$name
done
