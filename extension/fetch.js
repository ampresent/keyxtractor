function * paragraphing(){
	var t='';
	var last=0;
	var pa = $('p')
	for (var i=0;i<pa.length;i++){
		t+=pa[i].innerText;
		if (t.length>1023){
			yield {text:t, start:last, end:i};
			t=''
			last=i+1
		}
	}
	if (last < pa.length){
		yield {text:t, start:last, end:pa.length-1};
	}
}

var par = paragraphing();
for (var i of par){
	chrome.runtime.sendMessage('hdehcciknahicjmpododfboehibmfnfa', i);
}
