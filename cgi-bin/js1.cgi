#!/usr/bin/env perl
warningsToBrowser(1);
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use strict;
use warnings;
use CGI qw/:standard/;
use HTML::Template;

print header();


my $tpl = HTML::Template->new(filename=>'JS.tpl');

if (!param())
{
    my $lawl = "RAWR";
    #$tpl->param(name=>$lawl);
    print $tpl->output();
}

else
{
	 my $tpl2 = HTML::Template->new(filename=>'JSR.tpl');
	 print $tpl2->output();
}
