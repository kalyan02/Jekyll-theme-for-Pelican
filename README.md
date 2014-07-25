Jekyll-theme-for-Pelican
========================

The Jekyll default theme is quite minimal, so I ported it to pelican.

## Installation

 - Copy `jekyll` folder to your pelican installation directory
 - Modify the variables from `pelicanconf.py` and either copy the file or use them in your own config
 - Change `THEME` variable in `pelicanconf.py` and `publishconf.py`
 
## Additional Variables

Here are some variables that are theme specific that you might want to set
 
 - `TWITTER_URL`
 - `GITHUB_URL`
 - `AUTHOR_EMAIL`
 - `LINKS` - These are the links that appear right beside the title
 
        LINKS = (
            ('    home', SITEURL), # Name, URL
            ('photos','http://blog.fuss.in'),
            ('about','#footer')
        )

