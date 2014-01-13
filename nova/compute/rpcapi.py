
    def partition(self, ctxt, hypervisor, component, instance_list, percentage):
        
        self.cast(ctxt, self.make_msg('partition',
                hypervisor=hypervisor, component=component,
                instance_list=instance_list, percentage=percentage),
                _compute_topic(self.topic, ctxt, hypervisor, None))

