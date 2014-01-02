
    @exception.wrap_exception(notifier=notifier, publisher_id=publisher_id())
    @reverts_task_state
    @wrap_instance_fault
    def partition(self, context, hypervisor, component, instance_list, percentage):
        LOG.info("jack partition at compute manager %s", context.__dict__)
        self.driver.partition(component, instance_list, percentage)