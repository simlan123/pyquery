#!/usr/bin/env python
'''Copyright (c) 2010, Simon Pfeiffer
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of the Author nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.'''

from optparse import OptionParser
import sys
from BeautifulSoup import BeautifulSoup,ResultSet
def main():
    #parse options
    parser = OptionParser()
    parser.add_option("-t", "--tag", dest="tag",
                  help="selects all Elements with the given TAGNAME", metavar="TAGNAME")
    parser.add_option("-i", "--id",
                   dest="id", 
                  help="Selects all elements with the given IDVALUE",metavar="IDVALUE")
    parser.add_option("-c", "--class",
                   dest="class_", 
                  help="Selects all elements with the given CLASSNAME",metavar="CLASSNAME")
    parser.add_option("-n","--number",dest="index",
                       help="If you have multiple matches you can specify the match by its NUMBER in the result. Lets assume you have 3 matches and want the second put -n 1 ,because the index is zero based.")

    parser.add_option("-x", "--textonly",
                   dest="textonly",action="store_true",default=False,
                  help="Prints out the result without any Htmltags")


    (options, args) = parser.parse_args()
    #read stdin and put to Bsoup
    text=sys.stdin.readlines()
    html="".join(text)
    soup=BeautifulSoup(html)
    soup.pretify
    #Initialize Options and result variable
    attribs={"class":options.class_ , "id":options.id}
    result=None
    #The parsing of the html with attribs defined above
    resultset=soup.findAll(name=options.tag, attrs=attribs, recursive=True, text=None, limit=None)                                                                 #todo ^ text
    if options.index :
    #check for index number
        resultset=resultset[int(options.index)]
    if options.textonly:
    #transform type resultset to string via iteration
        if isinstance(resultset,ResultSet) :
            result=""
            for i in resultset:
                result=result+" "+i.text
        else:
            result=resultset.text
    if not result:
    #This is a little messy
    # I have to iterate here to get rid of the [] that python normaly prints for lists 
        for i in resultset:
            print i
            print " "
    else:
        print result
        sys.exit(1)
        
if __name__=="__main__":
    main()
