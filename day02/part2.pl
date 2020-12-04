#!/usr/bin/env perl
use strict;
use warnings;

my $part2 = 0;
while (<>) {
	my ($n1, $n2, $char, $pass) = $_ =~ /(\d+)-(\d+) (.): (.*)/;
	if (substr($pass, $n1 - 1, 1) eq $char xor substr($pass, $n2 - 1, 1) eq $char) {
		$part2++;
	}
}
print "$part2\n";
