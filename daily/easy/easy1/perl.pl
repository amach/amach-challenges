#!/usr/bin/env perl

$out = "perl_out.txt";

# Get info
print "What is your name? ";
chomp(my $name = <>);
print "How old are you? ";
chomp(my $age = <>);
print "What is your reddit username? ";
chomp(my $username = <>);

$st = "your name is $name, you are $age years old, and your username is $username\n";

# Print to screen
print $st;

# Print to file
open OUT, ">$out" or die "Cannot open $out for write :$!";
print OUT $st;
close OUT;
