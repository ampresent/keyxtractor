#Keyxtractor (Key extractor)

**TF-IDF** based keyword extraction tool, together with a chrome extension, aiming at helping read web pages.

daemon + chrome extension

## Server

	server.py [PORT]

Though chrome plugin does **not** support **port** customize yet.

server.py can **only** run **native** for now.

## Chrome setup

This plugin is still under development.

Enter `chrome://extensions`

Development mode, load `./extension` folder

Enable highlighter by click on the **Keyxtractor** button

## Corpus

	tfidf_wiki.model	-	TF-IDF model
	wiki.dic		-	Wiki token id-to-doc dictionary

###Generate your own corpus out of **wikipedia**
	
	train.py [wiki_dump_files] ...

## Incomming Features!

1. Customize ratio of keywords to size ( For now, only 10 keywords are extracted , you can tune it in server.py for now)
2. Better tokenizor, able to distinguish words like **sci-phi**, **White House**, etc.
3. Customize highlight css
4. Ready to deploy server side for **remote** server (rather than native for now)
