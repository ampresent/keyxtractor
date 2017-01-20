chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.tabs.executeScript(tab.ib, { file: 'jquery-3.1.1.min.js' }, function() {
		chrome.tabs.executeScript(tab.id, {file: 'highlight.js'}, function() {
			chrome.tabs.executeScript(tab.ib, {code: '$("div").children(":visible").not($(":has(pre)")).not($("pre")).text()'}, function(page){
				var xhr = new XMLHttpRequest();
				xhr.open("POST", "http://localhost:27896/", true);
				xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
				xhr.send(page);
				xhr.onreadystatechange = function() {
					if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
						chrome.tabs.insertCSS(tab.id, {code: '.high{color: red;}'});
						var lines = xhr.response.split('\n');
						for (var i=0;i<lines.length;i++){
							if (lines[i]){
								chrome.tabs.executeScript(tab.id, {code: "$('div').highlight('" + lines[i] + "');"});
							}
						}
					}
				};
			});
		});
	});
});
