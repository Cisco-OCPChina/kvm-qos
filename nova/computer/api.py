
    def partition(self, context, hypervisor, component, instance_list, percentage):
        """partition (ie, migrate) a running instance."""
        args = {
            "hypervisor": hypervisor,
            "component": component,
            "instance_list": instance_list,
            "percentage": percentage,
        }
        LOG.info("jack partition at compute api %s", args)
        self.compute_rpcapi.partition(context, hypervisor, component, instance_list, percentage)
