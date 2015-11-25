from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.neutron import utils
from rally.task import validation

class NeutronTest(utils.NeutronScenario):

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def list_agent(self, detailed=True):
        """
         list neutron agent
        """
	self.clients("neutron").list_agents()

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def list_external_net(self, detailed=True):
        """
         list neutron agent
        """
#        self._create_network(network_create_args or {})
#        self._list_networks()
	self.clients("neutron").retrieve_list()

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def list_secgroup_rule(self, detailed=True):
        """
         list neutron agent
        """
	self.clients("neutron").list_security_group_rules()

    @validation.required_services(consts.Service.NEUTRON)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["neutron"]})
    def list_service_provider(self, detailed=True):
        """
         list neutron agent
        """
	self.clients("neutron").list_service_providers()
