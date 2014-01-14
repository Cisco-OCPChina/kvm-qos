
 
    @exception.wrap_exception()
    def partition(self, hypervisor, component, instance_list, percentage):
        if cmp(component, 'cpu') == 0:
            self._do_cpu_partition(instance_list, percentage)
        
    def _do_cpu_partition(self, instance_list, percentage):
        dirs = '/cgroup/cpu/libvirt/qemu/'
        for i in instance_list:
            quotas = int(100000 * float(i['percentage']) * int(i['vcpus']) )
            ipath = (dirs + i['instance_name'] + '/cpu.cfs_quota_us')
            utils.execute('chmod', '777', ipath, run_as_root=True)
            f = open(ipath, 'w')
            f.write(str(quotas))
            f.close()
            utils.execute('chmod', '644', ipath, run_as_root=True)

