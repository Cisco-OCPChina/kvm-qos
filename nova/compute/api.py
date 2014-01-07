
    def partition(self, context, hypervisor, component, instance_list, percentage):
        """partition the resource of hypervisor."""
        self.compute_rpcapi.partition(context, hypervisor, component, instance_list, percentage)
