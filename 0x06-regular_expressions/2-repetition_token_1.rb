#!/usr/bin/env ruby
# Search the strings that starts with an 'h', `
# followed by an optional 'b', an optional 't', 
# and ends with an 'n'.
puts ARGV[0].scan(/hb?t?n/).join

