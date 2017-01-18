#Keyxtractor (Key extractor)

**TF-IDF** based keyword extraction tool, together with a chrome extension, aiming at helping read web pages.

daemon + chrome extension

## Server

	python extractor [PORT]

Though chrome plugin doesn't support **port** change yet.

## Chrome setup

This plugin is still under development.

Enter `chrome://extensions`

Development mode, load `./extension` folder

Enable highlighter by click on the **Keyxtractor** button

## Corpus

	tfidf_wiki.model	-	TF-IDF model
	wiki.dic		-	Wiki token id-to-doc dictionary

Corpus is created out of Wikipedia, customize as you wish. ( Corpus's code is a mess yet and not pushed. )

## Incomming Features!

1. Customize corpus to gain better user experience
2. Customize ratio of keywords to size
3. Bypass blocks like **code**
4. Better tokenizor, able to distinguish words like **sci-phi**, **White House**, etc.
5. Customize highlight css
