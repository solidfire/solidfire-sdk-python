#!/usr/bin/env ruby
require 'pandoc-ruby'
@converter = PandocRuby.new('# Markdown Title', :from => :rst, :to => :markdown)
puts @converter.convert
