#!/usr/bin/env ruby
# Search the string for a sequence of one or more capital letters
puts ARGV[0].scan(/[A-Z]*/).join
