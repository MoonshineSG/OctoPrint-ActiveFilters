import octoprint.plugin

class ActiveFiltersPlugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			js=["js/knockout.persist.js", "js/active_filters.js"]
		)

	def get_version(self):
		return self._plugin_version

	def get_update_information(self):
		return dict(
			active_filters=dict(
				displayName="Active Filters",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="MoonshineSG",
				repo="OctoPrint-ActiveFilters",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/MoonshineSG/OctoPrint-ActiveFilters/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Active Filters"
def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ActiveFiltersPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}


