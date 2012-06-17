#!/usr/bin/perl

$out = "perl_out.txt";

# Get info
print "What is your name? ";
chomp($name = <STDIN>);
print "How old are you? ";
chomp($age = <STDIN>);
print "What is your reddit username? ";
chomp($username = <STDIN>);

$st = "your name is $name, you are $age years old, and your username is $username\n";

# Print to screen
print $st;

# Print to file
open OUT, ">$out" or die "Cannot open $out for write :$!";
print OUT $st;
close OUT;
