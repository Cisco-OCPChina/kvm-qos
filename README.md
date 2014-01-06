KVM QoS
=======

KVM-QoS
-------
It's a component to support the openstack to partition the resource of CPU, network bandwidth.

Help
----
To install it should prepare a openstack with lastest Havana version. Pull the source code by "git clone https://github.com/iamjackhu/kvm-qos.git". Then run "sh install.sh", the shell will firstly backup somepython source code to /tmp/kvm-qos and after that it will replace some the nova and novaclient source code. 

After you reboot, it can work.

If you want to restoring back, please run "sh uninstall.sh", then the shell will restoring the related python code.  
