from rally.common import log as logging
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.keystone import utils as kutils
from rally.task import validation

class KeystoneTest(kutils.KeystoneScenario):
    """Benchmark scenarios for Nova images."""

    @validation.required_openstack(admin=True, users=True)
    @scenario.configure(context={"admin_cleanup": ["keystone"]})
    def list_role(self, detailed=True):
        """List all images.
         list user roles for given user.
        """
	self.admin_clients("keystone").roles.list()

    @validation.required_openstack(admin=True, users=True)
    @scenario.configure(context={"admin_cleanup": ["keystone"]})
    def get_token(self, detailed=True):
        """Get token.
         list the data about a token from the identity server
        """
	self.admin_clients("keystone").tokens.get_revoked()

    @validation.required_openstack(admin=True, users=True)
    @scenario.configure(context={"admin_cleanup": ["keystone"]})
    def list_endpoints(self, detailed=True):
        """
         List all available endpoints.
        """
	self.admin_clients("keystone").endpoints.list()
