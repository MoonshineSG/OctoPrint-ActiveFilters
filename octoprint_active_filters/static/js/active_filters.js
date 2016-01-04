$(function() {
	function activeFiltersPluginViewModel(viewModels) {
		var self = this;
		
		self.onAfterBinding = function () {
			terminal = viewModels[0];			
			terminal.activeFilters = terminal.activeFilters.extend({ persist: 'terminal.activeFilters' });
		}
	}

	OCTOPRINT_VIEWMODELS.push([
		activeFiltersPluginViewModel, 
		["terminalViewModel"],[]
	]);
});

