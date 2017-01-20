$.fn.highlight = function(word) {
    var pattern = new RegExp('\\b'+word+'\\b', 'gi'),
        repl = '<span class="high">' + word + '</span>';

    this.each(function() {
        $(this).contents().each(function() {
            if(this.nodeType === 3 && pattern.test(this.nodeValue)) {
                $(this).replaceWith(this.nodeValue.replace(pattern, repl));
            }
            else if(!$(this).hasClass('high')) {
                $(this).highlight(word);
            }
        });
    });
    return this;
};
