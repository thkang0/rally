from rally.common import log as logging
from rally import consts
from rally import exceptions
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.cinder import utils as cinder_utils
from rally.plugins.openstack.scenarios.glance import utils as glance_utils
from rally.plugins.openstack.scenarios.nova import utils as nova_utils
from rally.task import types
from rally.task import validation

class CinderTest(cinder_utils.CinderScenario,
                    nova_utils.NovaScenario,
                    glance_utils.GlanceScenario):
    """Benchmark scenarios for Nova images."""

    @validation.required_services(consts.Service.CINDER)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["cinder"]})
    def list_absolute_limits(self, detailed=True):
        """
         Lists absolute limits for a user.
        """
	self.clients("cinder").limits.get().absolute

    @validation.required_services(consts.Service.CINDER)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["cinder"]})
    def list_availability_zone(self, detailed=True):
        """
         Lists availability zone
        """
	self.clients("cinder").availability_zones.list()


    @validation.required_services(consts.Service.CINDER)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["cinder"]})
    def list_quota_usage(self, detailed=True):
        """
         Lists quota usage
        """
	self.admin_clients("cinder").quotas.get("admin")

    @validation.required_services(consts.Service.CINDER)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["cinder"]})
    def list_services(self, detailed=True):
        """
         Lists services
        """
	self.admin_clients("cinder").services.list()

