# Sylla Source
#### Online project repository and blog

This website is using the [Pelican static site generator](https://blog.getpelican.com/) with the [Attila Theme](https://github.com/arulrajnet/attila/tree/02dcad911ba1eb2d797a79ec008a810d89a2fde1). If you're interested in the mods I made to the theme checkout my [Attila fork.]()


**How to run in development**
Apply content and theme directory and start dev server.
`pelican content -s pelicanconf.py -t ../attila`
`pelican -l`

**Create new post**
`pelican `

**Run specific piece of content**
`pelican --write-selected output/testing.html`
`pelican --auto reload --listen`

**Other useful CLI commands**
Install a specific theme.
`pelican-themes -i theme-name-here`
