import octoprint.plugin

class ActiveFiltersPlugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			js=["js/knockout.persist.js", "js/active_filters.js"]
		)

__plugin_name__ = "Active Filters"
__plugin_implementation__ = ActiveFiltersPlugin()

