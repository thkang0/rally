from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.nova import utils
from rally.task import validation


class NovaFlavors(utils.NovaScenario):
    """Benchmark scenarios for Nova images."""

    @validation.required_services(consts.Service.NOVA)
    @validation.required_openstack(users=True)
    @scenario.configure(context={"cleanup": ["nova"]})
    def list_flavors(self, detailed=True, **kwargs):
        """List all images.
        Measure the "nova image-list" command performance.
        :param detailed: True if the image listing
                         should contain detailed information
        :param kwargs: Optional additional arguments for image listing
        """
	self.clients("nova").flavors.list(detailed)
        #self._list_flavors(detailed, **kwargs)
