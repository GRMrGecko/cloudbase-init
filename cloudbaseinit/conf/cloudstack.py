# Copyright 2016 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Config options available for the CloudStack metadata service."""

from oslo_config import cfg

from cloudbaseinit.conf import base as conf_base


class CloudStackOptions(conf_base.Options):

    """Config options available for the CloudStack metadata service."""

    def __init__(self, config):
        super(CloudStackOptions, self).__init__(config, group="cloudstack")
        self._options = [
            cfg.StrOpt(
                "metadata_base_url", default="http://10.1.1.1/",
                help="The base URL where the service looks for metadata",
                deprecated_name="cloudstack_metadata_ip",
                deprecated_group="DEFAULT"),
        ]

    def register(self):
        """Register the current options to the global ConfigOpts object."""
        group = cfg.OptGroup(self.group_name, title='CloudStack Options')
        self._config.register_group(group)
        self._config.register_opts(self._options, group=group)

    def list(self):
        """Return a list which contains all the available options."""
        return self._options
