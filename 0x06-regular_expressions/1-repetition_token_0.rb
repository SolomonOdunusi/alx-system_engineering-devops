#!/usr/bin/env ruby
# Search for the word hbt followed by {2 to 5} t's and then the letter n
puts ARGV[0].scan(/hbt{2,5}n/).join
