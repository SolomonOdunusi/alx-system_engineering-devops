#!/usr/bin/env ruby
# This search pattern matches any str that
# starts with h, followed by any char,
# and ends with n.
puts ARGV[0].scan(/^h.n$/).join

