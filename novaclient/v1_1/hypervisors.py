
    def partition(self, hypervisor, component, instance_list, percentage):
        """
        partition the resource of hypervisors.

        """
        url = ('/os-hypervisors/%s/partition' % hypervisor)
        body = {"hypervisor": hypervisor,
            "component": component,
            "instance_list": instance_list,
            "percentage": percentage}
        result = self._create(url, body, 'hypervisors', True)
        return result
        