Summary:	Beeps the PC speaker controlling frequency, duration, repetitions, etc.
Summary(pl.UTF-8):	Piszczy na głośniczku PC kontrolując częstotliwość, długość, powtórzenia itp.
Name:		beep
Version:	1.2.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.johnath.com/beep/%{name}-%{version}.tar.gz
# Source0-md5:	d541419fd7e5642952d7b48cbb40c712
URL:		http://johnath.com/beep/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
beep does what you'd expect: it beeps. But unlike printf("\a"), beep
allows you to control pitch, duration, and repetitions. Its job is to
live inside shell/perl scripts and allow more granularity than one has
otherwise. It is controlled completely through command line options.
It's not supposed to be complex, and it isn't - but it makes system
monitoring (or whatever else it gets hacked onto) that much more
informative.

%description -l pl.UTF-8
beep robi to, czego można się spodziewać: piszczy. Ale w
przeciwieństwie do printf("\a"), pozwala kontrolować wysokość dźwięku,
czas trwania i powtórzenia. Jego zadaniem jest żyć w skryptach Perla
lub powłoki i pozwalać na więcej, niż można zrobić bez niego.
Programem w całości steruje się z linii poleceń. Nie ma on być
skomplikowany - ale pozwala na bardziej informacyjne monitorowanie
systemu (czy cokolwiek, do czego zostanie użyty).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install beep $RPM_BUILD_ROOT%{_bindir}
gzip -dc beep.1.gz > $RPM_BUILD_ROOT%{_mandir}/man1/beep.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
