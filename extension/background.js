chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
	page = request.text;
	tab = sender.tab;
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "http://localhost:27896/", true);
	xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	xhr.send(page);
	xhr.onreadystatechange = function() {
		if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
			chrome.tabs.insertCSS(tab.id, {code: '.high{color: red;}'});
			var lines = xhr.response.split('\n');
			chrome.tabs.executeScript(tab.id, {file: 'highlight.js'}, function() {
				for (var i=0;i<lines.length;i++){
					if (lines[i]){
						chrome.tabs.executeScript(tab.id, {code: "$('p').slice("+request.start+","+request.end+").highlight('" + lines[i] + "');"});
					}
				}
			});
		}
	};
	
}); 

chrome.browserAction.onClicked.addListener(function(tab) {
	chrome.tabs.executeScript(tab.ib, { file: 'jquery-3.1.1.min.js' }, function() {
		chrome.tabs.executeScript(tab.ib, {file: 'fetch.js'} );
	});
});
