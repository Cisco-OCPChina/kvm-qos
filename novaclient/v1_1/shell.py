
@utils.arg('hypervisor', metavar='<hypervisor>', help='HyperVisor name or ID.')
@utils.arg('component', metavar='<component>', help='cpu memory network')
@utils.arg('vmlist', metavar='<vmlist>', help='vm1 vm2 vm3 or all')
@utils.arg('percentage', metavar='<percentage>', help='20% 30% 50% or average')
def do_partition(cs, args):
    """Partition the resource of one Hypervisor."""

    vm_list = args.vmlist.split(',')
    percent_list = args.percentage.split(',')

    if len(vm_list) != len(percent_list):
      print "vmlist and percetage should be equal!"
      return

   
    errorstr = None
    instance_list = []

    hypervisor = utils.find_resource(cs.hypervisors, args.hypervisor)
    if hypervisor != None:
        vmsonthishyper = cs.hypervisors.search(args.hypervisor, servers=True)
        search_opts = {'host': args.hypervisor, 'status': 'ACTIVE',}
        all_active_instance = cs.servers.list(search_opts=search_opts)
    
        active_host = {}
        for instance in all_active_instance:
          active_host[instance.name] = instance

        for vm in vm_list:
          if vm in active_host.keys():
            flavor =  _find_flavor(cs, active_host[vm]._info['flavor']['id'])
            instance = {'name':active_host[vm].name, 'percentage': percent_list.pop(),
                        'instance_name': active_host[vm]._info['OS-EXT-SRV-ATTR:instance_name'],
                        'vcpus': flavor.vcpus, 'ram': flavor.ram}
            instance_list.append(instance)
          else:
            errorstr = "domain:"+vm + " does not exists or ACTIVE!"
            print errorstr
            return
    else:
        print "The hypervisor %s does not exists!" % hypervisor
        return 

    cs.hypervisors.partition(args.hypervisor, args.component, instance_list, args.percentage)



