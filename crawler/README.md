# Opinion Dynamics Crawler

[Usage]

Specify all the terms to search for in `Search.txt`. After that, execute:

`$ python main.py`

[Pre-Usage Tasks]

* Clone the repo using `git clone https://github.com/SpandanKumarSahu/OpinionDynamics.git`
* Create a `config_secret.txt` file and place the following in the mentioned order:
    * config_key
    * config__key_secret
    * access__key_token
    * access__key_secret

[Warning]

Don't add the `config_secret.txt` file. There's a `.gitignore` file in-place to stop it, from accidentally adding it. Yet, it can be added to the repository, if one uses `git add -f`. 

[Further Developments]

Follow the [this](https://python-twitter.readthedocs.io/en/latest/searching.html) article for descriptive information on determining the search query. [Some](https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./) help from here too.


