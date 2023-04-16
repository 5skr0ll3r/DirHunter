# DirHunter:
## Is a directory discovery tool

Wrote in Bash

```
=====================================================================================

      	 ##    # ###   #   # #       # ##      # ####### ###### ###
      	 # #   # #  #  #   # #       # # #     #    #    #      #  #
      	 #  #  # #   # #   # #       # #  #    #    #    #      #   #
      	 #   # # #  #  #####  #     #  #   #   #    #    ###### #  #
      	 #  #  # # #   #   #   #   #   #    #  #    #    #      # #
      	 # #   # #  #  #   #    # #    #     # #    #    #      #  #
      	 ##    # #   # #   #     #     #      #     #    ###### #   #

=====================================================================================
Usage: ./dirhunter.sh -h host -f file [-p threads] [-s] [-l] 
	-s: Disables ping
	-p: Set's thread count (Default threads: 20)
	-l Desables the logo (Default is on)
        
 ```

## Example

```
5skr0ll3r@sskroller DirHunter % ./dirhunter.sh -h google.com -f directory-list-2.3-medium.txt 
=====================================================================================

      	 ##    # ###   #   # #       # ##      # ####### ###### ###
      	 # #   # #  #  #   # #       # # #     #    #    #      #  #
      	 #  #  # #   # #   # #       # #  #    #    #    #      #   #
      	 #   # # #  #  #####  #     #  #   #   #    #    ###### #  #
      	 #  #  # # #   #   #   #   #   #    #  #    #    #      # #
      	 # #   # #  #  #   #    # #    #     # #    #    #      #  #
      	 ##    # #   # #   #     #     #      #     #    ###### #   #

=====================================================================================
Host google.com responded
File Located
=============================
-> http://google.com/index.html
-> http://google.com/images
-> http://google.com/2006
-> http://google.com/news
-> http://google.com/contact
-> http://google.com/about
-> http://google.com/about.html
-> http://google.com/search
-> http://google.com/privacy
-> http://google.com/privacy.html
-> http://google.com/privacy.js
-> http://google.com/blog
-> http://google.com/home
-> http://google.com/2005
-> http://google.com/sitemap.html
-> http://google.com/sitemap.xml
-> http://google.com/support
-> http://google.com/downloads
-> http://google.com/3.html
-> http://google.com/security
-> http://google.com/security.html
-> http://google.com/press
-> http://google.com/templates
-> http://google.com/services
-> http://google.com/2004
-> http://google.com/docs
^C
Killing all running threads...
=============================
```

```
charalamposrentoumis@CharalapossAir2 DirHunter % ./dirhunter.sh -h google.com -f directory-list-2.3-medium.txt -sl
File Located
=============================
-> http://google.com/index.html
-> http://google.com/images
^C
Killing all running threads...
=============================
```

Clone: `git clone https://github.com/5skr0ll3r/DirHunter`

Or just copy the code

