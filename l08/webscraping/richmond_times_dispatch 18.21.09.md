1. copy the source code of the website
2. extract the links with this regex: text\?doc\=Perseus\%3atext\%3a2006\.05\.[0-9][0-9][0-9][0-9]
3. add the front part of the link with this regex: (find: ^) and (replace: http://www.perseus.tufts.edu/hopper/)
4. replace the first "text" of the link with "dltext" of the xml link (which can be found on the footer of the website) with the regex: (find: (?<=\/)text(?=\?) ) and (replace: dltext)
5. the links should look like this only the last 4 digits are unique: http://www.perseus.tufts.edu/hopper/dltext?doc=Perseus%3Atext%3A2006.05.0002
6. safe the file with the links (open bash in the terminal) and give wget the command to download
