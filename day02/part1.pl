#!/usr/bin/env perl
use strict;
use warnings;

my $part1 = 0;
while (<>) {
	my ($n1, $n2, $char, $pass) = $_ =~ /(\d+)-(\d+) (.): (.*)/;
	my $count = () = $pass =~ /$char/g; # get the length
	if ($n1 <= $count  and $count <= $n2) {
		$part1++;
	}
}
print "$part1\n";
