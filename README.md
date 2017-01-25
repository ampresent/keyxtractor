#Keyxtractor (Key extractor)

[中文](README_zh.md)

[English](README.md)

![](Sample.png)

**TF-IDF** based keyword extraction tool, together with a chrome extension, aiming at helping read web pages.

server side + chrome extension

## Server

	server.py [PORT]

Though chrome extension does **not** support **port** customize yet.

server.py can **only** run **native**(localhost) for now, not available for computing servers yet.

## Chrome setup

This extension is still under development.

Enter `chrome://extensions`

Development mode, load `./extension` folder

Enable highlighter by click on the **Keyxtractor** button

## Corpus

	tfidf_wiki.model	-	TF-IDF model
	wiki.dic		-	Wiki token id-to-doc dictionary

### Generate your own corpus out of **wikipedia**
	
	train.py [wiki_dump_files] ...

## Incomming Features!!

0. Better paragraphing ( density based algorithm, I suspect )
1. Customizable ratio of keywords to size ( For now, only 10 keywords per paragraph are extracted, you can tune it in server.py for now)
2. Better tokenizor ( able to distinguish words like **sci-phi**, **White House**, etc. )
3. Customizable highlight css
4. Ready-to-deploy server side for **remote** server (rather than native for now)

## ChangeLog

== 0.2 ==

train.py included ( Now you can customize your own corpus! )

~~Finer readable region discrimination~~ ( Accuracy optimization )

Whole word matching ( Accuracy optimization )

Paragraphing ( Also accuracy optimization, by giving the context )

## Searching for help

Too clumsy of me to handle front-end magic problems. Any help would mean a lot.
