Summary:	Beeps the PC speaker with control of frequency, duration, repetitions, etc.
Name:		beep
Version:	1.2.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.johnath.com/beep/%{name}-%{version}.tar.gz
URL:		http://johnath.com/beep/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
beep does what you'd expect: it beeps. But unlike printf("\a"), beep allows
you to control pitch, duration, and repetitions. Its job is to live inside
shell/perl scripts and allow more granularity than one has otherwise. It is
controlled completely through command line options. It's not supposed to be
complex, and it isn't - but it makes system monitoring (or whatever else it
gets hacked onto) that much more informative.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install beep $RPM_BUILD_ROOT%{_bindir}
install beep.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
