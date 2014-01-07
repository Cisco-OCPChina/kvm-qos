
    @wsgi.serializers(xml=HypervisorIndexTemplate)
    def partition(self, req, id, body):
        context = req.environ['nova.context']
        authorize(context)

        self.api.partition(context, body['hypervisor'], body['component'], body['instance_list'], body['percentage'])

        resp = dict(hypervisors=[self._view_hypervisor(hyp, True)
                                 for hyp in db.compute_node_get_all(context)])
        return resp

