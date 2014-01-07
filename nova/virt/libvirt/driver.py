
    @exception.wrap_exception()
    def partition(self, component, instance_list, percentage):
        
        LOG.info("jack partition at compute driver ")
        

    def _restart_cgconfig(self):
        result = os.popen('/etc/init.d/cgconfig restart').read()

    def _do_it(self, hypervisor, component, instance_list, percentage):
        dirs = '/cgroup/cpu/' + hypervisor.service['host']
        self._restart_cgconfig()
        if os.path.exists(dirs):
            os.removedirs(dirs)

        os.makedirs(dirs)

        for instance in instance_list:
            os.makedirs(dirs + '/' + instance['instance_name'])

            quotas = int(100000 * float(instance['percentage']) )
            f = open((dirs + '/' + instance['instance_name'] + '/cpu.cfs_quota_us'), 'w')
            f.write(str(quotas))
            f.close()

            processids = self._get_instance_processids(instance['instance_name'], instance['vcpus'])
            for pid in processids:
                f = open((dirs + '/' + instance['instance_name'] + '/tasks'), 'w')
                f.write(str(pid))
                f.close()
    
    def _get_instance_processids(self, instance_name, vcpus):
        detectcmd = ("ps -ef --sort size | grep kvm | grep %s | awk '{print $2}' | sed -n '2p' " % instance_name)
        processid = int(os.popen(detectcmd).read())
        result = []

        detectcmd = ("ls /proc/%s/task/" % processid)
        ls = os.popen(detectcmd).read()
        if ls != None:
                list = ls.split("\n")
                for i in list:
                        if len(i) > 0:
                                result.append(i)
        else: result.append(processid)
        return set(result)

