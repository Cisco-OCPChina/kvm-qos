
    @exception.wrap_exception(notifier=notifier, publisher_id=publisher_id())
    @reverts_task_state
    @wrap_instance_fault
    def partition(self, context, hypervisor, component, instance_list, percentage):
        self.driver.partition(hypervisor, component, instance_list, percentage)

